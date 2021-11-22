"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .DepartmentCategoryTree import DepartmentCategoryTree

from .DepartmentIdentifier import DepartmentIdentifier


class CategoryListingResponse(Schema):

    
    data = fields.List(fields.Nested(DepartmentCategoryTree, required=False), required=False)
    
    departments = fields.List(fields.Nested(DepartmentIdentifier, required=False), required=False)
    

