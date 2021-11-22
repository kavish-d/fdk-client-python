"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class InventoryValidationResponse(Schema):

    
    data = fields.Dict(required=False)
    
    message = fields.Str(required=False)
    

