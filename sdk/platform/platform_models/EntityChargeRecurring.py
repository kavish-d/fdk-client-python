"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class EntityChargeRecurring(Schema):

    
    interval = fields.Str(required=False)
    

