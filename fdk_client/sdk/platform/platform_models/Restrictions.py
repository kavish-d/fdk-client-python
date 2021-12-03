"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema



from .UsesRestriction import UsesRestriction



from .BulkBundleRestriction import BulkBundleRestriction



from .PriceRange import PriceRange

from .PostOrder import PostOrder

from .PaymentCodes import PaymentCodes


class Restrictions(BaseSchema):

    
    coupon_allowed = fields.Boolean(required=False)
    
    uses = fields.Nested(UsesRestriction, required=False)
    
    platforms = fields.List(fields.Str(required=False), required=False)
    
    bulk_bundle = fields.Nested(BulkBundleRestriction, required=False)
    
    ordering_stores = fields.List(fields.Int(required=False), required=False)
    
    price_range = fields.Nested(PriceRange, required=False)
    
    post_order = fields.Nested(PostOrder, required=False)
    
    payments = fields.Nested(PaymentCodes, required=False)
    
