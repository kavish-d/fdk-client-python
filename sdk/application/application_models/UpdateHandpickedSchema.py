"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .HandpickedTagSchema import HandpickedTagSchema


class UpdateHandpickedSchema(Schema):

    
    tag = fields.Nested(HandpickedTagSchema, required=False)
    

