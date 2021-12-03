"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .IntegrationLevel import IntegrationLevel


class IntegrationConfigResponse(BaseSchema):

    
    items = fields.List(fields.Nested(IntegrationLevel, required=False), required=False)
    

