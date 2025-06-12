from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from . import crud, database, schemas

app = FastAPI()

@app.post("/tasks/", response_model=schemas.Task)
async def create_task(task: schemas.TaskCreate, db: AsyncSession = Depends(database.get_db)):
    return await crud.create_task(db=db, task=task)

@app.get("/tasks/", response_model=list[schemas.Task])
async def get_tasks(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(database.get_db)):
    return  await crud.get_tasks(db=db, skip=skip, limit=limit)

@app.patch("/tasks/{task_id}/complete", response_model=schemas.Task)
async def update_task_completion(task_id: int, completed: bool, db: AsyncSession = Depends(database.get_db)):
    return await crud.update_task_completion(db=db, task_id=task_id, completed=completed)