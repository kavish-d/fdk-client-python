"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class AttributeSchemaRange(Schema):

    
    min = fields.Int(required=False)
    
    max = fields.Int(required=False)
    

