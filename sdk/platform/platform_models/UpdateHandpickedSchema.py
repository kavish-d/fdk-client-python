"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .HandpickedTagSchema import HandpickedTagSchema


class UpdateHandpickedSchema(BaseSchema):

    
    tag = fields.Nested(HandpickedTagSchema, required=False)
    

