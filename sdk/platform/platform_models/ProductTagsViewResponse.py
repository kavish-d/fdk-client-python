"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .NestedTags import NestedTags


class ProductTagsViewResponse(BaseSchema):

    
    items = fields.Nested(NestedTags, required=False)
    

