import strawberry
import datetime

#Usuarios
@strawberry.type
class UsuarioEsquema:
    usuario_un : str
    estado : bool
    nombres : str
    apellidos : str
    documento : str
    tipo_documento : bool
    token_web : str
    token_movile : str

@strawberry.input
class UsuarioEsquemaInput:
    usuario_un : str
    estado : bool
    nombres : str
    apellidos : str
    documento : str
    tipo_documento : bool
    token_web : str
    token_movile : str

@strawberry.type
class tokenResponse:
    token: str
    usuario:str

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

"""
#Departamentos
@strawberry.type
class DepartamentoEsquema:
    id_departamento : int
    nombre_departamento : str

#Facultades
@strawberry.type
class FacultadEsquema:
    id_facultad : int
    nombre_facultad : str

#Programas
@strawberry.type
class ProgramaEsquema:
    codigo_programa : int
    nombre_programa : str

#DepartamentoProgramas

@strawberry.type
class DepartamentoProgramaEsquema:

    codigo_programa : int    
    id_departamento : int

#FacultadDepartamentos
@strawberry.type
class FacultadDepartamentoEsquema:
    id_facultad : int
    id_departamento : str


#InformacionAcademica
@strawberry.type
class InformacionAcademicaEsquema:
    historia_academica : int
    porcentaje_de_avance : float
    estado_historia : bool
    papi : float
    papa : float
    codigo_programa_academico : int

@strawberry.input
class InformacionAcademicaEsquemaInput:
    historia_academica : int
    porcentaje_de_avance : float
    estado_historia : bool
    papi : float
    papa : float
    codigo_programa_academico : int

#HistoriaAcademicaEstudiante
@strawberry.type
class HistoriaAcademicaEstudianteEsquema:
    cod_historia_academica : int
    usuario_un : str

#InformacionPersonalDelEstudiante
@strawberry.type
class InformacionPersonalDelEstudianteEsquema:
    fecha_nacimiento : datetime.date
    sexo : bool
    ciudad_nacimiento : str
    direccion_residencia : str
    ciudad_residencia : str
    telefono : str
    correo_alterno : str
    eps : str
    hijos : bool
    nombre_apellido_acudiente : str
    relacion_acudiente : str
    telefono_acudiente : str
    usuario_un : str

@strawberry.input
class InformacionPersonalDelEstudianteEsquemaInput:
    fecha_nacimiento : datetime.date
    sexo : bool
    ciudad_nacimiento : str
    direccion_residencia : str
    ciudad_residencia : str
    telefono : str
    correo_alterno : str
    eps : str
    hijos : bool
    nombre_apellido_acudiente : str
    relacion_acudiente : str
    telefono_acudiente : str
    usuario_un : str
"""