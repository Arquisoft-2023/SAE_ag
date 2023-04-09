from datetime import date
import strawberry

#Tipos de Remision
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

@strawberry.type
class NuevaSolicitudRemision:
    idTipoRemision : int
    usuarioUnEstudiante : str
    programaCurricular : str
    usuarioUnDocente : str
    justificacion : str

#Primeras Escuchas
@strawberry.type
class PrimerasEscuchas:
    idPrimeraEscucha : int
    observacion : str
    fechaPrimeraEscucha : str
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