"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class DomainStatusRequest(Schema):

    
    domain_url = fields.Str(required=False)
    

