"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

class ConfigurationValidator:
    
    class getBuildConfig(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        platform_type = fields.Str(required=False)
         
    
    class updateBuildConfig(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        platform_type = fields.Str(required=False)
         
    
    class getPreviousVersions(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        platform_type = fields.Str(required=False)
         
    
    class getAppFeatures(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class updateAppFeatures(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getAppBasicDetails(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class updateAppBasicDetails(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getAppContactInfo(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class updateAppContactInfo(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getAppApiTokens(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class updateAppApiTokens(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getAppCompanies(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getAppStores(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getInventoryConfig(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class updateInventoryConfig(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class partiallyUpdateInventoryConfig(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getAppCurrencyConfig(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class updateAppCurrencyConfig(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getAppSupportedCurrency(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getOrderingStoresByFilter(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class updateOrderingStoreConfig(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getStaffOrderingStores(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
         
    
    class getDomains(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class addDomain(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class removeDomainById(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class changeDomainType(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getDomainStatus(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class createApplication(Schema):
        
        company_id = fields.Str(required=False)
         
    
    class getApplications(Schema):
        
        company_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
         
    
    class getApplicationById(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getCurrencies(Schema):
        
        company_id = fields.Str(required=False)
         
    
    class getDomainAvailibility(Schema):
        
        company_id = fields.Str(required=False)
         
    
    class getIntegrationById(Schema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Int(required=False)
         
    
    class getAvailableOptIns(Schema):
        
        company_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getSelectedOptIns(Schema):
        
        company_id = fields.Str(required=False)
        
        level = fields.Str(required=False)
        
        uid = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getIntegrationLevelConfig(Schema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        level = fields.Str(required=False)
        
        opted = fields.Boolean(required=False)
        
        check_permission = fields.Boolean(required=False)
         
    
    class getIntegrationByLevelId(Schema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        level = fields.Str(required=False)
        
        uid = fields.Int(required=False)
         
    
    class updateLevelUidIntegration(Schema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        level = fields.Str(required=False)
        
        uid = fields.Int(required=False)
         
    
    class getLevelActiveIntegrations(Schema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        level = fields.Str(required=False)
        
        uid = fields.Int(required=False)
         
    
    class updateLevelIntegration(Schema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        level = fields.Str(required=False)
         
    
    class getBrandsByCompany(Schema):
        
        company_id = fields.Str(required=False)
        
        q = fields.Str(required=False)
         
    
    class getCompanyByBrands(Schema):
        
        company_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getStoreByBrands(Schema):
        
        company_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getOtherSellerApplications(Schema):
        
        company_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getOtherSellerApplicationById(Schema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class optOutFromApplication(Schema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    