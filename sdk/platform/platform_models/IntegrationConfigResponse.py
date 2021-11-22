"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .IntegrationLevel import IntegrationLevel


class IntegrationConfigResponse(Schema):

    
    items = fields.List(fields.Nested(IntegrationLevel, required=False), required=False)
    

