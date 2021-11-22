"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .CustomPageSchema import CustomPageSchema


class CustomPage(Schema):

    
    data = fields.Nested(CustomPageSchema, required=False)
    

