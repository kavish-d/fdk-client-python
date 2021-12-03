"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class DomainStatus(BaseSchema):

    
    display = fields.Str(required=False)
    
    status = fields.Boolean(required=False)
    
