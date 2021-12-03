"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .StorePriorityRule import StorePriorityRule


class ArticleAssignmentRule(BaseSchema):

    
    store_priority = fields.Nested(StorePriorityRule, required=False)
    

