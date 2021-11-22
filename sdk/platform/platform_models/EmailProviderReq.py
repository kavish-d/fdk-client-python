"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *











from .EmailProviderReqFrom import EmailProviderReqFrom


class EmailProviderReq(Schema):

    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    api_key = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    provider = fields.Str(required=False)
    
    from_ = fields.List(fields.Nested(EmailProviderReqFrom, required=False), required=False)
    

