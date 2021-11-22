"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *












class Document(Schema):

    
    value = fields.Str(required=False)
    
    verified = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    legal_name = fields.Str(required=False)
    

