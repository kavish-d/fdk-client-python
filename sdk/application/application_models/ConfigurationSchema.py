"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *










class ConfigurationSchema(Schema):

    
    sleep_time = fields.Int(required=False)
    
    start_on_launch = fields.Boolean(required=False)
    
    duration = fields.Int(required=False)
    
    slide_direction = fields.Str(required=False)
    

