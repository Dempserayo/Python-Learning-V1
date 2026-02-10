from fastapi import FastAPI, HTTPException
from datetime import datetime
from zoneinfo import ZoneInfo

app = FastAPI()

country_timezone = {
    "CO": "America/Bogota",
    "MX": "America/Mexico_City",
    "AR": "America/Argentina/Buenos_Aires",
    "BR": "America/Sao_Paulo",
    "PE": "America/Lima",
}

@app.get("/")
async def root():
    return("Hola mundo")

@app.get("/time/{iso_code}")
async def time(iso_code: str):
    iso = iso_code.upper()
    timezone_str = country_timezone.get(iso)

    if not timezone_str:
        raise HTTPException(
            status_code=404,
            detail="Código de país no soportado"
        )

    tz = ZoneInfo(timezone_str)
    return { "country": iso, "timezone": timezone_str, "time": datetime.now(tz).isoformat()}
