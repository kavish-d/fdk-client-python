"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *



from .PageNumber import PageNumber


class NumberGetResponse(Schema):

    
    items = fields.List(fields.Dict(required=False), required=False)
    
    page = fields.Nested(PageNumber, required=False)
    

