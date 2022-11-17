from pydantic import BaseModel

class Content(BaseModel):
    title: str
    description: str
    url: str
    module: int
    chapter: int