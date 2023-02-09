#!/usr/bin/env python3
"""city Module"""
from models.base_model import BaseModel


class City(BaseModel):
    """This class Initializes city instances"""
    state_id: str = ""
    name: str = ""
