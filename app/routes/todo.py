


from fastapi import APIRouter, HTTPException,status

from app.consts.todos import allTodos as todos
from app.schemas.schema import Todo


router = APIRouter(
    prefix="/todo"
)

@router.get("/")
def getTodos():
    return todos



@router.post("/addtodo",status_code=status.HTTP_201_CREATED)
def addTodo(todo:Todo):
    try:
        todos.append(todo)
        return {
            "success":True,
            "data":todo
        }
    except Exception:
        raise HTTPException(
            status_code=401,
            detail="faild to create Todo"
        )