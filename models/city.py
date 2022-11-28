#!/usr/bin/python3
"""City Class Inherits from Base Model"""

from models.base_model import BaseModel


class City(BaseModel):
    """City Class"""
    state_id = ''
    name = ''
