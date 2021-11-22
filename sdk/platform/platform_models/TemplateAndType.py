"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class TemplateAndType(Schema):

    
    template_type = fields.Str(required=False)
    
    template = fields.Str(required=False)
    

