"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class CartProductIdentifer(Schema):

    
    identifier = fields.Str(required=False)
    

