"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class LatLong(BaseSchema):

    
    coordinates = fields.List(fields.Float(required=False), required=False)
    
    type = fields.Str(required=False)
    

