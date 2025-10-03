from fastapi import FastAPI, Body
from data import Userlogin

app = FastAPI()

bdd_usuarios = [
    {
        "id": 1,
        "username": "Erick",
        "password": "123",
        "is_active": True
    },
    {
        "id": 2,
        "username": "Cris",
        "password": "chao123",
        "is_active": True
    }
]

@app.get('/Usuarios', tags=['Lista de usuarios'])
def mostrar_lista():
    return bdd_usuarios

@app.get('/Usuario_ID/{id}', tags=['Busqueda por ID'])
def mostrar_usuario_id(id: int):
    for usuario in bdd_usuarios:
        if usuario["id"] == id:
            return usuario
    return "Usuario no valido"

@app.post('/Crear', tags=['Creacion de usuarios'])
def crear_usuario(data: Userlogin):
    bdd_usuarios.append({
        'id': data.id,
        'username': data.username,
        'password': data.password,
        'is_active': data.is_active
    })
    return bdd_usuarios

@app.put('/Actualizar/{id}', tags=['Actualizacion de datos'])
def actualizar_datos(id: int, data:Userlogin):
    for actualizar in bdd_usuarios:
        if actualizar['id'] == data.id:
            actualizar['username'] = data.username
            actualizar['password'] = data.password
            actualizar['is_active'] = data.is_active
            return actualizar
    return bdd_usuarios

@app.delete('/Eliminar/{id}', tags=['Eliminar usuario'])
def eliminar_usuario(id: int):
    for eliminar in bdd_usuarios:
        if eliminar['id'] == id:
            bdd_usuarios.remove(eliminar)
    return bdd_usuarios

@app.post('/Login', tags=['Login'])
def login(data: Userlogin):
    for usuario in bdd_usuarios:
        if usuario["username"] == data.username and usuario["password"] == data.password:
            return "Login exitoso"
    return "login fallido"