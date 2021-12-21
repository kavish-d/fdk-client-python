"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .GetSearchWordsData import GetSearchWordsData

from .Page import Page


class GetSearchWordsDetailResponse(BaseSchema):
    # Catalog swagger.json

    
    items = fields.Nested(GetSearchWordsData, required=False)
    
    page = fields.Nested(Page, required=False)
    

