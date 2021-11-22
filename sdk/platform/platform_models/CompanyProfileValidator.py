"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

class CompanyProfileValidator:
    
    class updateCompany(Schema):
        
        company_id = fields.Str(required=False)
         
    
    class cbsOnboardGet(Schema):
        
        company_id = fields.Str(required=False)
         
    
    class getCompanyMetrics(Schema):
        
        company_id = fields.Str(required=False)
         
    
    class editBrand(Schema):
        
        company_id = fields.Str(required=False)
        
        brand_id = fields.Str(required=False)
         
    
    class getBrand(Schema):
        
        company_id = fields.Str(required=False)
        
        brand_id = fields.Str(required=False)
         
    
    class createBrand(Schema):
        
        company_id = fields.Str(required=False)
         
    
    class createCompanyBrandMapping(Schema):
        
        company_id = fields.Str(required=False)
         
    
    class getBrands(Schema):
        
        company_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
         
    
    class createLocation(Schema):
        
        company_id = fields.Str(required=False)
         
    
    class getLocations(Schema):
        
        company_id = fields.Str(required=False)
        
        store_type = fields.Str(required=False)
        
        q = fields.Str(required=False)
        
        stage = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class updateLocation(Schema):
        
        company_id = fields.Str(required=False)
        
        location_id = fields.Str(required=False)
         
    
    class getLocationDetail(Schema):
        
        company_id = fields.Str(required=False)
        
        location_id = fields.Str(required=False)
         
    
    class createLocationBulk(Schema):
        
        company_id = fields.Str(required=False)
         
    