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
    return "Usuario no encontrado"

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
def actualizar_datos(id: int, username: str, is_active: bool):
    for ID in bdd_usuarios:
        if ID['id'] == id:
            ID['id'] = id
            ID['username'] = username
            ID['is_active'] = is_active
    return bdd_usuarios

@app.delete('/Eliminar/{id}', tags=['Eliminar usuario'])
def eliminar_usuario(id: int):
    for eliminar in bdd_usuarios:
        if eliminar['id'] == id:
            bdd_usuarios.remove(eliminar)
    return bdd_usuarios

@app.post('/Login', tags=['Login'])
def login(username: str, password: str):
    for usuario in bdd_usuarios:
        if usuario["username"] == username and usuario["password"] == password:
            return "Login exitoso"
    return "login fallido"
