"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .NavigationSchema import NavigationSchema


class DefaultNavigationResponse(Schema):

    
    items = fields.List(fields.Nested(NavigationSchema, required=False), required=False)
    

