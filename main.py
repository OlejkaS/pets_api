from collections import OrderedDict
from datetime import datetime
from fastapi import FastAPI
from schemas import DeletePetModel, PetBaseModel, PetListWithCount


app = FastAPI(
    title='FastAPI pets'
)


fake_db = []
id = 1


@app.post('/pets')
def add_pet(pets: PetBaseModel):
    global id
    pets = OrderedDict(pets)
    pets['created_at'] = datetime.now()
    pets['id'] = id
    fake_db.append(pets)
    pets.move_to_end('id', last=False)
    id += 1
    return pets


@app.get('/pets', response_model=PetListWithCount)
def list_pets(limit: int = 20):
    return {'count': len(fake_db), 'items': fake_db}


@app.delete('/pets')
def delete_pet(ids: DeletePetModel):
    delete_count = 0
    errors = []
    for id in dict(ids)['ids']:
        found = False
        for num, pet in enumerate(fake_db):
            if id == pet['id']:
                fake_db.pop(num)
                delete_count += 1
                found = True
                break
        if not found:
            errors.append(
                {
                    'id': id,
                    'error': 'Pet with the matching ID was not found.'
                }
            )
    return {'deleted': delete_count, 'errors': errors}
