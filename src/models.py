from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional, List
from enum import Enum


class Gender(str, Enum):
    male = "male"
    female = "female"
    none = "none"


class Role(str, Enum):
    admin = "admin"
    user = "user"
    test = "test"


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str]
    email: str
    gender: Gender
    roles: List[Role]


class UpdatedUser(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    email: Optional[str]
    gender: Optional[Gender]
    roles: Optional[List[Role]]
