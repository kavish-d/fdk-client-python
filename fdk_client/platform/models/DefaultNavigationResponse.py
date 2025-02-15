"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .NavigationSchema import NavigationSchema


class DefaultNavigationResponse(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(NavigationSchema, required=False), required=False)
    

