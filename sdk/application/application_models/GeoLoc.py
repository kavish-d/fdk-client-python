"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class GeoLoc(Schema):

    
    latitude = fields.Str(required=False)
    
    longitude = fields.Str(required=False)
    

