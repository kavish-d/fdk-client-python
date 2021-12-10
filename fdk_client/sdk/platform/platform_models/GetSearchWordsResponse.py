"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .Page import Page

from .GetSearchWordsData import GetSearchWordsData


class GetSearchWordsResponse(BaseSchema):

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(GetSearchWordsData, required=False), required=False)
    

