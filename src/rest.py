from fastapi import APIRouter, HTTPException, Query
from src.port import ShipmentDetailRepository

class ShipmentDetailsController:
    def __init__(self, repository: ShipmentDetailRepository) -> None:
        self.repository = repository
        self.router = APIRouter(prefix="/shipments", tags=["shipments"])
        self._register_routes()

    def _register_routes(self) -> None:
        self.router.add_api_route("/{shipment_id}", self.get_sd_by_id, methods=["GET"])
        self.router.add_api_route("", self.get_sd_listings_by_page, methods=["GET"])

    def get_sd_by_id(self, shipment_id: str) -> dict:
        row = self.repository.get_shipment_details_by_id(shipment_id)
        if row is None:
            raise HTTPException(status_code=404, detail="Shipment not found")
        return row

    def get_sd_listings_by_page(
        self,
        page: int = Query(1, ge=1),
        size: int = Query(20, ge=1, le=100),
    ) -> list[dict]:
        rows = self.repository.get_shipment_listings_by_page(page, size)
        if rows is None:
            raise HTTPException(status_code=404, detail="No shipments listings found")
        return rows