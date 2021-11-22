"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *








class SortMethod(Schema):

    
    name = fields.Str(required=False)
    
    selected = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    

