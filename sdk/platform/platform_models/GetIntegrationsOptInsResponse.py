"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .IntegrationOptIn import IntegrationOptIn

from .Page import Page


class GetIntegrationsOptInsResponse(Schema):

    
    items = fields.List(fields.Nested(IntegrationOptIn, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

