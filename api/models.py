import re
from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, validator
import uuid

#########################
# BLOCK WITH API MODELS #
#########################


LETTER_MATCH_PATTERN = re.compile(r'^[я-яА-Яа-zA-Z\-]+$')


class TunedModel(BaseModel):
    """Tell pydantic to convert even non dict obj to json"""
    class Config:

        orm_mode = True


class UserCreate(BaseModel):
    name: str
    surname: str
    email: EmailStr

    @validator('name')
    def validate_name(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=422, detail="Name should contains only letters"
            )
        return value

    @validator('surname')
    def validate(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=422, detail="Surname should contains only letters"
            )
        return value


class ShowUser(TunedModel):
    user_id: uuid.UUID
    name: str
    surname: str
    email: EmailStr
    is_active: bool
