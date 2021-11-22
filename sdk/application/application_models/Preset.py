"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .AvailablePageSchema import AvailablePageSchema


class Preset(Schema):

    
    pages = fields.List(fields.Nested(AvailablePageSchema, required=False), required=False)
    

