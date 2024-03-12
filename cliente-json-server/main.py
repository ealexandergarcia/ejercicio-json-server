import requests
import json

empleado = {
    "codigo":44,
    "nombre": "Andres",
    "apellido": "Otro"
}
# obtener = requests.get("http://127.0.0.1:5005")
# crear = requests.post("http://127.0.0.1:3000", data = json.dumps(empleado))
eliminar = requests.delete("http://127.0.0.1:3000/3")
print(eliminar)