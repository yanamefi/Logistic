from pydantic import BaseModel, model_validator
from typing import List, Optional
from enum import Enum


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    password_confirmation: str

    @model_validator(mode='after')
    def check_passwords_match(cls, values):
        password = values.password
        password_confirmation = values.password_confirmation
        if password != password_confirmation:
            raise ValueError('Passwords do not match')
        return values


class DriverLicenseType(str, Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"


class TruckDriverCreate(UserBase):
    acc_status: str = "driver"
    driver_license_type: DriverLicenseType
    driver_license_number: str
    experience_years: int
    vehicle_types: List[str]
    has_international_permit: bool


class LogisticianCreate(UserBase):
    acc_status: str = "logistician"
    company_name: Optional[str] = None
    position: str
    specialization: List[str]
    experience_years: int


class BusinessOwnerCreate(UserBase):
    acc_status: str = "business"
    company_name: str
    business_type: str
    company_size: int
    logistics_frequency: str
    cargo_types: List[str]


class TransportCompanyOwnerCreate(UserBase):
    acc_status: str = "company"
    company_name: str
    fleet_size: int
    vehicle_types: List[str]
    operation_area: str
    special_permits: Optional[List[str]] = None


class Login(BaseModel):
    email: str
    password: str
