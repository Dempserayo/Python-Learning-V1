from pydantic import BaseModel, EmailStr
from sqlmodel import SQLModel, Field  # pyright: ignore[reportMissingImports]

class CustomerBase(SQLModel):
    name: str = Field(default = None)
    description: str | None = Field(default = None)
    email: EmailStr = Field(default = None) 
    age: int = Field(default = None)

class CustomerCreate(CustomerBase):
    pass 
    
class Customer(SQLModel, table = True):
    id: int | None = Field(default = None, primary_key=True)


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
