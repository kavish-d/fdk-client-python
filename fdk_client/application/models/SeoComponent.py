"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .SeoSchema import SeoSchema


class SeoComponent(BaseSchema):
    # Content swagger.json

    
    seo = fields.Nested(SeoSchema, required=False)
    

