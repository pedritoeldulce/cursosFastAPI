from fastapi import FastAPI, status, Response
#import uvicorn
from typing import Optional, List
from data import courses
from models.Course import Course

app = FastAPI()

@app.get('/courses')
def get_courses():
    return {"courses":courses}

@app.get('/courses/{id}')
def get_course(id: int):
    
    #my_course = Course()
    print(courses[id])
    return "my_course"
    """ courseFound = list(filter(lambda course: course['id'] == id, courses))
    print(courseFound)
    if courseFound:
        return {"course":courseFound, "message":"Course found"}

    return {"message": "Course not found"} """

# Bùsqueda por tag
@app.get('/courses/{id}/tag')
def get_tag(id:int):

    courseFound = list(filter(lambda course: course['id'] == id, courses))
    if courseFound:
        return {"name":courseFound[0]['tag'][0]['name'], "message":"course found"}

    return {"message":"course not found"}


@app.post('/courses')
def create_course(course: Course):
    courses.append(course)
    return {"courses": courses, "message":"course added"}


@app.delete('/courses/{id}')
def delete_course(id:int):
    userfound = list(filter(lambda course: course[0]["id"] == id, courses))
    print(userfound)
    if userfound:
        return {"courses": courses, "message":"course deleted"}

    return {"message":"course not found"}

# Corregir el error 'Course' object is not subscriptable


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

