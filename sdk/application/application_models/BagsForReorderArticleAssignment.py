"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class BagsForReorderArticleAssignment(Schema):

    
    level = fields.Str(required=False)
    
    strategy = fields.Str(required=False)
    

