"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema




class GetFaqSchema(BaseSchema):

    
    faqs = fields.List(fields.Dict(required=False), required=False)
    

