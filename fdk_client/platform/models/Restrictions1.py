"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .PromotionPaymentModes import PromotionPaymentModes

from .UsesRestriction1 import UsesRestriction1

from .PostOrder1 import PostOrder1




class Restrictions1(BaseSchema):
    # Cart swagger.json

    
    user_registered_after = fields.Str(required=False)
    
    user_id = fields.List(fields.Str(required=False), required=False)
    
    anonymous_users = fields.Boolean(required=False)
    
    payments = fields.List(fields.Nested(PromotionPaymentModes, required=False), required=False)
    
    uses = fields.Nested(UsesRestriction1, required=False)
    
    post_order = fields.Nested(PostOrder1, required=False)
    
    platforms = fields.List(fields.Str(required=False), required=False)
    

