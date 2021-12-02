"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .Media import Media










class Department(BaseSchema):

    
    logo = fields.Nested(Media, required=False)
    
    slug = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    priority_order = fields.Int(required=False)
    
    name = fields.Str(required=False)
    

