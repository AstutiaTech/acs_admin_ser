from sqlalchemy.orm import Session
from database.model import create_room_type
from modules.utils.tools import slugify

seed = [
    {
        "name": "Living Room",
        "asset_type_id": 1,
        "file_url": "https://res.cloudinary.com/dsk9puurc/image/upload/v1720616162/living-room_yysykz.svg",
        "value_code": "001",
    },
    {
        "name": "Conference Room",
        "asset_type_id": 2,
        "file_url": "https://res.cloudinary.com/dsk9puurc/image/upload/v1720616160/conference_f98enl.svg",
        "value_code": "002",
    },
    {
        "name": "Bedroom",
        "asset_type_id": 1,
        "file_url": "https://res.cloudinary.com/dsk9puurc/image/upload/v1720616159/bedroom_x1qpls.svg",
        "value_code": "003",
    },
    {
        "name": "Bathroom",
        "asset_type_id": 1,
        "file_url": "https://res.cloudinary.com/dsk9puurc/image/upload/v1720616159/bathroom_n206hl.svg",
        "value_code": "004",
    },
    {
        "name": "Dinning Room",
        "asset_type_id": 1,
        "file_url": "https://res.cloudinary.com/dsk9puurc/image/upload/v1720616160/dining-room_gywzgf.svg",
        "value_code": "005",
    },
]

def seed_room_type(db: Session):
    global seed
    if len(seed) > 0:
        for i in range(len(seed)):
            slug = slugify(input_string=seed[i]['name'], strip='_')
            create_room_type(db=db, asset_type_id=seed[i]['asset_type_id'], name=seed[i]['name'], description=None, slug=slug, file_url=seed[i]['file_url'], value_code=seed[i]['value_code'], status=1, created_by=1)
    return True
