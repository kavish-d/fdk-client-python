"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class RewardsRule(Schema):

    
    amount = fields.Float(required=False)
    

