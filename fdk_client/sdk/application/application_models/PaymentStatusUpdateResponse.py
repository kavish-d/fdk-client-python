"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema








class PaymentStatusUpdateResponse(BaseSchema):
    # Payment swagger.json

    
    aggregator_name = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    retry = fields.Boolean(required=False)
    

