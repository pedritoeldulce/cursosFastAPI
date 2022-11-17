from pydantic import BaseModel
from typing import List

from models.Content import Content

class Course(BaseModel):
    id: int
    name: str
    content: List[Content]
    category: str
    status: str

