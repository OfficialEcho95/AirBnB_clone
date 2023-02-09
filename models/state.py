#!/usr/bin/env python3
"""State Module"""
from models.base_model import BaseModel


class State(BaseModel):
    """This class Initializes state instances"""
    name: str = ""
