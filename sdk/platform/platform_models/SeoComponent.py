"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .SeoSchema import SeoSchema


class SeoComponent(Schema):

    
    seo = fields.Nested(SeoSchema, required=False)
    

