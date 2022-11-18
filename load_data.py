import requests

security_backend = "http://localhost:8080"
headers = {"Content-Type": "application/json; charset=utf-8"}

# CREATE ROLES
roles = [
    {"name": "Administrador", "description": "Accede a todo."},
    {"name": "Jurado", "description": "Administra resultados y ve reportes."},
    {"name": "Ciudadano", "description": "Ve solo los reportes."}
]
url = f'{security_backend}/rol/insert'
admin = None
for rol in roles:
    response = requests.post(url, headers=headers, json=rol)
    if rol.get('name') == 'Administrador':
        admin = response.json()
    print(response.json)


# PERMISSIONS RELATED TO ADMIN
modules = ['party', 'table', 'candidate', 'result']


