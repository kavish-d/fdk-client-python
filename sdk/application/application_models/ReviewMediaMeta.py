"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *








class ReviewMediaMeta(Schema):

    
    max_count = fields.Float(required=False)
    
    size = fields.Float(required=False)
    
    type = fields.Str(required=False)
    

