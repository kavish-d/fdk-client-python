"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class GeoLocation(Schema):

    
    longitude = fields.Float(required=False)
    
    latitude = fields.Float(required=False)
    

