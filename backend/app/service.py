from fastapi import HTTPException, status
from app.repository import get_tasks as repo_get_tasks, get_task_by_id as repo_get_task_by_id, create_task as repo_create_task, update_task_completion as repo_update_task_completion
from app.schemas import TaskCreate

async def get_tasks(db, skip: int = 0, limit: int = 10):
    tasks = await repo_get_tasks(db, skip, limit)
    if not tasks:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No tasks found"
        )
    return tasks

async def get_task_by_id(db, task_id: int):
    task = await repo_get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )
    return task

async def create_task(db, task: TaskCreate):
    db_task = await repo_create_task(db, task.title, task.description)    
    return db_task

async def update_task_completion(db, task_id: int, completed: bool):
    task = await repo_update_task_completion(db, task_id, completed)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )
    return task