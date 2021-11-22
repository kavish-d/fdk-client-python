"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *










class FailOrderDateMeta(Schema):

    
    added_on_store = fields.Str(required=False)
    
    inventory_updated_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    

