"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Department import Department


class DepartmentResponse(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(Department, required=False), required=False)
    

