import strawberry

@strawberry.input
class UsuarioAuthInput:
    usuario_un : str
    password: str
    tokentype: str
@strawberry.type
class UsuarioAuthGeneral:
    message: str
    #rol: str
@strawberry.type
class UsuarioAuthWithToken:
    ldapRes : str
    usuario_un : str
    token: str
    
