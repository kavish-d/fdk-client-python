"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class ValidateProduct(Schema):

    
    valid = fields.Boolean(required=False)
    

