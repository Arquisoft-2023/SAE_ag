from dacite import from_dict

class mapper_tutoria:
    def to_json(self, item, metodo = "None"):
        data = {}
        try:
            data = item.__dict__
            if metodo == "asignar":
                data["es_tutor"] = "Actual"
            elif metodo == "crear_obs":
                data["lista_observacion"] = mapper.mapper_to_json_lista(self, item.lista_observacion)
            return data
        except Exception as e:
            print(gestion.imprimir_error(self,"Error al convertir a to_json", 500, e))
            return data

class mapper:
    def mapper_lista(self, response, data_class):
        lista_data = []
        data = response.json()
        for item in data:
            lista_data.append(from_dict(data_class=data_class, data=item))
        return lista_data
    
    def mapper_uno(self, response, data_class):
        data = response.json()
        res = from_dict(data_class=data_class, data=data)
        return res
    
    def mapper_to_json_lista(self, data_list):
        lista_data = []
        for elemento in data_list:
            lista_data.append(elemento.__dict__)
        return lista_data

class gestion:
    def gestionar_respuesta_micro(self, response, data_class = None, tipo_respuesta = "Primitivo", key = None):
        try:
            data = response.json()
            if response.status_code == 200:
                if tipo_respuesta == "lista":
                    return mapper.mapper_lista(self, response, data_class)
                elif tipo_respuesta == "uno":
                    return mapper.mapper_uno(self, response, data_class)
                elif tipo_respuesta == "uno_con_key":
                    return data[key]
                elif tipo_respuesta == "boolean":
                    return gestion.imprimir_mensaje(self, "True", 200)
                return data
            else:
                return gestion.imprimir_mensaje(self, data["description"], data["status"])
        except Exception as e:
            return gestion.imprimir_error(self,"Error al mapear", 500, e)
    
    def imprimir_error(self, description, status, e):
        return (str({ "description": description, "status": status, "error": str(e)}))
    
    def imprimir_mensaje(self, description, status):
        return (str({ "description": description, "status": status }))
