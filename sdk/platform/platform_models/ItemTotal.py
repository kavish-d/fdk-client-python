"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *










class ItemTotal(Schema):

    
    new = fields.Int(required=False)
    
    processing = fields.Int(required=False)
    
    returns = fields.Int(required=False)
    
    all = fields.Int(required=False)
    

