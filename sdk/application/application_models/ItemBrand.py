"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class ItemBrand(Schema):

    
    name = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    

