"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class SubscriptionLimitOtherPlatform(Schema):

    
    enabled = fields.Boolean(required=False)
    

