"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ArticleAssignment import ArticleAssignment

from .ArticleQuery import ArticleQuery






class AssignStoreArticle(BaseSchema):
    # Catalog swagger.json

    
    group_id = fields.Str(required=False)
    
    article_assignment = fields.Nested(ArticleAssignment, required=False)
    
    query = fields.Nested(ArticleQuery, required=False)
    
    quantity = fields.Int(required=False)
    
    meta = fields.Dict(required=False)
    

