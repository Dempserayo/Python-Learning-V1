from pydantic import BaseModel, EmailStr
from sqlmodel import SQLModel

class CustomerBase(SQLModel):
    name: str
    description: str | None
    email: EmailStr
    age: int

class CustomerCreate(CustomerBase):
    pass 
    
class Customer(SQLModel, table = True):
    id: int | None = None


class Transaction(BaseModel):
    id: int
    ammount: int
    description: str

class Invoice(BaseModel):
    id: int
    customer: Customer
    transactions: list[Transaction]
    total: int

    @property
    def ammount_total(self):
        return sum(transaction.amount for transaction in self.transactions)
