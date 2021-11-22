"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .StorePriority import StorePriority


class ArticleAssignmentRules(Schema):

    
    store_priority = fields.Nested(StorePriority, required=False)
    

