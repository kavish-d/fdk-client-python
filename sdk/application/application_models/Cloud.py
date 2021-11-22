"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *








class Cloud(Schema):

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    provider = fields.Str(required=False)
    

