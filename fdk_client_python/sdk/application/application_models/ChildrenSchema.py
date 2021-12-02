"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema












class ChildrenSchema(BaseSchema):

    
    question = fields.Str(required=False)
    
    answer = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    

