"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class Store(Schema):

    
    id = fields.Int(required=False)
    

