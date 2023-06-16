from graphql import GraphQLError
from pydantic import ValidationError
import strawberry
import requests
from dacite import from_dict


# from strawberry.types import Info
from gestionUsuarios.Server import url, port
import typing
from gestionUsuarios.utilities import *
from datetime import datetime
from gestionUsuarios.type_def.gestionUsuarios_td import *
from autenticacion.resolvers.autenticacion_rs import Query as autenticacionQuery, Mutation as autenticacionMutation




entryPoint = "bienestar"
urlApi = f'http://{url}:{port}/{entryPoint}'

entryPoint2 = "estudiante"
urlApi2 = f'http://{url}:{port}/{entryPoint2}'

@strawberry.type
class Query:
    
    #Usuarios

    @strawberry.field
    async def leer_usuarios(self) -> typing.List[UsuarioEsquema]:
        response = requests.request("GET", f'{urlApi}/usuarios')
        return gestion.gestionar_respuesta_micro(self, response, UsuarioEsquema, "lista")
    
    @strawberry.field
    async def buscar_un_usuario(self, usuario_un_a_buscar: str) -> UsuarioEsquema: 
        response = requests.request("GET", f'{urlApi}/usuarios/%7Busuario_un%7D?usuario_un_a_buscar={usuario_un_a_buscar}')
        if response.json() == {'detail': 'El usuario no existe'}:
            raise GraphQLError("El usuario no existe")
        else:
            return gestion.gestionar_respuesta_micro(self, response, UsuarioEsquema, "uno")
    
    
    @strawberry.field
    async def obtener_token_web(self, usuario_un_a_buscar: str) -> tokenResponse:
        response = requests.request("GET", f'{urlApi}/usuarios/web/%7BusuarioWeb%7D?usuario_web={usuario_un_a_buscar}')
        if response.json() == {'detail': 'El usuario no existe'}:
            raise GraphQLError("El usuario no existe")
        else:
            respuesta = tokenResponse(token=response.json()['token'], usuario=response.json()['usuario'])
            return respuesta
    
    
    @strawberry.field
    async def obtener_token_movile(self, usuario_un_a_buscar: str) -> tokenResponse:
        response = requests.request("GET", f'{urlApi}/usuarios/movile/%7BusuarioMovile%7D?usuario_movile={usuario_un_a_buscar}')
        if response.json() == {'detail': 'El usuario no existe'}:
            raise GraphQLError("El usuario no existe")
        else:
            respuesta = tokenResponse(token=response.json()['token'], usuario=response.json()['usuario'])
            return respuesta
    
    

    #Roles

    @strawberry.field
    async def leer_roles(self) -> typing.List[RolEsquema]:
        response = requests.request("GET", f'{urlApi}/usuariosRol')
        return gestion.gestionar_respuesta_micro(self, response, RolEsquema, "lista")

    #UsuariosRoles

    @strawberry.field
    async def leer_usuarios_roles(self) -> typing.List[UsuarioRolEsquema]:
        response = requests.request("GET", f'{urlApi}/usuariosRoles/usuariosRol')
        return gestion.gestionar_respuesta_micro(self, response, UsuarioRolEsquema, "lista")
    
    """
    #Departamentos

    @strawberry.field
    def leer_departamentos(self) -> typing.List[DepartamentoEsquema]:
        response = requests.request("GET", f'{urlApi}/informacionUniversidad/departamentos')
        return gestion.gestionar_respuesta_micro(self, response, DepartamentoEsquema, "lista")
    
    #Facultades

    @strawberry.field
    def leer_facultades(self) -> typing.List[FacultadEsquema]:
        response = requests.request("GET", f'{urlApi}/informacionUniversidad/facultades')
        return gestion.gestionar_respuesta_micro(self, response, FacultadEsquema, "lista")
    
    #Programas

    @strawberry.field
    def leer_programas(self) -> typing.List[ProgramaEsquema]:
        response = requests.request("GET", f'{urlApi}/informacionUniversidad/programasAcademicos')
        return gestion.gestionar_respuesta_micro(self, response, ProgramaEsquema, "lista")

    #DepartamentoProgramas

    @strawberry.field
    def leer_departamentos_programas(self) -> typing.List[DepartamentoProgramaEsquema]:
        response = requests.request("GET", f'{urlApi}/informacionUniversidad/departamentoProgramas')
        return gestion.gestionar_respuesta_micro(self, response, DepartamentoProgramaEsquema, "lista")
    
    #FacultadDepartamentos

    @strawberry.field
    def leer_facultades_departamentos(self) -> typing.List[FacultadDepartamentoEsquema]:
        response = requests.request("GET", f'{urlApi}/informacionUniversidad/facultadDepartamentos')
        return gestion.gestionar_respuesta_micro(self, response, FacultadDepartamentoEsquema, "lista")

    #InformacionAcademica

    @strawberry.field
    def leer_informacion_academica(self, cod_historia_academica : int) -> InformacionAcademicaEsquema:
        response = requests.request("GET", f'{urlApi}/estudiante/informacionAcademica/%7Busuario_un%7D?hist_academica={cod_historia_academica}')
        return gestion.gestionar_respuesta_micro(self, response, InformacionAcademicaEsquema, "uno")
    
    #HistorriaAcademicaEstudiante

    @strawberry.field
    def leer_historia_academica_estudiante(self) -> typing.List[HistoriaAcademicaEstudianteEsquema]:
        response = requests.request("GET", f'{urlApi}/estudiante/historiaAcademicaEstudiante')
        return gestion.gestionar_respuesta_micro(self, response, HistoriaAcademicaEstudianteEsquema, "lista")

    #InformacionPersonalDelEstudiante

    @strawberry.field
    def leer_informacion_personal_estudiante(self, usuario_un : str ) -> InformacionPersonalDelEstudianteEsquema:
        response = requests.get(f'{urlApi2}/informacionPersonal/{usuario_un}')
        dict = response.json()
        dict['fecha_nacimiento'] = datetime.strptime(dict['fecha_nacimiento'], '%Y-%m-%d').date()
        return from_dict(data_class=InformacionPersonalDelEstudianteEsquema, data=dict)

    """
        
