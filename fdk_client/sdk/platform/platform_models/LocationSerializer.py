"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .InvoiceDetailsSerializer import InvoiceDetailsSerializer



from .SellerPhoneNumber import SellerPhoneNumber

from .GetAddressSerializer1 import GetAddressSerializer1



from .ProductReturnConfigSerializer import ProductReturnConfigSerializer

from .LocationManagerSerializer import LocationManagerSerializer

















from .Document import Document

from .LocationDayWiseSerializer import LocationDayWiseSerializer


class LocationSerializer(BaseSchema):

    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    display_name = fields.Str(required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    address = fields.Nested(GetAddressSerializer1, required=False)
    
    stage = fields.Str(required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    uid = fields.Int(required=False)
    
    warnings = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    store_type = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    company = fields.Int(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
