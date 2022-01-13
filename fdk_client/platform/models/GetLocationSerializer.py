"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .ProductReturnConfigSerializer import ProductReturnConfigSerializer



from .LocationManagerSerializer import LocationManagerSerializer









from .SellerPhoneNumber import SellerPhoneNumber





from .GetCompanySerializer import GetCompanySerializer



from .UserSerializer1 import UserSerializer1



from .InvoiceDetailsSerializer import InvoiceDetailsSerializer

from .UserSerializer1 import UserSerializer1



from .Document import Document



from .LocationIntegrationType import LocationIntegrationType

from .LocationDayWiseSerializer import LocationDayWiseSerializer

from .GetAddressSerializer import GetAddressSerializer

from .UserSerializer1 import UserSerializer1


class GetLocationSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    code = fields.Str(required=False)
    
    store_type = fields.Str(required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    modified_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    stage = fields.Str(required=False)
    
    company = fields.Nested(GetCompanySerializer, required=False)
    
    phone_number = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer1, required=False)
    
    warnings = fields.Dict(required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    verified_by = fields.Nested(UserSerializer1, required=False)
    
    display_name = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    verified_on = fields.Str(required=False)
    
    integration_type = fields.Nested(LocationIntegrationType, required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    created_by = fields.Nested(UserSerializer1, required=False)
    

