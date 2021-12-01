"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema







from .Association import Association





from .AuthMeta import AuthMeta




class SubscriberConfig(BaseSchema):

    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    webhook_url = fields.Str(required=False)
    
    association = fields.Nested(Association, required=False)
    
    status = fields.Str(required=False, validate=OneOf(SubscriberStatus.__members__.keys()))
    
    email_id = fields.Str(required=False)
    
    auth_meta = fields.Nested(AuthMeta, required=False)
    
    event_id = fields.List(fields.Int(required=False), required=False)
    

