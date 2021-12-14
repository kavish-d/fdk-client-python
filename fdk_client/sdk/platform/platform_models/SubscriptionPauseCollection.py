"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class SubscriptionPauseCollection(BaseSchema):
    # Billing swagger.json

    
    behavior = fields.Str(required=False)
    
    resume_at = fields.Str(required=False)
    

