from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class RoleBase(BaseModel):
    name: str
    permisos: Optional[List[str]] = []

class RoleCreate(RoleBase):
    pass

class RoleUpdate(BaseModel):
    name: Optional[str] = None
    permisos: Optional[List[str]] = None

class RoleOut(RoleBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True