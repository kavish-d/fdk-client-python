"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class Identifiers(Schema):

    
    ean = fields.Str(required=False)
    
    sku_code = fields.Str(required=False)
    

