"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .AvailablePageSchema import AvailablePageSchema


class Preset(BaseSchema):

    
    pages = fields.List(fields.Nested(AvailablePageSchema, required=False), required=False)
    

