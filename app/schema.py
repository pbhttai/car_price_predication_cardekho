from pydantic import BaseModel, Field
from enum import Enum

class FuelType(str, Enum):
    petrol = "Petrol"
    diesel = "Diesel"
    cng = "CNG"

class SellerType(str, Enum):
    dealer = "Dealer"
    individual = "Individual"

class TransmissionType(str, Enum):
    manual = "Manual"
    automatic = "Automatic"

class CarFeatures(BaseModel):
    Car_Name: str = Field(..., examples=["ritz","alto"])
    Year: int = Field(..., examples=[2014])
    Present_Price: float = Field(..., examples=[5.59])
    Fuel_Type: FuelType
    Seller_Type: SellerType
    Transmission: TransmissionType
    Owner: int = Field(..., ge=0, le=3, examples=[0], description="Number of previous owners (0,1 or 3)")

class PredicationResponse(BaseModel):
    predication_price: float
