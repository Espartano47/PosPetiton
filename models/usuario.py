from pydantic import BaseModel

class UsuarioLogin(BaseModel):
    username: str
    password: str

class UsuarioOut(BaseModel):
    username: str
    role: str
