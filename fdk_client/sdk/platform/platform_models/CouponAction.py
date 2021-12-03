"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class CouponAction(BaseSchema):

    
    action_date = fields.Str(required=False)
    
    txn_mode = fields.Str(required=False)
    
