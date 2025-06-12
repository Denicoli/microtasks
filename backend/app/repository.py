from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import Task
from app.schemas import TaskCreate

async def get_tasks(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Task).order_by(Task.id.desc()).offset(skip).limit(limit))
    return result.scalars().all()

async def get_task_by_id(db: AsyncSession, task_id: int):
    task = await db.execute(select(Task).where(Task.id == task_id))
    return task.scalar_one_or_none()

async def create_task(db: AsyncSession, task: TaskCreate):
    db_task = Task(title=task.title, description=task.description)
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    return db_task

async def update_task_completion(db: AsyncSession, task_id: int, completed: bool):
    result = await db.execute(select(Task).where(Task.id == task_id))
    task = result.scalar_one_or_none()
    
    if task is None:
        return None
    
    task.completed = completed
    await db.commit()
    await db.refresh(task)
    return task