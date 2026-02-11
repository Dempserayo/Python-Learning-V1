from pydantic import BaseModel, EmailStr

class Customer(BaseModel):
    id: int
    name: str
    description: str | None
    email: EmailStr
    age: int

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
