"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class SendMobileVerifyLinkSuccess(Schema):

    
    verify_mobile_link = fields.Boolean(required=False)
    

