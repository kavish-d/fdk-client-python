"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class GetFaqSchema(Schema):

    
    faqs = fields.List(fields.Dict(required=False), required=False)
    

