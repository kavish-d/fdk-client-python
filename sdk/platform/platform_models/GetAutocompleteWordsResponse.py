"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .Page import Page

from .GetAutocompleteWordsData import GetAutocompleteWordsData


class GetAutocompleteWordsResponse(Schema):

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(GetAutocompleteWordsData, required=False), required=False)
    

