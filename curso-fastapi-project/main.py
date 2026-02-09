from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


#Decorador @app 
@app.get("/")
async def root():
    return {"message":"hola mundo"}


@app.get("/test")
async def hora():
    hora = datetime.now()
    return {"Hora: ": hora}