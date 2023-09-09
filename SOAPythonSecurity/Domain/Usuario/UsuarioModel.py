



#UsuarioModel

from pydantic import BaseModel


################################################################################################


class Usuario (BaseModel):
    usuario: str | None = None
    clave: str | None = None
    salida:str | None = None  #Enriqueser la carga util