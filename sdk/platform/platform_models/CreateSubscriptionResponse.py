"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .EntitySubscription import EntitySubscription




class CreateSubscriptionResponse(BaseSchema):

    
    subscription = fields.Nested(EntitySubscription, required=False)
    
    confirm_url = fields.Str(required=False)
    

