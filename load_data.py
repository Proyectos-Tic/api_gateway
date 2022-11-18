import requests

security_backend = "http://localhost:8080"
headers = {"Content-Type":"application/json; charset=utf-8"}

# Create roles
roles = [
    { "name": "Administrador", "description": "Administrador del sistema de notas"},
    { "name": "Profesor", "description": "El que jode"},
    { "name": "Student", "description":"El que sufre"}
]

url = f'{security_backend}/rol/create'
admin = None
for rol in roles:
    response = requests.post(url, headers=headers, json=rol)
    if rol.get('name') == "Administrador":
        admin = response.json()
    print(response.json())
print("="*30)

# Basic permission related to Admin
modules = ['student', 'course', 'department', 'enrollment', 'user', 'rol']
endpoints = [('s', 'GET'), ('/?', 'GET'), ('/create', 'POST'), ('/update/?','PUT'), ('/delete/?', 'DELETE')]
url = f'{security_backend}/permission/create'
for module in modules:
    for endpoint, method in endpoints:
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