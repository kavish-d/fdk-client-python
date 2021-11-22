"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .Department import Department


class DepartmentResponse(Schema):

    
    items = fields.List(fields.Nested(Department, required=False), required=False)
    

