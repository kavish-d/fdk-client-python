"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .SeoSchema import SeoSchema


class SeoComponent(BaseSchema):

    
    seo = fields.Nested(SeoSchema, required=False)
    

