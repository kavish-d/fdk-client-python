"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *



from .Subscription import Subscription


class CancelSubscriptionRes(Schema):

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(Subscription, required=False)
    

