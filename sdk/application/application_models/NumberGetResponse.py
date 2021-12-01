"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema



from .PageNumber import PageNumber


class NumberGetResponse(BaseSchema):

    
    items = fields.List(fields.Dict(required=False), required=False)
    
    page = fields.Nested(PageNumber, required=False)
    

