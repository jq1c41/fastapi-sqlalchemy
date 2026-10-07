from typing import Optional

from src.port import ShipmentDetailRepository

from typing import Optional, List, Dict, Any

class MockShipmentDetailRepository(ShipmentDetailRepository):
    def __init__(self):
        self.data: List[Dict[str, Any]] = [
            {"id": "ship_001", "destination": "Kuala Lumpur", "status": "In Transit", "weight_kg": 450.5},
            {"id": "ship_002", "destination": "Penang", "status": "Delivered", "weight_kg": 120.0},
            {"id": "ship_003", "destination": "Johor Bahru", "status": "Pending", "weight_kg": 890.0},
            {"id": "ship_004", "destination": "Kuching", "status": "In Transit", "weight_kg": 310.2},
            {"id": "ship_005", "destination": "Kota Kinabalu", "status": "Cancelled", "weight_kg": 50.0},
        ]

    def get_shipment_listings_by_page(self, page: int, n_listings: int) -> Optional[List[Dict[str, Any]]]:
        start_index = (page - 1) * n_listings
        end_index = start_index + n_listings
        sliced_data = self.data[start_index:end_index]
        return sliced_data if sliced_data else None

    def get_shipment_details_by_id(self, shipment_id: str) -> Optional[Dict[str, Any]]:
        shipment = next((item for item in self.data if item.get("id") == shipment_id), None)
        return shipment