@strawberry.type
class Mutation:

    #Usuarios

    @strawberry.mutation
    async def ingresar_usuario(self, item: UsuarioEsquemaInput) -> UsuarioEsquema:
        existenciaUsuario = await autenticacionMutation.verifyExistenceUserLDAP(self, usuario_un= item.usuario_un) # type: ignore
        if existenciaUsuario == False:
            raise GraphQLError("El usuario no existe en el LDAP")
        else:
            data = mapper_general.to_json(self, item)
            response = requests.request("POST",f'{urlApi}/usuarios', json=data)
            respuesta = gestion.gestionar_respuesta_micro(self, response, UsuarioEsquema, "uno")
            return respuesta
    
    @strawberry.mutation
    async def modificar_estado_usuario(self, usuario_un_a_buscar: str, estado_nuevo: bool) -> UsuarioEsquema:
        response = requests.request("PUT", f'{urlApi}/usuarios/%7Busuario_un%7D&%7Bestado%7D?usuario_un_a_buscar={usuario_un_a_buscar}&estado_nuevo={estado_nuevo}')
        return gestion.gestionar_respuesta_micro(self, response, UsuarioEsquema, "uno")
    
    @strawberry.mutation
    async def modificar_datos_usuario(self, item: UsuarioEsquemaInput) -> UsuarioEsquema:
        datos_nuevos= mapper_general.to_json(self, item)
        response = requests.put(f'{urlApi}/usuarios/%7Busuario_un%7D?usuario_un_a_econtrar={datos_nuevos["usuario_un"]}', json=datos_nuevos)
        return gestion.gestionar_respuesta_micro(self, response, UsuarioEsquema, "uno")
    
    @strawberry.mutation
    async def eliminar_usuario(self, usuario_un_a_buscar: str) -> typing.List[UsuarioEsquema]:
        response = requests.delete(f'{urlApi}/usuarios/%7Busuario_un%7D?usuario_un_a_econtrar={usuario_un_a_buscar}')
        return gestion.gestionar_respuesta_micro(self, response, UsuarioEsquema, "lista")


    

    @strawberry.mutation
    async def modificar_token_usuario_web (self, usuario_web: str, token_nuevo: str) -> tokenResponse:
        response = requests.put(f'{urlApi}/usuarios/web/%7BusuarioWeb%7D&%7BtokenWeb%7D?usuario_web={usuario_web}&token_nuevo={token_nuevo}')

        return tokenResponse(token=response.json()['token'], usuario=response.json()['usuario'])
    
    @strawberry.mutation
    async def modificar_token_usuario_movil (self, usuario_movile: str, token_nuevo: str) -> tokenResponse:
        response = requests.put(f'{urlApi}/usuarios/movile/%7BusuarioMovile%7D&%7BtokenMovile%7D?usuario_movile={usuario_movile}&token_nuevo={token_nuevo}')
        return tokenResponse(token=response.json()['token'], usuario=response.json()['usuario'])
    
    @strawberry.mutation
    async def eliminar_token_usuario_web (self, usuario_web: str) -> tokenResponse:

        response = requests.delete(f'{urlApi}/usuarios/web/%7BusuarioWeb%7D?usuario_web={usuario_web}')
        return tokenResponse(token=response.json()['token'], usuario=response.json()['usuario'])
    
    @strawberry.mutation
    async def eliminar_token_usuario_movil (self, usuario_movile: str) -> tokenResponse:
        response = requests.delete(f'{urlApi}/usuarios/movile/%7BusuarioMovile%7D?usuario_movile={usuario_movile}')
        return tokenResponse(token=response.json()['token'], usuario=response.json()['usuario'])

        
    

    #Roles

    @strawberry.mutation
    async def ingresar_rol(self, rol : str) -> typing.List[RolEsquema]:
        response = requests.request("POST",f'{urlApi}/usuariosRol?nuevo_rol={rol}')
        respuesta = gestion.gestionar_respuesta_micro(self, response, RolEsquema, "lista")
        return respuesta
    
    @strawberry.mutation
    async def modificar_nombre_rol(self, rol_a_buscar: str, rol_nuevo: str) -> RolEsquema:
        response = requests.put(f'{urlApi}/usuariosRol/%7Brol_id%7D?rol_a_econtrar={rol_a_buscar}&datos_nuevo_rol={rol_nuevo}')
        return gestion.gestionar_respuesta_micro(self, response, RolEsquema, "uno")
    
    @strawberry.mutation
    async def eliminar_rol(self, rol_a_buscar: str) -> typing.List[RolEsquema]:
        response = requests.delete(f'{urlApi}/usuariosRol/%7Brol_id%7D?rol_a_econtrar={rol_a_buscar}')
        return gestion.gestionar_respuesta_micro(self, response, RolEsquema, "lista")
    
    #UsuariosRoles

    @strawberry.mutation
    async def asignar_rol_a_usuario(self, usuario_un_a_buscar: str, rol_a_buscar: str) -> typing.List[UsuarioRolEsquema]:
        response = requests.request("POST",f'{urlApi}/usuariosRoles/%7Busuario_un%7D&%7Brol_id%7D?usuario_un_a_buscar={usuario_un_a_buscar}&rol_id_a_buscar={rol_a_buscar}')
        respuesta = gestion.gestionar_respuesta_micro(self, response, UsuarioRolEsquema, "lista")
        return respuesta
    
    @strawberry.mutation
    async def eliminar_usuario_y_rol(self, usuario_un_a_buscar: str) -> str:
        response = requests.delete(f'{urlApi}/usuariosRoles/usuariosRol/%7Busuario_un%7D?usuario_un_elim={usuario_un_a_buscar}')
        return response
    
    @strawberry.mutation
    async def modificar_usuario_y_rol(self, usuario_un: str, rol_nuevo: str) -> str:
        response = requests.put(f'{urlApi}/usuariosRoles/usuariosRol/%7Busuario_un%7D&%7Brol_id%7D?usuario_un_a_buscar={usuario_un}&rol_id_nuevo={rol_nuevo}')
        return response
    
    """
    #Departamentos

    @strawberry.mutation
    async def agregar_departameto(self, departamento_nuevo: str) -> typing.List[DepartamentoEsquema]:
        response = requests.post(f'{urlApi}/informacionUniversidad/departamentos?departamento_nuevo={departamento_nuevo}')
        return gestion.gestionar_respuesta_micro(self, response, DepartamentoEsquema, "lista")
    
    @strawberry.mutation
    async def modificar_nombre_departamento(self, departamento_a_econtrar: int,datos_nuevo_departamento: str) -> DepartamentoEsquema:
        response = requests.put(f'{urlApi}/informacionUniversidad/departamentos/%7Bdepartamento_id%7D?departamento_a_econtrar={departamento_a_econtrar}&datos_nuevo_departamento={datos_nuevo_departamento}')
        return gestion.gestionar_respuesta_micro(self, response, DepartamentoEsquema, "uno")
    
    @strawberry.mutation
    async def eliminar_departamento(self, departamento_a_econtrar: int) -> typing.List[DepartamentoEsquema]:
        response = requests.delete(f'{urlApi}/informacionUniversidad/departamentos/%7Bdepartamento_id%7D?departamento_a_econtrar={departamento_a_econtrar}')
        return gestion.gestionar_respuesta_micro(self, response, DepartamentoEsquema, "lista")
    
    #Facultades

    @strawberry.mutation
    async def agregar_facultad(self, facultad_nueva: str) -> typing.List[FacultadEsquema]:
        response = requests.post(f'{urlApi}/informacionUniversidad/facultades?facultad_nueva={facultad_nueva}')
        return gestion.gestionar_respuesta_micro(self, response, FacultadEsquema, "lista")
    
    @strawberry.mutation
    async def modificar_nombre_facultad(self, facultad_a_econtrar: int,datos_nuevo_facultad: str) -> FacultadEsquema:
        response = requests.put(f'{urlApi}/informacionUniversidad/facultades/%7Bfacultad_id%7D?facultad_nombre_nuevo={datos_nuevo_facultad}&facultad_a_modificar={facultad_a_econtrar}')
        return gestion.gestionar_respuesta_micro(self, response, FacultadEsquema, "uno")
    
    @strawberry.mutation
    async def eliminar_facultad(self, facultad_a_econtrar: int) -> typing.List[FacultadEsquema]:
        response = requests.delete(f'{urlApi}/informacionUniversidad/facultades/%7Bfacultad_id%7D?facultad_a_econtrar={facultad_a_econtrar}')
        return gestion.gestionar_respuesta_micro(self, response, FacultadEsquema, "lista")
    
    #Programas

    @strawberry.mutation
    async def agregar_programa(self, nombre_programa_nuevo: str, codigo_programa_nuevo : int) -> ProgramaEsquema:
        response = requests.post(f'{urlApi}/informacionUniversidad/programasAcademicos?programa_nuevo={nombre_programa_nuevo}&codigo_programa_nuevo={codigo_programa_nuevo}')
        return gestion.gestionar_respuesta_micro(self, response, ProgramaEsquema, "uno")
    
    @strawberry.mutation
    async def modificar_nombre_programa(self, programa_a_econtrar: int,datos_nuevo_programa: str) -> ProgramaEsquema:
        response = requests.put(f'{urlApi}/informacionUniversidad/programasAcademicos/%7Bprograma_id%7D?programa_nombre_nuevo={datos_nuevo_programa}&programa_a_modificar={programa_a_econtrar}')
        return gestion.gestionar_respuesta_micro(self, response, ProgramaEsquema, "uno")
    
    @strawberry.mutation
    async def eliminar_programa(self, programa_a_econtrar: int) -> typing.List[ProgramaEsquema]:
        response = requests.delete(f'{urlApi}/informacionUniversidad/programasAcademicos/%7Bprograma_id%7D?programa_a_econtrar={programa_a_econtrar}')
        return gestion.gestionar_respuesta_micro(self, response, ProgramaEsquema, "lista")
    
    #DepartamentosProgramas

    @strawberry.mutation
    async def agregar_departamento_programa(self, departamento_a_econtrar: int, programa_a_econtrar: int) -> typing.List[DepartamentoProgramaEsquema]:
        response = requests.post(f'{urlApi}/informacionUniversidad/departamentoProgramas?codigo_programa_nu={programa_a_econtrar}&id_departamento_nu={departamento_a_econtrar}')
        return gestion.gestionar_respuesta_micro(self, response, DepartamentoProgramaEsquema, "lista")
    
    @strawberry.mutation
    async def modificar_departamento_programa(self, codigo_programa_vi: int, departamento_nuevo: int) -> typing.List[DepartamentoProgramaEsquema]:
        response = requests.put(f'{urlApi}/informacionUniversidad/departamentoProgramas/%7Bdepartamento_id%7D&%7Bprograma_id%7D?codigo_programa_vi={codigo_programa_vi}&departamento_nuevo={departamento_nuevo}')
        return gestion.gestionar_respuesta_micro(self, response, DepartamentoProgramaEsquema, "lista")
    
    @strawberry.mutation
    async def eliminar_departamento_programa(self, codigo_programa_vi: int, departamento_nuevo: int) -> typing.List[DepartamentoProgramaEsquema]:
        response = requests.delete(f'{urlApi}/informacionUniversidad/departamentoProgramas/%7Bdepartamento_id%7D&%7Bprograma_id%7D?codigo_programa_vi={codigo_programa_vi}&departamento_nuevo={departamento_nuevo}')
        return gestion.gestionar_respuesta_micro(self, response, DepartamentoProgramaEsquema, "lista")
    
    #FacultadDepartamentos

    @strawberry.mutation
    async def agregar_facultad_departamento(self, facultad_a_econtrar: int, departamento_a_econtrar: int) -> FacultadDepartamentoEsquema:
        response = requests.post(f'{urlApi}/informacionUniversidad/facultadDepartamentos?id_facultad_nu={facultad_a_econtrar}&id_departamento_nu={departamento_a_econtrar}')
        return gestion.gestionar_respuesta_micro(self, response, FacultadDepartamentoEsquema, "uno")
    
    @strawberry.mutation
    async def modificar_facultad_departamento(self, id_facultad_vi: int, departamento_nuevo: int) -> FacultadDepartamentoEsquema:
        response = requests.put(f'{urlApi}/informacionUniversidad/facultadDepartamentos/%7Bfacultad_id%7D&%7Bdepartamento_id%7D?id_facultad_vi={id_facultad_vi}&departamento_nuevo={departamento_nuevo}')
        return gestion.gestionar_respuesta_micro(self, response, FacultadDepartamentoEsquema, "uno")
    
    @strawberry.mutation
    async def eliminar_facultad_departamento(self, id_facultad_eliminar: int, departamento_eliminar: int) -> typing.List[FacultadDepartamentoEsquema]:
        response = requests.delete(f'{urlApi}/informacionUniversidad/facultadDepartamentos/%7Bfacultad_id%7D&%7Bdepartamento_id%7D?id_facultad_eliminar={id_facultad_eliminar}&departamento_eliminar={departamento_eliminar}')
        return gestion.gestionar_respuesta_micro(self, response, FacultadDepartamentoEsquema, "lista")
    
    #InformacionAcademica

    @strawberry.mutation
    async def agregar_informacion_academica(self, item: InformacionAcademicaEsquemaInput ) -> InformacionAcademicaEsquema:
        data = mapper_general.to_json(self, item)
        response = requests.post(f'{urlApi}/estudiante/informacionAcademica', json=data)
        return gestion.gestionar_respuesta_micro(self, response, InformacionAcademicaEsquema, "uno")
    
    @strawberry.mutation
    async def modificar_informacion_academica(self, item: InformacionAcademicaEsquemaInput ) -> InformacionAcademicaEsquema:
        data = mapper_general.to_json(self, item)
        response = requests.put(f'{urlApi}/estudiante/informacionAcademica/%7Bhist_academica%7D', json=data)
        return gestion.gestionar_respuesta_micro(self, response, InformacionAcademicaEsquema, "uno")
    
    @strawberry.mutation
    async def eliminar_informacion_academica(self, hist_academica: int ) -> typing.List[InformacionAcademicaEsquema]:
        response = requests.delete(f'{urlApi}/estudiante/informacionAcademica/{hist_academica}')
        return gestion.gestionar_respuesta_micro(self, response, InformacionAcademicaEsquema, "lista")
    
    #HistorialAcademicaEstudiante

    @strawberry.mutation
    async def agregar_historial_academica_estudiante(self, historiaAcademica: int, usuario_un: str ) -> HistoriaAcademicaEstudianteEsquema:
        response = requests.post(f'{urlApi}/estudiante/historiaAcademicaEstudiante?historiaAcademica={historiaAcademica}&usuario_un={usuario_un}')
        return gestion.gestionar_respuesta_micro(self, response, HistoriaAcademicaEstudianteEsquema, "uno")
    
    @strawberry.mutation
    async def modificar_historial_academica_estudiante(self, historiaAcademica: int, usuario_un: str ) -> HistoriaAcademicaEstudianteEsquema:
        response = requests.put(f'{urlApi}/estudiante/historiaAcademicaEstudiante/{usuario_un}?historiaAcademica={historiaAcademica}')
        return gestion.gestionar_respuesta_micro(self, response, HistoriaAcademicaEstudianteEsquema, "uno")

    @strawberry.mutation
    async def eliminar_historia_academica_estudiante(self, usuario_un: str ) -> typing.List[HistoriaAcademicaEstudianteEsquema]:
        response = requests.delete(f'{urlApi}/estudiante/historiaAcademicaEstudiante/{usuario_un}')
        return gestion.gestionar_respuesta_micro(self, response, HistoriaAcademicaEstudianteEsquema, "lista")
    
    #InformacionPersonalDelEstudiante

    @strawberry.mutation
    async def agregar_informacion_personal_estudiante(self, item: InformacionPersonalDelEstudianteEsquemaInput ) -> InformacionPersonalDelEstudianteEsquema:
        item.fecha_nacimiento = str(item.fecha_nacimiento)
        data = mapper_general.to_json(self, item)
        response = requests.post(f'{urlApi2}/informacionPersonal', json=data)
        dict = response.json()
        dict['fecha_nacimiento'] = datetime.strptime(dict['fecha_nacimiento'], '%Y-%m-%d').date()
        return from_dict(data_class=InformacionPersonalDelEstudianteEsquema, data=dict)
    
    @strawberry.mutation
    async def modificar_informacion_personal_estudiante(self, item: InformacionPersonalDelEstudianteEsquemaInput ) -> InformacionPersonalDelEstudianteEsquema:
        item.fecha_nacimiento = str(item.fecha_nacimiento)
        data = mapper_general.to_json(self, item)
        response = requests.put(f'{urlApi2}/informacionPersonal/{item.usuario_un}', json=data)
        dict = response.json()
        dict['fecha_nacimiento'] = datetime.strptime(dict['fecha_nacimiento'], '%Y-%m-%d').date()
        return from_dict(data_class=InformacionPersonalDelEstudianteEsquema, data=dict)
    
    @strawberry.mutation
    async def eliminar_informacion_personal_estudiante(self, usuario_un: str ) -> str:
        response = requests.delete(f'{urlApi2}/informacionPersonal/{usuario_un}')
        return gestion.gestionar_respuesta_micro(self, response, InformacionPersonalDelEstudianteEsquema, "")

    """