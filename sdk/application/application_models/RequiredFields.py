"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .PlatformEmail import PlatformEmail

from .PlatformMobile import PlatformMobile


class RequiredFields(Schema):

    
    email = fields.Nested(PlatformEmail, required=False)
    
    mobile = fields.Nested(PlatformMobile, required=False)
    

