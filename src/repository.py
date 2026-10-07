from typing import Optional

from sqlalchemy import text
from src.config import SQLAlchemyConfig
from src.port import ShipmentDetailRepository

class SqlAlchemyShipmentDetailRepository(ShipmentDetailRepository):
    def __init__(self, config: SQLAlchemyConfig):
        try:
            self.engine = config.create_engine()
        except Exception as e:
            raise RuntimeError(f"Failed to initialize database engine: {e}")

    def get_shipment_listings_by_page(self, page: int, n_listings: int) -> Optional[list[dict]]:
        stmt = text(
            """
            SELECT * FROM shipment_details 
            ORDER BY id 
            OFFSET :offset ROWS 
            FETCH NEXT :limit ROWS ONLY
            """
        )

        offset_value = max(0, (page - 1) * n_listings)

        with self.engine.connect() as conn:
            result = conn.execute(
                stmt,
                {"limit": n_listings, "offset": offset_value}
            )
            # Use ._mapping to safely convert SQLAlchemy 2.0 rows to dictionaries
            return [dict(row._mapping) for row in result]

    def get_shipment_details_by_id(self, shipment_id: str) -> Optional[dict]:
        stmt = text("SELECT * FROM shipment_details WHERE id = :shipment_id")
        with self.engine.connect() as conn:
            result = conn.execute(stmt, {"shipment_id": shipment_id})
            row = result.fetchone()
            if row:
                return dict(row._mapping)  # Use ._mapping to safely convert SQLAlchemy 2.0 row to dictionary
            return None