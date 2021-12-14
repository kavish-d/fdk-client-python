"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class PageMeta(BaseSchema):
    # Content swagger.json

    
    key = fields.Str(required=False)
    
    value = fields.Dict(required=False)
    

