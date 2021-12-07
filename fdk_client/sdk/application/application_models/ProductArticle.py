"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .ArticlePriceInfo import ArticlePriceInfo



from .BaseInfo import BaseInfo





from .BaseInfo import BaseInfo






class ProductArticle(BaseSchema):

    
    price = fields.Nested(ArticlePriceInfo, required=False)
    
    quantity = fields.Int(required=False)
    
    store = fields.Nested(BaseInfo, required=False)
    
    extra_meta = fields.Dict(required=False)
    
    uid = fields.Str(required=False)
    
    seller = fields.Nested(BaseInfo, required=False)
    
    size = fields.Str(required=False)
    
    type = fields.Str(required=False)
    

