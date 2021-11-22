"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .Department import Department


class DepartmentResponse(Schema):

    
    items = fields.List(fields.Nested(Department, required=False), required=False)
    

