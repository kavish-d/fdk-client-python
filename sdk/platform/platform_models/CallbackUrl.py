"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class CallbackUrl(Schema):

    
    app = fields.Str(required=False)
    
    web = fields.Str(required=False)
    

