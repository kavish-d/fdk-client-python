"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema







from .ProductListingPrice import ProductListingPrice







from .ActionPage import ActionPage













from .Media import Media



from .ProductBrand import ProductBrand











from .ProductBrand import ProductBrand



from .ProductDetailGroupedAttribute import ProductDetailGroupedAttribute






class ProductListingDetail(BaseSchema):
    # Catalog swagger.json

    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    has_variant = fields.Boolean(required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    image_nature = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    action = fields.Nested(ActionPage, required=False)
    
    rating = fields.Float(required=False)
    
    attributes = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    rating_count = fields.Int(required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    product_online_date = fields.Str(required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    discount = fields.Str(required=False)
    
    teaser_tag = fields.Str(required=False)
    
    sellable = fields.Boolean(required=False)
    
    uid = fields.Int(required=False)
    
    short_description = fields.Str(required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    color = fields.Str(required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    item_type = fields.Str(required=False)
    
    item_code = fields.Str(required=False)
    

