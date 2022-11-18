
from fastapi import FastAPI, status, Response, HTTPException
#import uvicorn
from typing import Optional, List
from data import courses

from fastapi.responses import PlainTextResponse, JSONResponse


# importamos la clase Course (modelo)
from models.Course import Course

app = FastAPI()

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

    print(courseFound)
    if courseFound:
        
        return {"content":courseFound[0].content, "message":"course Found"}
        

    return {"message":"course not found"}


@app.post('/courses')
def create_course(course: Course):

    # id nuevo a ingresar
    n_id=course.id

    # compara con las lista de ID de la lista courses
    courseFound = list(filter(lambda course: course.id == n_id, courses))

    if courseFound is not None:
        raise HTTPException(status_code=400, detail="Duplicate id")

    if len(course.name) == 0:
        raise HTTPException(status_code=400, detail="field name required")

    
    
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

