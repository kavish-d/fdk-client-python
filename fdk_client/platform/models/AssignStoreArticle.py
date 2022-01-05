"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .ArticleQuery import ArticleQuery

from .ArticleAssignment import ArticleAssignment




class AssignStoreArticle(BaseSchema):
    # Catalog swagger.json

    
    meta = fields.Dict(required=False)
    
    group_id = fields.Str(required=False)
    
    query = fields.Nested(ArticleQuery, required=False)
    
    article_assignment = fields.Nested(ArticleAssignment, required=False)
    
    quantity = fields.Int(required=False)
    

