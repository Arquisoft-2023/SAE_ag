import strawberry

@strawberry.type
class rems:
    usuario_estudiante1: str
    usuario_tutor1: str
    tipo_remision: str
    estado_remision: str
    estado_solicitud: str
    estado_PE: str
    fecha_PE: str
    observacion_PE: str
    justificacion: str
    fecha_solicitud: str
    fecha_aprobacion: str

@strawberry.input
class rems_input:
    usuario_estudiante1: str
    usuario_tutor1: str
    tipo_remision: str
    estado_remision: str
    estado_solicitud: str
    estado_PE: str
    fecha_PE: str
    observacion_PE: str
    justificacion: str
    fecha_solicitud: str
    fecha_aprobacion: str