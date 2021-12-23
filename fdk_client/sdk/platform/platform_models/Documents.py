"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .Gst import Gst


class Documents(BaseSchema):
    # Order swagger.json

    
    gst = fields.Nested(Gst, required=False)
    

