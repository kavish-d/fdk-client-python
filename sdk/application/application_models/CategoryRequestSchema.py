"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class CategoryRequestSchema(BaseSchema):

    
    slug = fields.Str(required=False)
    
    title = fields.Str(required=False)
    

