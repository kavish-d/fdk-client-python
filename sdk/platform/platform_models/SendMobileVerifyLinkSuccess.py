"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class SendMobileVerifyLinkSuccess(Schema):

    
    verify_mobile_link = fields.Boolean(required=False)
    

