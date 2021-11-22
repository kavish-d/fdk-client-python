"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *





from .ArticleQuery import ArticleQuery

from .ArticleAssignment import ArticleAssignment




class AssignStoreArticle(Schema):

    
    group_id = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    query = fields.Nested(ArticleQuery, required=False)
    
    article_assignment = fields.Nested(ArticleAssignment, required=False)
    
    quantity = fields.Int(required=False)
    

