"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *








class TicketAsset(Schema):

    
    display = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    type = fields.Raw(required=False)
    

