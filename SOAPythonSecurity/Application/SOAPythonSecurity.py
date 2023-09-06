# Esta vendria a ser el API
# SOAPythonSecurity

################################################################################################

from fastapi import FastAPI

app: FastAPI = FastAPI (title='SOA Python Security Emerson Rueda', description='IUE HE 2023-02')


################################################################################################

@app.get("/autenticarusuario",
         summary="Autenticar Usuario",
         description="API Para Autenticar Usuario",
         tags=["AutenticarUsuario"])

async def autenticar_usuario(usuario: str | None = None, clave: str | None = None):
    salida: str ="usuario: "+usuario +", clave:  "+ clave
    return salida

################################################################################################