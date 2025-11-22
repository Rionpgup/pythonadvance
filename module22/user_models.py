from pydantic import BaseModel
from typing import Optional
#
# class User(BaseModel):
#     id: int
#     name: str
#     age: int
#     email: str
#
# #validation
#
# user = User(id=1, name="John Doe", age=30, email="jon.doe@gmail.com")

#default values and optional fields
class User(BaseModel):
    id: int
    name: str
    age: Optional[int] = None
    email : Optional[str] = None

user1 = User(id=1, name="John Doe", age=30, email="jon.doe@gmail.com")
print(user1)
user2 = User(id=2, name="Jane", age=None, email="jane@gmail.com")
print(user2)
user3 = User(id=3, name="Charlie", age=30)
print(user3)
user4 = User(id=4, name="John")
print(user4)
#field constraints
class another_user(BaseMOdel):
    id: conint(gt=0)
    name: constr(nin_length=2, max_length=50)

    valid_user = another_user(id=1, name="ALice")
    print(valid_user)