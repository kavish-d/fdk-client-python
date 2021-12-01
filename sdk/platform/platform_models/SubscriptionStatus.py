"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema



from .Subscription import Subscription


class SubscriptionStatus(BaseSchema):

    
    is_enabled = fields.Boolean(required=False)
    
    subscription = fields.Nested(Subscription, required=False)
    

