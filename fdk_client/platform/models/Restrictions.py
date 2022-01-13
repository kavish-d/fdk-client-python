"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PriceRange import PriceRange

from .PostOrder import PostOrder



from .UsesRestriction import UsesRestriction





from .BulkBundleRestriction import BulkBundleRestriction




class Restrictions(BaseSchema):
    # Cart swagger.json

    
    price_range = fields.Nested(PriceRange, required=False)
    
    post_order = fields.Nested(PostOrder, required=False)
    
    coupon_allowed = fields.Boolean(required=False)
    
    uses = fields.Nested(UsesRestriction, required=False)
    
    platforms = fields.List(fields.Str(required=False), required=False)
    
    ordering_stores = fields.List(fields.Int(required=False), required=False)
    
    bulk_bundle = fields.Nested(BulkBundleRestriction, required=False)
    
    payments = fields.Dict(required=False)
    

