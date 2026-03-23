from pydantic import BaseModel
from typing import Optional

class CustomerBase(BaseModel):
    name: str
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    document: Optional[str] = None
    status: Optional[int] = 1


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(CustomerBase):
    pass