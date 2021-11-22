"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

class CatalogValidator:
    
    class deleteSearchKeywords(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class updateSearchKeywords(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class getSearchKeywords(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class createCustomKeyword(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getAllSearchKeyword(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class deleteAutocompleteKeyword(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class updateAutocompleteKeyword(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class getAutocompleteKeywordDetail(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class createCustomAutocompleteRule(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getAutocompleteConfig(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class createProductBundle(Schema):
        
        company_id = fields.Str(required=False)
         
    
    class getProductBundle(Schema):
        
        company_id = fields.Str(required=False)
        
        q = fields.Str(required=False)
         
    
    class updateProductBundle(Schema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class getProductBundleDetail(Schema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class createSizeGuide(Schema):
        
        company_id = fields.Str(required=False)
         
    
    class getSizeGuides(Schema):
        
        company_id = fields.Str(required=False)
        
        active = fields.Boolean(required=False)
        
        q = fields.Str(required=False)
        
        tag = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class updateSizeGuide(Schema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class getSizeGuide(Schema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class getCatalogConfiguration(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class createConfigurationProductListing(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getConfigurations(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class createConfigurationByType(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        type = fields.Str(required=False)
         
    
    class getConfigurationByType(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        type = fields.Str(required=False)
         
    
    class getQueryFilters(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class createCollection(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getAllCollections(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getCollectionDetail(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        slug = fields.Str(required=False)
         
    
    class deleteCollection(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class updateCollection(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class addCollectionItems(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class getCollectionItems(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        sort_on = fields.Str(required=False)
        
        page_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getCatalogInsights(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        brand = fields.Str(required=False)
         
    
    class getSellerInsights(Schema):
        
        company_id = fields.Str(required=False)
        
        seller_app_id = fields.Str(required=False)
         
    
    class createMarketplaceOptin(Schema):
        
        company_id = fields.Int(required=False)
        
        marketplace = fields.Str(required=False)
         
    
    class getMarketplaceOptinDetail(Schema):
        
        company_id = fields.Int(required=False)
         
    
    class getCompanyDetail(Schema):
        
        company_id = fields.Int(required=False)
         
    
    class getCompanyBrandDetail(Schema):
        
        company_id = fields.Int(required=False)
        
        is_active = fields.Boolean(required=False)
        
        q = fields.Boolean(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        marketplace = fields.Str(required=False)
         
    
    class getCompanyMetrics(Schema):
        
        company_id = fields.Int(required=False)
         
    
    class getStoreDetail(Schema):
        
        company_id = fields.Int(required=False)
        
        q = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getGenderAttribute(Schema):
        
        company_id = fields.Int(required=False)
        
        attribute_slug = fields.Str(required=False)
         
    
    class listProductTemplateCategories(Schema):
        
        company_id = fields.Str(required=False)
        
        departments = fields.Str(required=False)
        
        item_type = fields.Str(required=False)
         
    
    class listDepartmentsData(Schema):
        
        company_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        name = fields.Str(required=False)
        
        search = fields.Str(required=False)
        
        is_active = fields.Boolean(required=False)
         
    
    class getDepartmentData(Schema):
        
        company_id = fields.Str(required=False)
        
        uid = fields.Str(required=False)
         
    
    class listProductTemplate(Schema):
        
        company_id = fields.Str(required=False)
        
        department = fields.Str(required=False)
         
    
    class validateProductTemplate(Schema):
        
        company_id = fields.Str(required=False)
        
        slug = fields.Str(required=False)
         
    
    class downloadProductTemplateViews(Schema):
        
        company_id = fields.Str(required=False)
        
        slug = fields.Str(required=False)
         
    
    class downloadProductTemplateView(Schema):
        
        company_id = fields.Str(required=False)
        
        item_type = fields.Str(required=False)
         
    
    class validateProductTemplateSchema(Schema):
        
        company_id = fields.Str(required=False)
        
        item_type = fields.Str(required=False)
         
    
    class listHSNCodes(Schema):
        
        company_id = fields.Str(required=False)
         
    
    class listProductTemplateExportDetails(Schema):
        
        company_id = fields.Str(required=False)
         
    
    class listTemplateBrandTypeValues(Schema):
        
        company_id = fields.Str(required=False)
        
        filter = fields.Str(required=False)
         
    
    class createCategories(Schema):
        
        company_id = fields.Str(required=False)
         
    
    class listCategories(Schema):
        
        company_id = fields.Str(required=False)
        
        level = fields.Str(required=False)
        
        departments = fields.Str(required=False)
        
        q = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class updateCategory(Schema):
        
        company_id = fields.Str(required=False)
        
        uid = fields.Str(required=False)
         
    
    class getCategoryData(Schema):
        
        company_id = fields.Str(required=False)
        
        uid = fields.Str(required=False)
         
    
    class createProduct(Schema):
        
        company_id = fields.Str(required=False)
         
    
    class getProducts(Schema):
        
        company_id = fields.Int(required=False)
        
        brand_ids = fields.List(fields.Int(required=False), required=False)
        
        category_ids = fields.List(fields.Int(required=False), required=False)
        
        item_ids = fields.List(fields.Int(required=False), required=False)
        
        department_ids = fields.List(fields.Int(required=False), required=False)
        
        item_code = fields.List(fields.Float(required=False), required=False)
        
        q = fields.Str(required=False)
        
        tags = fields.List(fields.Str(required=False), required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class deleteProduct(Schema):
        
        company_id = fields.Str(required=False)
        
        item_id = fields.Int(required=False)
         
    
    class editProduct(Schema):
        
        company_id = fields.Str(required=False)
        
        item_id = fields.Int(required=False)
         
    
    class getProduct(Schema):
        
        item_code = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        item_id = fields.Int(required=False)
        
        brand_uid = fields.Int(required=False)
         
    
    class getProductValidation(Schema):
        
        company_id = fields.Int(required=False)
         
    
    class getProductSize(Schema):
        
        item_code = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        item_id = fields.Int(required=False)
        
        brand_uid = fields.Int(required=False)
        
        uid = fields.Int(required=False)
         
    
    class updateProductAssetsInBulk(Schema):
        
        company_id = fields.Int(required=False)
         
    
    class getProductBulkUploadHistory(Schema):
        
        company_id = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class deleteProductBulkJob(Schema):
        
        company_id = fields.Str(required=False)
        
        batch_id = fields.Int(required=False)
         
    
    class createProductsInBulk(Schema):
        
        company_id = fields.Int(required=False)
        
        batch_id = fields.Str(required=False)
         
    
    class getProductTags(Schema):
        
        company_id = fields.Int(required=False)
         
    
    class createProductAssetsInBulk(Schema):
        
        company_id = fields.Int(required=False)
         
    
    class getProductAssetsInBulk(Schema):
        
        company_id = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class deleteSize(Schema):
        
        company_id = fields.Str(required=False)
        
        item_id = fields.Int(required=False)
        
        size = fields.Int(required=False)
         
    
    class addInventory(Schema):
        
        company_id = fields.Str(required=False)
        
        item_id = fields.Float(required=False)
        
        size = fields.Str(required=False)
         
    
    class getInventoryBySize(Schema):
        
        company_id = fields.Str(required=False)
        
        item_id = fields.Str(required=False)
        
        size = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
        
        sellable = fields.Boolean(required=False)
         
    
    class getInventoryBySizeIdentifier(Schema):
        
        company_id = fields.Str(required=False)
        
        item_id = fields.Str(required=False)
        
        size_identifier = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
        
        location_ids = fields.List(fields.Int(required=False), required=False)
         
    
    class deleteInventory(Schema):
        
        company_id = fields.Str(required=False)
        
        size = fields.Str(required=False)
        
        item_id = fields.Int(required=False)
        
        location_id = fields.Float(required=False)
         
    
    class createBulkInventoryJob(Schema):
        
        company_id = fields.Int(required=False)
         
    
    class getInventoryBulkUploadHistory(Schema):
        
        company_id = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class deleteBulkInventoryJob(Schema):
        
        company_id = fields.Str(required=False)
        
        batch_id = fields.Str(required=False)
         
    
    class createBulkInventory(Schema):
        
        company_id = fields.Int(required=False)
        
        batch_id = fields.Str(required=False)
         
    
    class createInventoryExportJob(Schema):
        
        company_id = fields.Int(required=False)
         
    
    class getInventoryExport(Schema):
        
        company_id = fields.Int(required=False)
         
    
    class exportInventoryConfig(Schema):
        
        company_id = fields.Str(required=False)
        
        filter_type = fields.Str(required=False)
         
    
    class createHsnCode(Schema):
        
        company_id = fields.Str(required=False)
         
    
    class getAllHsnCodes(Schema):
        
        company_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
         
    
    class updateHsnCode(Schema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class getHsnCode(Schema):
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class bulkHsnCode(Schema):
        
        company_id = fields.Str(required=False)
         
    
    class getApplicationBrands(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        department = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
    
    class getDepartments(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getCategories(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        department = fields.Str(required=False)
         
    
    class getAppicationProducts(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        q = fields.Str(required=False)
        
        f = fields.Str(required=False)
        
        filters = fields.Boolean(required=False)
        
        sort_on = fields.Str(required=False)
        
        page_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_type = fields.Str(required=False)
        
        item_ids = fields.List(fields.Int(required=False), required=False)
         
    
    class getProductDetailBySlug(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        slug = fields.Str(required=False)
         
    
    class getAppProducts(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        brand_ids = fields.List(fields.Int(required=False), required=False)
        
        category_ids = fields.List(fields.Int(required=False), required=False)
        
        department_ids = fields.List(fields.Int(required=False), required=False)
        
        tags = fields.List(fields.Str(required=False), required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
         
    
    class getOptimalLocations(Schema):
        
        company_id = fields.Str(required=False)
         
    