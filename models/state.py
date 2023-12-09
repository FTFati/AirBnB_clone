#!/usr/bin/python3
"""
Public class attributes that inherit from BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Represent a state.

    Attributes:
        name (str): The name of the state.
    """

    name = ""
