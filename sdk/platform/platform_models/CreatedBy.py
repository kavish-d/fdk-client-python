"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *





from .TagMeta import TagMeta


class CreatedBy(Schema):

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    tags = fields.List(fields.Nested(TagMeta, required=False), required=False)
    

