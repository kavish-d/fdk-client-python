"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
















class ProfileEditSuccessSchema(Schema):

    
    email = fields.Str(required=False)
    
    verify_email_otp = fields.Boolean(required=False)
    
    verify_email_link = fields.Boolean(required=False)
    
    verify_mobile_otp = fields.Boolean(required=False)
    
    user = fields.Str(required=False)
    
    register_token = fields.Str(required=False)
    
    user_exists = fields.Boolean(required=False)
    

