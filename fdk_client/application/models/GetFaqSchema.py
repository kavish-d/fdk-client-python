"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class GetFaqSchema(BaseSchema):
    # Content swagger.json

    
    faqs = fields.List(fields.Dict(required=False), required=False)
    

