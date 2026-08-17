from pydantic import BaseModel, Field
from typing import Optional

class Person(BaseModel):
    name: str = Field(description="The name of the person")
    age: int
    city: str
    email: Optional[str] = Field(None, description="The email address of the person")