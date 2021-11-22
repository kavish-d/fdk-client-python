"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *







from .AttributeSchemaRange import AttributeSchemaRange






class AttributeMaster(Schema):

    
    type = fields.Str(required=False)
    
    mandatory = fields.Boolean(required=False)
    
    format = fields.Str(required=False)
    
    range = fields.Nested(AttributeSchemaRange, required=False)
    
    multi = fields.Boolean(required=False)
    
    allowed_values = fields.List(fields.Str(required=False), required=False)
    

