"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .EntitySubscription import EntitySubscription




class CreateSubscriptionResponse(Schema):

    
    subscription = fields.Nested(EntitySubscription, required=False)
    
    confirm_url = fields.Str(required=False)
    

