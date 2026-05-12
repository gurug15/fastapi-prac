from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from app.repositories.db import get_db
from app.repositories.schemas.todo_db_schema import TodoSchema
from app.schemas.schema import Todo

router = APIRouter(prefix="/todo")

@router.get("/")
def getTodos(db: Session = Depends(get_db)):
    todos = db.query(TodoSchema).all()
    return todos

@router.post("/addtodo", status_code=status.HTTP_201_CREATED)
def addTodo(todo: Todo, db: Session = Depends(get_db)):
    try:
        new_todo = TodoSchema(content=todo.content)
        db.add(new_todo)
        db.commit()
        db.refresh(new_todo)
        return {
            "success": True,
            "data": new_todo
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to create Todo"
        )