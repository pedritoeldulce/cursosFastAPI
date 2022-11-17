
from fastapi import FastAPI, status, Response
#import uvicorn
from typing import Optional, List
from data import courses

# importamos la clase Course (modelo)
from models.Course import Course

app = FastAPI()

@app.get('/courses')
def get_courses():
    return {"courses":courses}

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
        # return {"content":courseFound[0]['tag'][0]['name'], "message":"course found"}
        return {"content":courseFound[0].content, "message":"course Found"}

    return {"message":"course not found"}


@app.post('/courses')
def create_course(course: Course):
    courses.append(course)
    return {"courses": courses, "message":"course added"}


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
    userfound = list(filter(lambda course: course[0]["id"] == id, courses))
    print(userfound)
    if userfound:
        return {"courses": courses, "message":"course deleted"}

    return {"message":"course not found"}

