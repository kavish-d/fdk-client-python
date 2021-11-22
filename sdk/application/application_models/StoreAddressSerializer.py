"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




















class StoreAddressSerializer(Schema):

    
    address1 = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    city = fields.Str(required=False)
    
    longitude = fields.Float(required=False)
    
    address2 = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    latitude = fields.Float(required=False)
    
    state = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    

