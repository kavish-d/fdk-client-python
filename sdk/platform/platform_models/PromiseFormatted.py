"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class PromiseFormatted(Schema):

    
    min = fields.Str(required=False)
    
    max = fields.Str(required=False)
    

