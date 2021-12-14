"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .FAQ import FAQ


class CreateFaqSchema(BaseSchema):
    # Content swagger.json

    
    faq = fields.Nested(FAQ, required=False)
    

