import strawberry
from typing import List, Optional

@strawberry.type
class posiblesrespuestas:
    respuesta: str
    pnivelriesgo: str

@strawberry.input
class posiblesrespuestas_input:
    respuesta: str
    pnivelriesgo: str    
