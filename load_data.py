import requests

security_backend = "http://localhost:8080"
headers = {"Content-Type":"application/json; charset=utf-8"}

# Create roles
roles = [
    { "name": "Administrador", "description": "Administrador del sistema de votación"},
    { "name": "Jurado", "description": "Persona natural con algunos permisos en el sistema de votación"},
    { "name": "Ciudadano", "description":"Persona natural"}
]

url = f'{security_backend}/rol/create'
admin = None
for rol in roles:
    response = requests.post(url, headers=headers, json=rol)
    if rol.get('name') == "Administrador":
        admin = response.json()
    print(response.json())
print("="*30)

# TODO: Create particular endpoints to match permission/rol [user, reports]
# Basic permission related to Admin
modules = ['candidato', 'mesa', 'partido', 'reports' , 'enrollment', 'user', 'rol']
endpoints_ag = [('/all', 'GET'), ('/?', 'GET'), ('/create', 'POST'), ('/update/?','PUT'), ('/delete/?', 'DELETE')]
url = f'{security_backend}/permission/create'
for module in modules:
    for endpoint, method in endpoints_ag:
        permission_url = f'/{module}{endpoint}'
        body = {
            "url": permission_url,
            "method": method
        }
        response = requests.post(url, headers=headers, json=body)
        print(response.json())
        permission = response.json()
        url_relation = f'{security_backend}/rol/update/{admin.get("idRol")}/add_permission/{permission.get("idPermission")}'
        response = requests.put(url_relation, headers=headers)