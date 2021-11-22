"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *












class ReviewFacet(Schema):

    
    display = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    selected = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    type = fields.Str(required=False)
    

