"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .SeoSchema import SeoSchema


class SeoComponent(Schema):

    
    seo = fields.Nested(SeoSchema, required=False)
    

