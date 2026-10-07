from abc import ABC, abstractmethod
from typing import Optional

class ShipmentDetailRepository(ABC):
    @abstractmethod
    def get_shipment_details_by_id(self, shipment_id: str)-> Optional[dict]:
        pass
    @abstractmethod
    def get_shipment_listings_by_page(self, page: int, n_listings: int)->Optional[list[dict]]:
        pass
