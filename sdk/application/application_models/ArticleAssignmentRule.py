"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .StorePriorityRule import StorePriorityRule


class ArticleAssignmentRule(Schema):

    
    store_priority = fields.Nested(StorePriorityRule, required=False)
    

