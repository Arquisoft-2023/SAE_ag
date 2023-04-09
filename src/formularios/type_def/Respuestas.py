import strawberry
from typing import List, Optional

@strawberry.type
class respuestas:
    respuesta: str
    nivelriesgo: str

@strawberry.input
class respuestas_input:
    respuesta: str
    nivelriesgo: str   
