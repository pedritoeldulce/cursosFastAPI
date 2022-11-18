
from fastapi import FastAPI, status, Response, HTTPException, Request

from typing import Optional, List
from data import courses

from fastapi.responses import PlainTextResponse, JSONResponse

# importamos la clase Course (modelo)
from models.Course import Course

app = FastAPI()

# Middleware: es una funcion que funciona con cada solicitud antes de que sea procesada por cualquiera operacion
#             de ruta especìfica. Y tambien con cada respuesta antes de devolverlo

is_logged = False

@app.middleware("http")
async def check_logged(request: Request, call_next):
    
    if is_logged:
        print(f"Accessing the route: {request.url}")
        response = await call_next(request)
        return response

    return JSONResponse(status_code=401, content={"message":"Log in"})

@app.get('/courses')
def get_courses():

    return {"courses":courses}
    #return UJSONResponse()
    #return JSONResponse(content={"Courses":courses,"message":"List Course", "status":"OK"})
    #return JSONResponse(status_code=200, content={"courses":courses[0], "status":"OK"})

@app.get('/courses/{id}')
def get_course(id:int):
    
    # course es una clase razon por la cual usamos course.id
    courseFound = list(filter(lambda course: course.id == id, courses))
    
    if courseFound:
        return {"course":courseFound, "message":"Course found"}

    return {"message": "Course not found"}

# Bùsqueda content por id
@app.get('/courses/{id}/content')
def get_content(id:int):
    
    courseFound = list(filter(lambda course: course.id == id, courses))

    if courseFound:
        
        return {"content":courseFound[0].content, "message":"course Found"}
        
    return {"message":"course not found"}


@app.post('/courses')
def create_course(course: Course):

    # course: Curse: valores del nuevo curso que se va a ingresar. instancia course del tipo Course
    # del objeto instanciado se obtiene los datos de content para luego hacer la comparacion con nuestra lista
   
    new_content = course.content  # Guargamos el valor de content para luego compararlo en el filtere

    # coursesFound contiene una lista con los valores similares a new_content
    coursesFound = list(filter(lambda course: course.content == new_content, courses))

    # buscamos si el contenido del curso es similar a alguno de la lista
    for course in coursesFound:
        if course.content == new_content:
            raise HTTPException(status_code = 400, detail="Content duplicate")

    # campo name es obligatorio, debe tener valor
    if len(course.name) == 0:
        raise HTTPException(status_code=400, detail="field name required")

    if len(course.category) == 0:
        raise HTTPException(status_code=400, detail="field category required")

    courses.append(course)    
    #return {"courses": courses, "message":"course added"}
    #return PlainTextResponse(status_code=201, content="course registed")
    return JSONResponse(status_code=201, content={"message":"Course Registed", "status":"OK"})

@app.put('/courses/{id}')
def update_course(data: Course, id: int):

    # Busqueda por ID
    courseFound = list(filter(lambda course: course.id == id, courses))

    if courseFound:
            
        courseFound[0].name = data.name
        courseFound[0].content = data.content
        courseFound[0].category = data.category
        courseFound[0].status = data.status

        return {"course": courseFound, "message":"course updated"}

    return {"message":"Course Not found"}

@app.delete('/courses/{id}')
def delete_course(id:int):

    userfound = list(filter(lambda course: course.id == id, courses))
    
    if userfound:
        # Eliminimanos el valor de la lista, solo contiene 1 valor a lista
        courses.remove(userfound[0])

        return {"courses": courses, "message":"course deleted"}

    return {"message":"course not found"}

