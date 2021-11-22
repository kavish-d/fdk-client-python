"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class PageSpecParam(Schema):

    
    key = fields.Str(required=False)
    
    required = fields.Boolean(required=False)
    

