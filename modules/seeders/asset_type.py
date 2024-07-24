from sqlalchemy.orm import Session
from database.model import create_asset_type
from modules.utils.tools import slugify

seed = [
    {
        "name": "Apartment",
        "description": "A residential unit that is part of one (or several) residential buildings, or a separate dwelling within a house",
    },
    {
        "name": "Workspace",
        "description": "A designated space or facility where hands-on work and practical activities, such as manufacturing, repairs, or artistic pursuits, are carried out by individuals or small groups",
    },
    {
        "name": "Warehouse",
        "description": "A facility that, along with storage racks, handling equipment and personnel and management resources",
    },
    {
        "name": "Bunker",
        "description": "A reinforced underground shelter, typically for use in wartime.",
    },
]

def seed_asset_type(db: Session):
    global seed
    if len(seed) > 0:
        for i in range(len(seed)):
            slug = slugify(input_string=seed[i]['name'], strip='_')
            create_asset_type(db=db, name=seed[i]['name'], description=seed[i]['description'], slug=slug, status=1, created_by=1)
    return True