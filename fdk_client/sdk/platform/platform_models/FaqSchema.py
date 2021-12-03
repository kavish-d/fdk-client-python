"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema












class FaqSchema(BaseSchema):

    
    slug = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    question = fields.Str(required=False)
    
    answer = fields.Str(required=False)
    
