"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class SubscriptionPauseCollection(Schema):

    
    behavior = fields.Str(required=False)
    
    resume_at = fields.Str(required=False)
    

