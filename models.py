from pydantic import BaseModel, ConfigDict

class TodoCreate(BaseModel):
    name: str
    completed: bool = False

class TodoOut(TodoCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)
    
