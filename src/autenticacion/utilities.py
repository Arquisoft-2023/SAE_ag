from dacite import from_dict


class mapper_general:
    def to_json(self, item):
        data = {}
        try:
            data = item.__dict__
            return data
        except Exception as e:
            print(gestion.imprimir_error(self,"Error al convertir a to_json", 500, e))
            return data
class mapper:
    def mapper_uno(self, response, data_class):
        data = response.json()
        print(data)
        res = from_dict(data_class=data_class, data=data)
        return res

class gestion:
    def gestionar_respuesta_micro(self, response, data_class = None, tipo_respuesta = "Primitivo", key = None):
        try:
            data = response.json()
            if response.status_code == 200:
                if tipo_respuesta == "uno":
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