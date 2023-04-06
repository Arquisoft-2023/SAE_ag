import strawberry

#Usuarios
@strawberry.type
class UsuarioEsquema:
    usuario_un : str
    estado : bool
    nombres : str
    apellidos : str
    documento : str
    tipo_documento : bool

@strawberry.input
class UsuarioEsquemaInput:
    usuario_un : str
    estado : bool
    nombres : str
    apellidos : str
    documento : str
    tipo_documento : bool


#Roles
@strawberry.type
class RolEsquema:
    rol: str
    rol_id: int

@strawberry.input
class RolEsquemaInput:
    rol: str

#UsuariosRoles
@strawberry.type
class UsuarioRolEsquema:
    usuario_un: str
    rol_id: int

@strawberry.input
class UsuarioRolEsquemaInput:
    usuario_un: str
    rol_id: int