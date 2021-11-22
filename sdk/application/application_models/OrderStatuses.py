"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *








class OrderStatuses(Schema):

    
    display = fields.Str(required=False)
    
    value = fields.Int(required=False)
    
    is_selected = fields.Boolean(required=False)
    

