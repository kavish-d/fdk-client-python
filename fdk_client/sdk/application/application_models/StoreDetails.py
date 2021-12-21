"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema



from .StoreTiming import StoreTiming



from .SellerPhoneNumber import SellerPhoneNumber



from .StoreAddressSerializer import StoreAddressSerializer

from .StoreDepartments import StoreDepartments

from .CompanyStore import CompanyStore

from .StoreManagerSerializer import StoreManagerSerializer


class StoreDetails(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    timing = fields.List(fields.Nested(StoreTiming, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    name = fields.Str(required=False)
    
    address = fields.Nested(StoreAddressSerializer, required=False)
    
    departments = fields.List(fields.Nested(StoreDepartments, required=False), required=False)
    
    company = fields.Nested(CompanyStore, required=False)
    
    manager = fields.Nested(StoreManagerSerializer, required=False)
    

