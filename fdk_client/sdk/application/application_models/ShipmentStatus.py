"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class ShipmentStatus(BaseSchema):

    
    title = fields.Str(required=False)
    
    hex_code = fields.Str(required=False)
    
