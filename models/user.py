#!/usr/bin/python3
"""
Public class attributes that inherit from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    class User that handles users' information
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
