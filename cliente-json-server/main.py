import requests
import json

empleado = {
    "codigo":44,
    "nombre": "Andres",
    "apellido": "Otro"
}
obtener = requests.post("http://127.0.0.1:3000", data = json.dumps(empleado))
# obtener = requests.get("http://127.0.0.1:5005")
print(obtener.json())