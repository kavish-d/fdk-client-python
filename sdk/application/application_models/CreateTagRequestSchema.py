"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .CreateTagSchema import CreateTagSchema


class CreateTagRequestSchema(BaseSchema):

    
    tags = fields.List(fields.Nested(CreateTagSchema, required=False), required=False)
    

