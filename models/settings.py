from pydantic import BaseModel
from typing import Optional

class SettingsBase(BaseModel):
    system_name: str
    company_name: str
    currency: str
    language: str
    tax: Optional[float] = 0
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    logo: Optional[str] = None

class SettingsCreate(SettingsBase):
    pass

class SettingsUpdate(SettingsBase):
    pass