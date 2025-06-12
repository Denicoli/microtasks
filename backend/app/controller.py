from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app import schemas, database, service

router = APIRouter()

@router.post("/tasks/", response_model=schemas.Task)
async def create_task(task: schemas.TaskCreate, db: AsyncSession = Depends(database.get_db)):
    return await service.create_task(db, task)

@router.get("/tasks/", response_model=list[schemas.Task])
async def get_tasks(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(database.get_db)):
    return  await service.get_tasks(db, skip, limit)

@router.patch("/tasks/{task_id}/complete", response_model=schemas.Task)
async def update_task_completion(task_id: int, completed: bool, db: AsyncSession = Depends(database.get_db)):
    return await service.update_task_completion(db, task_id, completed)
