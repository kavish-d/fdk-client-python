"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *










class UpdateAddressResponse(Schema):

    
    is_default_address = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    
    is_updated = fields.Boolean(required=False)
    
    success = fields.Boolean(required=False)
    

