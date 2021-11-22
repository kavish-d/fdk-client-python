"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *








class ShipmentPayment(Schema):

    
    logo = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    status = fields.Str(required=False)
    

