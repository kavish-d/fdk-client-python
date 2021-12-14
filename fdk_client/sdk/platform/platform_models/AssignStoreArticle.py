"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .ArticleAssignment import ArticleAssignment





from .ArticleQuery import ArticleQuery




class AssignStoreArticle(BaseSchema):
    # Catalog swagger.json

    
    article_assignment = fields.Nested(ArticleAssignment, required=False)
    
    quantity = fields.Int(required=False)
    
    group_id = fields.Str(required=False)
    
    query = fields.Nested(ArticleQuery, required=False)
    
    meta = fields.Dict(required=False)
    

