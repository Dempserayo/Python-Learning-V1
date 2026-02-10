from zoneinfo import ZoneInfo
import zoneinfo
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

country_timezone = {
    'CO': 'America/Bogota',
    'MX': 'America/Mexico_City',
    'AR': 'America/Argentina/Buenos_Aires',
    'BR': 'America/Sao_Paulo',
    'PE': 'America/Lima',
}

@app.get("/")
async def root():
    return("Hola mundo")

@app.get("/time/{iso_code}")
async def time(iso_code: str):
    iso = iso_code.upper()
    timezone_str = country_timezone.get(iso)
    tz = zoneinfo.ZoneInfo(timezone_str)
    return {"time": datetime.now(tz),}