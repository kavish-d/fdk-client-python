"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .GetLocationSerializer import GetLocationSerializer

from .Page import Page


class LocationListSerializer(BaseSchema):

    
    items = fields.List(fields.Nested(GetLocationSerializer, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

