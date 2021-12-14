"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .CustomPageSchema import CustomPageSchema


class CustomPage(BaseSchema):
    # Content swagger.json

    
    data = fields.Nested(CustomPageSchema, required=False)
    

