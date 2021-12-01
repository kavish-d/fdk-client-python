"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class ContentSchema(BaseSchema):

    
    type = fields.Str(required=False)
    
    value = fields.Dict(required=False)
    

