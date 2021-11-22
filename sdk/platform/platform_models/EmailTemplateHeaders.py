"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class EmailTemplateHeaders(Schema):

    
    key = fields.Str(required=False)
    
    value = fields.Str(required=False)
    

