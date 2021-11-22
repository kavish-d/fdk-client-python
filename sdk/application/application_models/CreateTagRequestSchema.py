"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .CreateTagSchema import CreateTagSchema


class CreateTagRequestSchema(Schema):

    
    tags = fields.List(fields.Nested(CreateTagSchema, required=False), required=False)
    

