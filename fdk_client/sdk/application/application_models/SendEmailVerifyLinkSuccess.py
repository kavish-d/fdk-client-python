"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema




class SendEmailVerifyLinkSuccess(BaseSchema):
    # User swagger.json

    
    verify_email_link = fields.Boolean(required=False)
    

