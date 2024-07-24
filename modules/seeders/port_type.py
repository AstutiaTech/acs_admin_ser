from sqlalchemy.orm import Session
from database.model import create_port_type
from modules.utils.tools import slugify

seed = [
    {
        "name": "Lights",
        "description": "",
        "file_url": "https://res.cloudinary.com/dsk9puurc/image/upload/v1720616159/bulb-lighting_bbpcm8.svg",
        "value_code": "001",
    },
    {
        "name": "Thermostat",
        "description": "",
        "file_url": "https://res.cloudinary.com/dsk9puurc/image/upload/v1720616162/thermometer_ed1b3c.svg",
        "value_code": "002",
    },
    {
        "name": "Plugs and Outlets",
        "description": "",
        "file_url": "https://res.cloudinary.com/dsk9puurc/image/upload/v1720616162/plugs-connection_yj0ihf.svg",
        "value_code": "003",
    },
    {
        "name": "Refrigerators",
        "description": "",
        "file_url": "https://res.cloudinary.com/dsk9puurc/image/upload/v1720616161/large-fridge_db4tyy.svg",
        "value_code": "004",
    },
    {
        "name": "Smart TV",
        "description": "",
        "file_url": "https://res.cloudinary.com/dsk9puurc/image/upload/v1720616162/monitor-tv_nfyl0y.svg",
        "value_code": "005",
    },
    {
        "name": "Air Purifiers",
        "description": "",
        "file_url": "https://res.cloudinary.com/dsk9puurc/image/upload/v1720616160/humidity-conditioning_aftshs.svg",
        "value_code": "006",
    },
    {
        "name": "Air Conditioner",
        "description": "",
        "file_url": "https://res.cloudinary.com/dsk9puurc/image/upload/v1720616159/air-conditioner_bqoio5.svg",
        "value_code": "007",
    },
    {
        "name": "Water Heater",
        "description": "",
        "file_url": "https://res.cloudinary.com/dsk9puurc/image/upload/v1720616159/water-heater_ybdeel.svg",
        "value_code": "008",
    },
    {
        "name": "CCTV Camera",
        "description": "",
        "file_url": "https://res.cloudinary.com/dsk9puurc/image/upload/v1720616159/cctv-camera_anu76l.svg",
        "value_code": "009",
    },
    {
        "name": "Electric Kettle",
        "description": "",
        "file_url": "https://res.cloudinary.com/dsk9puurc/image/upload/v1720616160/electric_kettle_wzdgwh.svg",
        "value_code": "010",
    },
    {
        "name": "Door Lock",
        "description": "",
        "file_url": "https://res.cloudinary.com/dsk9puurc/image/upload/v1720616160/door-lock_zcopbe.svg",
        "value_code": "011",
    },
]

def seed_port_type(db: Session):
    global seed
    if len(seed) > 0:
        for i in range(len(seed)):
            slug = slugify(input_string=seed[i]['name'], strip='_')
            create_port_type(db=db, name=seed[i]['name'], description=seed[i]['description'], slug=slug, file_url=seed[i]['file_url'], value_code=seed[i]['value_code'], status=1, created_by=1)
    return True