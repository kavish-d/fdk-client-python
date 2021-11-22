"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .PostOrder import PostOrder

from .UsesRestriction import UsesRestriction

from .PaymentCodes import PaymentCodes



from .BulkBundleRestriction import BulkBundleRestriction





from .PriceRange import PriceRange


class Restrictions(Schema):

    
    post_order = fields.Nested(PostOrder, required=False)
    
    uses = fields.Nested(UsesRestriction, required=False)
    
    payments = fields.Nested(PaymentCodes, required=False)
    
    ordering_stores = fields.List(fields.Int(required=False), required=False)
    
    bulk_bundle = fields.Nested(BulkBundleRestriction, required=False)
    
    platforms = fields.List(fields.Str(required=False), required=False)
    
    coupon_allowed = fields.Boolean(required=False)
    
    price_range = fields.Nested(PriceRange, required=False)
    

