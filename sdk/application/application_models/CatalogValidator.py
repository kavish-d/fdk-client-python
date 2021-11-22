"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

class CatalogValidator:
    
    class getProductDetailBySlug(Schema):
        
        slug = fields.Str(required=False)
         
    
    class getProductSizesBySlug(Schema):
        
        slug = fields.Str(required=False)
        
        store_id = fields.Int(required=False)
         
    
    class getProductPriceBySlug(Schema):
        
        slug = fields.Str(required=False)
        
        size = fields.Str(required=False)
        
        pincode = fields.Str(required=False)
        
        store_id = fields.Int(required=False)
         
    
    class getProductSellersBySlug(Schema):
        
        slug = fields.Str(required=False)
        
        size = fields.Str(required=False)
        
        pincode = fields.Str(required=False)
        
        strategy = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getProductComparisonBySlugs(Schema):
        
        slug = fields.List(fields.Str(required=False), required=False)
         
    
    class getSimilarComparisonProductBySlug(Schema):
        
        slug = fields.Str(required=False)
         
    
    class getComparedFrequentlyProductBySlug(Schema):
        
        slug = fields.Str(required=False)
         
    
    class getProductSimilarByIdentifier(Schema):
        
        slug = fields.Str(required=False)
        
        similar_type = fields.Str(required=False)
         
    
    class getProductVariantsBySlug(Schema):
        
        slug = fields.Str(required=False)
         
    
    class getProductStockByIds(Schema):
        
        item_id = fields.Str(required=False)
        
        alu = fields.Str(required=False)
        
        sku_code = fields.Str(required=False)
        
        ean = fields.Str(required=False)
        
        upc = fields.Str(required=False)
         
    
    class getProductStockForTimeByIds(Schema):
        
        timestamp = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
        
        page_id = fields.Str(required=False)
         
    
    class getProducts(Schema):
        
        q = fields.Str(required=False)
        
        f = fields.Str(required=False)
        
        filters = fields.Boolean(required=False)
        
        sort_on = fields.Str(required=False)
        
        page_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_type = fields.Str(required=False)
         
    
    class getBrands(Schema):
        
        department = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getBrandDetailBySlug(Schema):
        
        slug = fields.Str(required=False)
         
    
    class getCategories(Schema):
        
        department = fields.Str(required=False)
         
    
    class getCategoryDetailBySlug(Schema):
        
        slug = fields.Str(required=False)
         
    
    class getHomeProducts(Schema):
        
        sort_on = fields.Str(required=False)
        
        page_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getDepartments(Schema):
        
        pass 
    
    class getSearchResults(Schema):
        
        q = fields.Str(required=False)
         
    
    class getCollections(Schema):
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        tag = fields.List(fields.Str(required=False), required=False)
         
    
    class getCollectionItemsBySlug(Schema):
        
        slug = fields.Str(required=False)
        
        f = fields.Str(required=False)
        
        filters = fields.Boolean(required=False)
        
        sort_on = fields.Str(required=False)
        
        page_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getCollectionDetailBySlug(Schema):
        
        slug = fields.Str(required=False)
         
    
    class getFollowedListing(Schema):
        
        collection_type = fields.Str(required=False)
        
        page_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class followById(Schema):
        
        collection_type = fields.Str(required=False)
        
        collection_id = fields.Str(required=False)
         
    
    class unfollowById(Schema):
        
        collection_type = fields.Str(required=False)
        
        collection_id = fields.Str(required=False)
         
    
    class getFollowerCountById(Schema):
        
        collection_type = fields.Str(required=False)
        
        collection_id = fields.Str(required=False)
         
    
    class getFollowIds(Schema):
        
        collection_type = fields.Str(required=False)
         
    
    class getStores(Schema):
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
        
        city = fields.Str(required=False)
        
        range = fields.Int(required=False)
        
        latitude = fields.Float(required=False)
        
        longitude = fields.Float(required=False)
         
    
    class getInStockLocations(Schema):
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
        
        city = fields.Str(required=False)
        
        range = fields.Int(required=False)
        
        latitude = fields.Float(required=False)
        
        longitude = fields.Float(required=False)
         
    
    class getLocationDetailsById(Schema):
        
        location_id = fields.Int(required=False)
         
    