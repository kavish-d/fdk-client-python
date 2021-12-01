"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema



from .DomainStatus import DomainStatus


class DomainStatusResponse(BaseSchema):

    
    connected = fields.Boolean(required=False)
    
    status = fields.List(fields.Nested(DomainStatus, required=False), required=False)
    

