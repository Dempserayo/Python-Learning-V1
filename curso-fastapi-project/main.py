from zoneinfo import ZoneInfo
import zoneinfo
from fastapi import FastAPI
from datetime import datetime

from models import Customer, CustomerCreate
from models import Transaction
from models import Invoice
from db import SessionDep, create_all_table  # pyright: ignore[reportMissingImports]



app = FastAPI(lifespan=create_all_table)

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
async def view_time(iso_code: str):
    iso = iso_code.upper()
    timezone_str = country_timezone.get(iso)
    tz = zoneinfo.ZoneInfo(timezone_str)
    return {"time": datetime.now(tz),}


db_customers: list[Customer] = []

@app.post("/customers", response_model= Customer)
async def create_customer(customer_data: CustomerCreate, session: SessionDep ):
    customer = Customer.model_validate(customer_data.model_dump())
    
    #Asumiendo que se hace base de datos
    customer.id = len(db_customers)
    db_customers.append(customer)
    return customer

@app.get("/customers",response_model=list[Customer])
async def list_customer():
    return db_customers


@app.post("/transaction")
async def create_transaction(transaction_data: Transaction):
    return transaction_data

@app.post("/invoice")
async def create_invoice(invoice_data: Invoice):
    return invoice_data