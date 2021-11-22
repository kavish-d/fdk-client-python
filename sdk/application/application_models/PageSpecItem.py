"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *





from .PageSpecParam import PageSpecParam

from .PageSpecParam import PageSpecParam


class PageSpecItem(Schema):

    
    page_type = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    params = fields.List(fields.Nested(PageSpecParam, required=False), required=False)
    
    query = fields.List(fields.Nested(PageSpecParam, required=False), required=False)
    

