"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class ListSizeGuide(BaseSchema):

    
    page = fields.Dict(required=False)
    
    items = fields.List(fields.Dict(required=False), required=False)
    
