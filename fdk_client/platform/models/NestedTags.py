"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class NestedTags(BaseSchema):
    # Catalog swagger.json

    
    tags = fields.List(fields.Str(required=False), required=False)
    

