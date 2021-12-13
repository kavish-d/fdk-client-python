"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema



from .Document import Document



from .LocationManagerSerializer import LocationManagerSerializer



from .SellerPhoneNumber import SellerPhoneNumber







from .LocationDayWiseSerializer import LocationDayWiseSerializer

from .GetAddressSerializer1 import GetAddressSerializer1

from .ProductReturnConfigSerializer import ProductReturnConfigSerializer









from .InvoiceDetailsSerializer import InvoiceDetailsSerializer


class LocationSerializer(BaseSchema):

    
    name = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    warnings = fields.Dict(required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    stage = fields.Str(required=False)
    
    store_type = fields.Str(required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    address = fields.Nested(GetAddressSerializer1, required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    company = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    

