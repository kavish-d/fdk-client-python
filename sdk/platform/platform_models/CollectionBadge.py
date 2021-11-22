"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class CollectionBadge(Schema):

    
    text = fields.Str(required=False)
    
    color = fields.Str(required=False)
    

