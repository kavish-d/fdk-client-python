"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

class ConfigurationValidator:
    
    class getApplication(Schema):
        
        pass 
    
    class getOwnerInfo(Schema):
        
        pass 
    
    class getBasicDetails(Schema):
        
        pass 
    
    class getIntegrationTokens(Schema):
        
        pass 
    
    class getOrderingStores(Schema):
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
         
    
    class getStoreDetailById(Schema):
        
        store_id = fields.Int(required=False)
         
    
    class getFeatures(Schema):
        
        pass 
    
    class getContactInfo(Schema):
        
        pass 
    
    class getCurrencies(Schema):
        
        pass 
    
    class getCurrencyById(Schema):
        
        id = fields.Str(required=False)
         
    
    class getAppCurrencies(Schema):
        
        pass 
    
    class getLanguages(Schema):
        
        pass 
    
    class getOrderingStoreCookie(Schema):
        
        pass 
    
    class removeOrderingStoreCookie(Schema):
        
        pass 
    
    class getAppStaffs(Schema):
        
        order_incent = fields.Boolean(required=False)
        
        ordering_store = fields.Int(required=False)
        
        user = fields.Str(required=False)
         
    