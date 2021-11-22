"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class PlatformOrderDetailsPage(Schema):

    
    next = fields.Str(required=False)
    
    previous = fields.Str(required=False)
    

