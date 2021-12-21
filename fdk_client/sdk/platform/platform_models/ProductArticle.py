"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema



from .BaseInfo import BaseInfo

from .BaseInfo import BaseInfo





from .ArticlePriceInfo import ArticlePriceInfo






class ProductArticle(BaseSchema):
    # Cart swagger.json

    
    uid = fields.Str(required=False)
    
    store = fields.Nested(BaseInfo, required=False)
    
    seller = fields.Nested(BaseInfo, required=False)
    
    quantity = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    price = fields.Nested(ArticlePriceInfo, required=False)
    
    extra_meta = fields.Dict(required=False)
    
    size = fields.Str(required=False)
    

