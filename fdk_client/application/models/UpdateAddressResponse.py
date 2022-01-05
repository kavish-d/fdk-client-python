"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class UpdateAddressResponse(BaseSchema):
    # Cart swagger.json

    
    success = fields.Boolean(required=False)
    
    is_default_address = fields.Boolean(required=False)
    
    is_updated = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    

