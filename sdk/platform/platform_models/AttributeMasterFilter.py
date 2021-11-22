"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *








class AttributeMasterFilter(Schema):

    
    indexing = fields.Boolean(required=False)
    
    depends_on = fields.List(fields.Str(required=False), required=False)
    
    priority = fields.Int(required=False)
    

