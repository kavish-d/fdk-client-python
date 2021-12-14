"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .StorePriorityRule import StorePriorityRule


class ArticleAssignmentRule(BaseSchema):
    # Configuration swagger.json

    
    store_priority = fields.Nested(StorePriorityRule, required=False)
    

