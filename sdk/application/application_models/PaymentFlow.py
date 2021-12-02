"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .AggregatorRoute import AggregatorRoute

from .AggregatorRoute import AggregatorRoute

from .AggregatorRoute import AggregatorRoute

from .AggregatorRoute import AggregatorRoute

from .AggregatorRoute import AggregatorRoute

from .AggregatorRoute import AggregatorRoute

from .AggregatorRoute import AggregatorRoute

from .AggregatorRoute import AggregatorRoute

from .AggregatorRoute import AggregatorRoute

from .AggregatorRoute import AggregatorRoute

from .AggregatorRoute import AggregatorRoute


class PaymentFlow(BaseSchema):

    
    fynd = fields.Nested(AggregatorRoute, required=False)
    
    rupifi = fields.Nested(AggregatorRoute, required=False)
    
    upi_razorpay = fields.Nested(AggregatorRoute, required=False)
    
    juspay = fields.Nested(AggregatorRoute, required=False)
    
    simpl = fields.Nested(AggregatorRoute, required=False)
    
    stripe = fields.Nested(AggregatorRoute, required=False)
    
    ccavenue = fields.Nested(AggregatorRoute, required=False)
    
    payubiz = fields.Nested(AggregatorRoute, required=False)
    
    bqr_razorpay = fields.Nested(AggregatorRoute, required=False)
    
    razorpay = fields.Nested(AggregatorRoute, required=False)
    
    mswipe = fields.Nested(AggregatorRoute, required=False)
    

