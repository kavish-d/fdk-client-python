"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema



from .CardPaymentGateway import CardPaymentGateway




class ActiveCardPaymentGatewayResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    cards = fields.Nested(CardPaymentGateway, required=False)
    
    message = fields.Str(required=False)
    

