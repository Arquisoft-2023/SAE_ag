import strawberry

@strawberry.type
class obs:
    fecha_obs: str
    descripcion: str

@strawberry.input
class obs_input:
    fecha_obs: str
    descripcion: str