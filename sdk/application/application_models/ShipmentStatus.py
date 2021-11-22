"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class ShipmentStatus(Schema):

    
    title = fields.Str(required=False)
    
    hex_code = fields.Str(required=False)
    

