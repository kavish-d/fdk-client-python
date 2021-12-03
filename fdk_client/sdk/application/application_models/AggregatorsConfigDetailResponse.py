"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .AggregatorConfigDetail import AggregatorConfigDetail

from .AggregatorConfigDetail import AggregatorConfigDetail

from .AggregatorConfigDetail import AggregatorConfigDetail

from .AggregatorConfigDetail import AggregatorConfigDetail

from .AggregatorConfigDetail import AggregatorConfigDetail



from .AggregatorConfigDetail import AggregatorConfigDetail

from .AggregatorConfigDetail import AggregatorConfigDetail

from .AggregatorConfigDetail import AggregatorConfigDetail




class AggregatorsConfigDetailResponse(BaseSchema):

    
    mswipe = fields.Nested(AggregatorConfigDetail, required=False)
    
    rupifi = fields.Nested(AggregatorConfigDetail, required=False)
    
    simpl = fields.Nested(AggregatorConfigDetail, required=False)
    
    ccavenue = fields.Nested(AggregatorConfigDetail, required=False)
    
    razorpay = fields.Nested(AggregatorConfigDetail, required=False)
    
    env = fields.Str(required=False)
    
    juspay = fields.Nested(AggregatorConfigDetail, required=False)
    
    stripe = fields.Nested(AggregatorConfigDetail, required=False)
    
    payumoney = fields.Nested(AggregatorConfigDetail, required=False)
    
    success = fields.Boolean(required=False)
    
