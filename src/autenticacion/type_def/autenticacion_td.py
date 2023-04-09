import strawberry

@strawberry.input
class UsuarioAuthInput:
    usuario_un : str
@strawberry.type
class UsuarioAuthGeneral:
    message: str
    #rol: str
@strawberry.type
class UsuarioAuthWithToken:
    usuario_un : str
    estado : bool
    token: str
    
