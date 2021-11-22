"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class SubscriptionLimitTeam(Schema):

    
    limit = fields.Int(required=False)
    

