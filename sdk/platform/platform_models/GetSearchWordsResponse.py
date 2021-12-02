"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .GetSearchWordsData import GetSearchWordsData

from .Page import Page


class GetSearchWordsResponse(BaseSchema):

    
    items = fields.List(fields.Nested(GetSearchWordsData, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

