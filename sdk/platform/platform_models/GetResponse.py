"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *



from .Page import Page


class GetResponse(Schema):

    
    data = fields.Dict(required=False)
    
    page = fields.Nested(Page, required=False)
    

