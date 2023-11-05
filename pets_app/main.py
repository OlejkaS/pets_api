from fastapi import FastAPI

import api.models as models
from db.database import engine
from routers.pets import router as pets_router


app = FastAPI(
    title='FastAPI pets',
)

app.include_router(
    router=pets_router,
    prefix='/pets',
    tags=['Pets']
)

models.Base.metadata.create_all(bind=engine)
