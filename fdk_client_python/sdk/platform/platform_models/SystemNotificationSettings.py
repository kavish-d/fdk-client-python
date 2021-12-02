"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class SystemNotificationSettings(BaseSchema):

    
    sound = fields.Boolean(required=False)
    
    priority = fields.Str(required=False)
    
    time_to_live = fields.Str(required=False)
    

