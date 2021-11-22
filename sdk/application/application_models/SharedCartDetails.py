"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *












class SharedCartDetails(Schema):

    
    source = fields.Dict(required=False)
    
    user = fields.Dict(required=False)
    
    created_on = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    token = fields.Str(required=False)
    

