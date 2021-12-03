"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .DepartmentCategoryTree import DepartmentCategoryTree

from .DepartmentIdentifier import DepartmentIdentifier


class CategoryListingResponse(BaseSchema):

    
    data = fields.List(fields.Nested(DepartmentCategoryTree, required=False), required=False)
    
    departments = fields.List(fields.Nested(DepartmentIdentifier, required=False), required=False)
    
