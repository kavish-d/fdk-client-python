"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *








class PaymentStatusUpdateResponse(Schema):

    
    aggregator_name = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    retry = fields.Boolean(required=False)
    

