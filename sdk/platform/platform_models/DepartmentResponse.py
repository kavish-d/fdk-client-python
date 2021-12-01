"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .Department import Department


class DepartmentResponse(BaseSchema):

    
    items = fields.List(fields.Nested(Department, required=False), required=False)
    

