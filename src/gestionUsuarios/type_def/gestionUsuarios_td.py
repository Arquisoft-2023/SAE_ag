import strawberry

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