"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .Stats import Stats


class GetStats(BaseSchema):

    
    items = fields.List(fields.Nested(Stats, required=False), required=False)
    

