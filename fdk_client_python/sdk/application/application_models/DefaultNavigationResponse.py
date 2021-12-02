"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .NavigationSchema import NavigationSchema


class DefaultNavigationResponse(BaseSchema):

    
    items = fields.List(fields.Nested(NavigationSchema, required=False), required=False)
    

