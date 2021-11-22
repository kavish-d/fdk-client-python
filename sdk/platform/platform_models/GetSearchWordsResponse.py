"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .Page import Page

from .GetSearchWordsData import GetSearchWordsData


class GetSearchWordsResponse(Schema):

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(GetSearchWordsData, required=False), required=False)
    

