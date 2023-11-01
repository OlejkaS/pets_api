from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

import api.models as models
from api.schemas import (
    DeletePetModel,
    DeleteResponseModel,
    PetBaseModel,
    PetList,
    PetListWithCount,
)
from db.database import engine, get_db


app = FastAPI(
    title='FastAPI pets'
)

models.Base.metadata.create_all(bind=engine)


@app.post('/pets', response_model=PetList)
def add_pet(pets: PetBaseModel, db: Session = Depends(get_db)) -> PetList:
    pet_obj = models.Pet(name=pets.name, age=pets.age, type=pets.type)
    db.add(pet_obj)
    db.commit()
    db.refresh(pet_obj)
    return pet_obj


@app.get('/pets', response_model=PetListWithCount)
def list_pets(
    limit: int = 20,
    db: Session = Depends(get_db)
) -> PetListWithCount:
    queryset = db.query(models.Pet).all()[:limit]
    return {'count': len(queryset), 'items': queryset}


@app.delete('/pets', response_model=DeleteResponseModel)
def delete_pet(
    ids: DeletePetModel,
    db: Session = Depends(get_db)
) -> DeleteResponseModel:
    errors = []
    delete_count = 0
    for id in dict(ids)['ids']:
        found = False
        queryset = db.query(models.Pet).filter(models.Pet.id == id).first()
        if queryset:
            db.delete(queryset)
            delete_count += 1
            found = True
        if not found:
            errors.append(
                {
                    'id': id,
                    'error': 'Pet with the matching ID was not found.'
                }
            )
    db.commit()
    return {'deleted': delete_count, 'errors': errors}
