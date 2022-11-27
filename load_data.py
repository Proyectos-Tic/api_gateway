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

# TODO: Create particular endpoints to match permission/rol [user, reports, candidate]
# Basic permission related to Admin
modules = ['candidato', 'mesa', 'partido', 'voto', 'reports' , 'permission', 'user', 'rol']
crud_endpoints = [('/all', 'GET'), ('/?', 'GET'), ('/create', 'POST'), ('/update/?','PUT'), ('/delete/?', 'DELETE')]
candidatos_endpoint = [('/?/partido/?', 'PUT')]
user_endpoints = [('/by_id/?', 'GET'), ('/by_nickname/?', 'GET'), ('/by_email/?', 'GET')]
reports_endpoints = [('/voto/sorted_candidato', 'GET'), ('/voto/sorted_candidato/?', 'GET'), ('/voto/sorted_mesa', 'GET'), ('/voto/sorted_partido', 'GET'),
                    ('/voto/sorted_partido/?', 'GET'), ('/voto/partido/porcentual', 'GET')]
url = f'{security_backend}/permission/create'
for module in modules:
    temp_endpoints = None
    if module == 'candidato':
        temp_endpoints = crud_endpoints + candidatos_endpoint
    elif module == 'user':
        temp_endpoints = crud_endpoints + user_endpoints
    elif module == 'reports':
        temp_endpoints = reports_endpoints
    else:
        temp_endpoints = crud_endpoints

    for endpoint, method in temp_endpoints:
        if(module=='voto' and endpoint=='/create'):
            endpoint= '/create/mesa/?/candidato/?'
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