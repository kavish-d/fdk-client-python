"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class AddProxyReq(Schema):

    
    attached_path = fields.Str(required=False)
    
    proxy_url = fields.Str(required=False)
    

