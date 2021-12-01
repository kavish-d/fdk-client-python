"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .Department import Department


class DepartmentResponse(BaseSchema):

    
    items = fields.List(fields.Nested(Department, required=False), required=False)
    

