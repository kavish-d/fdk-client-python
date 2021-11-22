"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *










class SubscriberEvent(Schema):

    
    id = fields.Int(required=False)
    
    subscriber_id = fields.Int(required=False)
    
    event_id = fields.Int(required=False)
    
    created_date = fields.Str(required=False)
    

