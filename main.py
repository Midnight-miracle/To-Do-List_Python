from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import database_models
from database import SessionLocal, engine
from database_models import Todo
from models import TodoCreate, TodoOut

app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)


def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/todos", response_model=list[TodoOut])
def get_all_todos(db: Session = Depends(get_session)):
    return db.query(Todo).all()


@app.get("/todos/{id}", response_model=TodoOut)
def get_todo(id: int, db: Session = Depends(get_session)):
    todo = db.get(Todo, id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@app.post("/todos", response_model=TodoOut, status_code=201)
def add_todo(data: TodoCreate, db: Session = Depends(get_session)):
    todo = Todo(**data.model_dump())
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


@app.put("/todos/{id}", response_model=TodoOut)
def update_todo(id: int, data: TodoCreate, db: Session = Depends(get_session)):
    todo = db.get(Todo, id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    for field, value in data.model_dump().items():
        setattr(todo, field, value)
    db.commit()
    db.refresh(todo)
    return todo


@app.delete("/todos/{id}")
def delete_todo(id: int, db: Session = Depends(get_session)):
    todo = db.get(Todo, id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
    return {"message": "Todo deleted"}