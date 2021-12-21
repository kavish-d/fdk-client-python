"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema







from .AttributeSchemaRange import AttributeSchemaRange






class AttributeMaster(BaseSchema):
    # Catalog swagger.json

    
    mandatory = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    format = fields.Str(required=False)
    
    range = fields.Nested(AttributeSchemaRange, required=False)
    
    allowed_values = fields.List(fields.Str(required=False), required=False)
    
    multi = fields.Boolean(required=False)
    

