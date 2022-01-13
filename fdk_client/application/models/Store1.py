"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .LatLong import LatLong




















class Store1(BaseSchema):
    # Catalog swagger.json

    
    lat_long = fields.Nested(LatLong, required=False)
    
    store_code = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    city = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    country = fields.Str(required=False)
    
    store_email = fields.Str(required=False)
    

