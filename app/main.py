from fastapi import FastAPI
from fastapi.responses import Response, JSONResponse
from contextlib import asynccontextmanager
from app.schema import CarFeatures, PredicationResponse
from app.model import predict_price, load_artifacts


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    load_artifacts()
    yield
    # shutdown (optional)


app = FastAPI(title="Car Price Prediction API", version="1.0", lifespan=lifespan)


@app.get("/")
def test():
    return JSONResponse(
        status_code=200, content={"success": True, "message": "this is test route"}
    )

@app.post("/predict", response_model=PredicationResponse)
def predict(features: CarFeatures):
    price=predict_price(features.model_dump())
    return PredicationResponse(predication_price=price)
