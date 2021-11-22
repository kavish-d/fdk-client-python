"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *



from .Meta import Meta




class Media(Schema):

    
    type = fields.Str(required=False)
    
    meta = fields.Nested(Meta, required=False)
    
    url = fields.Str(required=False)
    

