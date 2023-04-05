from dacite import from_dict

class mapper:
    def mapper_lista(self, response, data_class):
        # data2 = json.dumps(data, indent = 4)
        # print(data2)
        lista_data = []
        data = response.json()
        for item in data:
            lista_data.append(from_dict(data_class=data_class, data=item))
        return lista_data
    
    def mapper_uno(self, response, data_class):
        data = response.json()
        res = from_dict(data_class=data_class, data=data)
        return res
    
    def to_json(self, item, metodo):
        data = {}
        try:
            if metodo == "asignar":
                data  = {
                    "usuario_un_estudiante": item.usuario_un_estudiante,	
                    "usuario_un_tutor": item.usuario_un_tutor,
                    "es_tutor": "Actual"
                }
            return data
        except Exception as e:
            print(str({ "description": "Error Servidor", "status": 500, "error": str(e)}))
            return data

class error:
    def gestionar_respuesta_micro(self, response, data_class = None, tipo_respuesta = "str", key = None):
        try:
            data = response.json()
            if response.status_code == 200:
                if tipo_respuesta == "lista":
                    return mapper.mapper_lista(self, response, data_class)
                elif tipo_respuesta == "uno":
                    return mapper.mapper_uno(self, response, data_class)
                return data[key]
            else:
                return str({ "description": data["description"], "status": data["status"] })
        except Exception as e:
            return str({ "description": "Error Servidor", "status": 500 })