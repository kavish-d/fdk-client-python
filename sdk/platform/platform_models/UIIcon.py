"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *








class UIIcon(Schema):

    
    active = fields.Str(required=False)
    
    inactive = fields.Str(required=False)
    
    selected = fields.List(fields.Str(required=False), required=False)
    

