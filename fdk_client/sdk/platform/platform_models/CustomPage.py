"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .CustomPageSchema import CustomPageSchema


class CustomPage(BaseSchema):

    
    data = fields.Nested(CustomPageSchema, required=False)
    

