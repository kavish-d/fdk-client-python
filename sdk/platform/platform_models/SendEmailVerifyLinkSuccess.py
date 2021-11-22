"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class SendEmailVerifyLinkSuccess(Schema):

    
    verify_email_link = fields.Boolean(required=False)
    

