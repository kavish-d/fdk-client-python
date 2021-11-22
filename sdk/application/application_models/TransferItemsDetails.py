"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *












class TransferItemsDetails(Schema):

    
    id = fields.Str(required=False)
    
    logo_small = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    logo_large = fields.Str(required=False)
    
    display_name = fields.Boolean(required=False)
    

