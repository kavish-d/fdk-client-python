"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .IntegrationOptIn import IntegrationOptIn

from .Page import Page


class GetIntegrationsOptInsResponse(BaseSchema):

    
    items = fields.List(fields.Nested(IntegrationOptIn, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

