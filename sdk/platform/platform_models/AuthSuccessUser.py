"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *





from .AuthSuccessUserDebug import AuthSuccessUserDebug



from .AuthSuccessUserEmails import AuthSuccessUserEmails


class AuthSuccessUser(Schema):

    
    first_name = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    debug = fields.Nested(AuthSuccessUserDebug, required=False)
    
    active = fields.Boolean(required=False)
    
    emails = fields.Nested(AuthSuccessUserEmails, required=False)
    

