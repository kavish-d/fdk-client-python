"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class WebRedirect(Schema):

    
    link = fields.Str(required=False)
    
    type = fields.Str(required=False)
    

