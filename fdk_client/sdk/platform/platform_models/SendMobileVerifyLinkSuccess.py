"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema




class SendMobileVerifyLinkSuccess(BaseSchema):
    # User swagger.json

    
    verify_mobile_link = fields.Boolean(required=False)
    

