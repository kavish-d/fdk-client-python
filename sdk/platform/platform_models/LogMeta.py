"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *














class LogMeta(Schema):

    
    type = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    offset = fields.Str(required=False)
    
    partition = fields.Str(required=False)
    
    topic = fields.Str(required=False)
    

