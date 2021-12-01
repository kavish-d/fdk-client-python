"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .FAQ import FAQ


class CreateFaqSchema(BaseSchema):

    
    faq = fields.Nested(FAQ, required=False)
    

