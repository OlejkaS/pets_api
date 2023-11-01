from datetime import datetime
from fastapi import FastAPI
from schemas import DeletePetModel, PetBaseModel, PetListWithCount


app = FastAPI(
    title='FastAPI pets'
)


fake_pets = []


@app.post('/pets')
def add_pet(pets: PetBaseModel):
    pets = dict(pets)
    pets['created_at'] = datetime.now()
    fake_pets.append(pets)
    return pets


@app.get('/pets', response_model=PetListWithCount)
def list_pets(limit: int = 20):
    return {'count': len(fake_pets), 'items': fake_pets[:limit]}


@app.delete('/pets')
def delete_pet(ids: DeletePetModel):
    delete_count = 0
    errors = []
    found = False
    for id in dict(ids)['ids']:
        if not fake_pets:
            errors.append(
                    {
                        'id': id,
                        'error': 'Pet with the matching ID was not found.'
                    }
                )
            continue
        for num, pet in enumerate(fake_pets):
            if id == pet['id']:
                fake_pets.pop(num)
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
            break
    return {'deleted': delete_count, 'errors': errors}
