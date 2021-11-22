"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .UpdateDomain import UpdateDomain




class UpdateDomainTypeRequest(Schema):

    
    domain = fields.Nested(UpdateDomain, required=False)
    
    action = fields.Str(required=False)
    

