"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema




class SendMobileVerifyLinkSuccess(BaseSchema):
    # User swagger.json

    
    verify_mobile_link = fields.Boolean(required=False)
    

