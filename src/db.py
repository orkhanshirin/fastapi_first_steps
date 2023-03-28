from typing import List
from models import User, Role, Gender
from uuid import uuid4

db: List[User] = [
    User(
        id=uuid4(),
        first_name="orkhan",
        last_name="shirin",
        email="orkhan@blackswan-technologies.com",
        gender=Gender.male,
        roles=[Role.admin],
    ),
    User(
        id=uuid4(),
        first_name="pepiniho",
        last_name="frog",
        email="test@test.com",
        gender=Gender.none,
        roles=[Role.admin, Role.user],
    ),
]
