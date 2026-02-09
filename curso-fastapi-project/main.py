from fastapi import FastAPI

app = FastAPI()


#Decorador @app 
@app.get("/")
async def root():
    return {"message":"hola mundo"}
