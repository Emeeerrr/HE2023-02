# Esta vendria a ser el API
# SOAPythonSecurity

################################################################################################

from fastapi import FastAPI

from Domain.Usuario.UsuarioModel import Usuario

app: FastAPI = FastAPI (title='SOA Python Security Emerson Rueda', description='IUE HE 2023-02')


################################################################################################

@app.get("/autenticarusuario",
         summary="Autenticar Usuario",
         description="API Para Autenticar Usuario via GET",
         tags=["AutenticarUsuario"]
         )

async def autenticar_usuario(usuario: str | None = None, clave: str | None = None):
    salida: str ="usuario: "+usuario +", clave:  "+ clave #Enriquesimiento de la carga util
    return salida

@app.post("/autenticarusuario",
          response_model=Usuario,
          summary="Autenticar Usuario",
          description="API Para Autenticar Usuario Via POST",
          tags=["AutenticarUsuario"]
          )

async def autenticar_usuario(usuario: Usuario | None = None):
    usuario.salida= "usuario: "+usuario.usuario +", clave:"+usuario.clave #Enriquesimiento de la carga util
    return usuario

################################################################################################