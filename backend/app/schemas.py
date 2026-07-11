from pydantic import BaseModel


class CarInput(BaseModel):
    car_name: str
    brand: str
    model: str
    vehicle_age: int
    km_driven: int
    seller_type: str
    fuel_type: str
    transmission_type: str
    mileage: float
    engine: int
    max_power: float
    seats: int