"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .ActionPage import ActionPage

from .ActionPage import ActionPage




class Action(BaseSchema):

    
    page = fields.Nested(ActionPage, required=False)
    
    popup = fields.Nested(ActionPage, required=False)
    
    type = fields.Str(required=False)
    

