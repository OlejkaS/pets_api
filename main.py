from database import engine, SessionLocal
from fastapi import FastAPI, Depends
import models
from schemas import DeletePetModel, PetBaseModel, PetListWithCount

from sqlalchemy.orm import Session


app = FastAPI(
    title='FastAPI pets'
)

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.post('/pets')
def add_pet(pets: PetBaseModel, db: Session = Depends(get_db)):
    pet_obj = models.Pet(name=pets.name, age=pets.age, type=pets.type)
    db.add(pet_obj)
    db.commit()
    db.refresh(pet_obj)
    return pet_obj


@app.get('/pets', response_model=PetListWithCount)
def list_pets(limit: int = 20, db: Session = Depends(get_db)):
    queryset = db.query(models.Pet).all()[:limit]
    return {'count': len(queryset), 'items': queryset}


@app.delete('/pets')
def delete_pet(ids: DeletePetModel, db: Session = Depends(get_db)):
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
