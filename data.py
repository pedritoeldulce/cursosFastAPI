courses = []


""" courses = [
    {
        "id": 1,
        "name":"GIT DESDE CERO",
        "content": [
            {
                "title": "Bitacora del Capitan",
                "description": "Introducciòn a Git",
                "url": "https://drive.google.com/file/d/1QNe2yWhtHHWT3ppiY7sTRHcUEo8XTmDr/view?usp=share_link",
                "module":1,
                "chapter":1

            }
        ],
        "category": "Programaciòn",
        "status": "OK"

    },
    {
        "id": 2,
        "name":"GIT DESDE CERO",
        "content": [
            {
                "title": "Introducciòn a Git",
                "description": "que es Git - versiones",
                "url": "https://drive.google.com/file/d/1nsB72MmokEGFZZ7rmFGWTCef8lvtOIBp/view?usp=share_link",
                "module":1,
                "chapter":2

            }
        ],
        "category": "Programaciòn",
        "status": "OK"

    },
    {
        "id": 3,
        "name":"GIT DESDE CERO",
        "content": [
            {
                "title": "instalaciòn de Git",
                "description": "instalar GIT en diferentes sistemas operativos",
                "url": "https://drive.google.com/file/d/19BMdlAE4u4RWYy4RaIqyYC6uQo4LKnIU/view?usp=share_link",
                "module":1,
                "chapter":3

            }
        ],
        "category": "Programaciòn",
        "status": "OK"

    },
]
 """


# Otros datos

""" @app.post('/courses')
def create_course(id:int , content:List[dict] , tag:List[dict], category:str, status:str):
    
    new_curso = {
        "id":id,
        "content":content,
        "tag":tag,
        "category": category,
        "status": status
    }

    courses.append(new_curso)
    return {"courses": courses, "message":"course added"}
 """

# Ejemplos GET
""" @app.get('/')
def home():
    return {"message":"HOla NOa"}


@app.get('/users')
def get_users():

    return {"Users":users} 

@app.get('/user/{id_user}')
def get_user(id_user:int):

    userfound = list(filter(lambda u: u["id"] == id_user, users))

    if userfound:
        return {"message":"Usuario encontrado", "user": userfound}

    return {"message":"Usuario no encontrado"}


# mandar 2 ò màs parametros
@app.get('/user/{id}/nombre/{nombre}')
def getUser(id:int, nombre:str):

    userFound =  list(filter(lambda user:user['id'] == id and user['nombre'] == nombre, users))

    if userFound:
        return {"message":"Usuario encontrado:", "user":userFound}

    return {"message":"usuario no encontrado"} 

@app.get('/userquery/{id}')
def getQuery(id: int, nombre:str, age:int=None):


    if age:

        userFound = list(filter(lambda user: user['id']== id and user['nombre']== nombre and 
                user['age']==age, users))

        if userFound:
            return {"message":"Usuario encontrado sin age", "user":userFound}

        return {"message":"Usuario no encontrado"}

    else:

        userFound = list(filter(lambda user: user['id']== id and user['nombre']== nombre, users))

        if userFound:
            return{"user":userFound}
        return {"message":"Usuario no encontradp XD"}
    


@app.get('/welcome/{name}/{lastname}')
def welcome(name:int, lastname:int):
    return {"message":f"Bienvenido {name.upper()} - {lastname}"}

#Otra forma de correr el archivo


@app.get('/suma/{a}/{b}')
def suma(a:float, b:float, response: Response):
    
    if a+b>0:
        response.status_code = status.HTTP_200_OK
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST

    return {"message":f"{a+b}"} """

"""
if __name__== '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=3000) """

