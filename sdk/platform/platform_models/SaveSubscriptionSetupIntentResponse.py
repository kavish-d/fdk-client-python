"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class SaveSubscriptionSetupIntentResponse(Schema):

    
    success = fields.Boolean(required=False)
    
    data = fields.Dict(required=False)
    

