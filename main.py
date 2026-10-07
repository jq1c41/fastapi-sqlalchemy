from fastapi import FastAPI
from src.mock import MockShipmentDetailRepository
from src.rest import ShipmentDetailsController

def create_app() -> FastAPI:
    repository = MockShipmentDetailRepository()
    controller = ShipmentDetailsController(repository)
    app = FastAPI()
    app.include_router(controller.router)
    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
