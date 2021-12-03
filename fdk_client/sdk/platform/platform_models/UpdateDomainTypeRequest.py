"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .UpdateDomain import UpdateDomain




class UpdateDomainTypeRequest(BaseSchema):

    
    domain = fields.Nested(UpdateDomain, required=False)
    
    action = fields.Str(required=False)
    

