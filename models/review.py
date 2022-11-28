#!/usr/bin/python3
"""Review Class Inherits from Base Model"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class"""
    place_id = ''
    user_id = ''
    text = ''
