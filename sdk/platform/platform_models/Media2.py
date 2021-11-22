"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *








class Media2(Schema):

    
    landscape = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    portrait = fields.Str(required=False)
    

