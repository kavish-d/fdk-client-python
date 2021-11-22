"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *












class SendVerificationLinkMobileRequestSchema(Schema):

    
    verified = fields.Boolean(required=False)
    
    active = fields.Boolean(required=False)
    
    country_code = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    primary = fields.Boolean(required=False)
    

