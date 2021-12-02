"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class InvoiceCredSerializer(BaseSchema):

    
    enabled = fields.Boolean(required=False)
    
    password = fields.Str(required=False)
    
    username = fields.Str(required=False)
    

