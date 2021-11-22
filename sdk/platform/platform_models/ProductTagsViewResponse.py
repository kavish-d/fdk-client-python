"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .NestedTags import NestedTags


class ProductTagsViewResponse(Schema):

    
    items = fields.Nested(NestedTags, required=False)
    

