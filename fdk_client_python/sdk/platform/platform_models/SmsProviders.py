"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .SmsProvider import SmsProvider

from .Page import Page


class SmsProviders(BaseSchema):

    
    items = fields.List(fields.Nested(SmsProvider, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

