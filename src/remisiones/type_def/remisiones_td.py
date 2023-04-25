from datetime import date
import strawberry

#Tipos de Remision
@strawberry.input
class TipoRemisionInput:
    tipoRemision : str

@strawberry.type
class TiposRemision:
    idTipoRemision : int
    tipoRemision : str

#Solicitudes de Remision
@strawberry.type
class SolicitudesRemision:
    idSolicitudRemision : int
    idTipoRemision : int
    tipoRemision : str
    usuarioUnEstudiante : str
    programaCurricular : str
    usuarioUnDocente : str
    fechaSolicitudRemision : str
    justificacion : str
    estado : bool

@strawberry.input
class NuevaSolicitudRemisionInput:
    idTipoRemision : int
    usuarioUnEstudiante : str   
    programaCurricular : str
    usuarioUnDocente : str
    justificacion : str

@strawberry.type
class NuevaSolicitudRemision:
    idSolicitudRemision : int
    tipoRemision : TiposRemision
    usuarioUnEstudiante : str
    programaCurricular : str
    usuarioUnDocente : str
    fechaSolicitudRemision : str
    justificacion : str
    estado : bool

#Primeras Escuchas
@strawberry.type
class PrimerasEscuchas:
    idPrimeraEscucha : int
    observacion : str
    fechaPrimeraEscucha : str
    realizada : bool

@strawberry.input
class PrimeraEscuchaInput:
    observacion : str
    realizada : bool

#Remisiones
@strawberry.type
class Remisiones:
    idRemision : int
    idSolicitudRemision : int
    usuarioUnEstudiante : str
    programaCurricular : str
    usuarioUnDocente : str
    tipoRemision : str
    justificacionSolicitud : str
    idPrimeraEscucha : int
    observacionPrimeraEscucha : str
    fechaEnvioRemision : str
    remisionEfectiva : bool
    primeraEscuchaRealizada : bool
    
@strawberry.input
class NuevaRemisionInput:
    idSolicitudRemision : int
    fechaPrimeraEscucha : str

@strawberry.type
class NuevaRemision:
    idRemision : int
    solicitudRemision : NuevaSolicitudRemision
    primeraEscucha : PrimerasEscuchas
    fechaEnvioRemision : str
    remisionEfectiva : bool