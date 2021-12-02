"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .GetCompanySerializer import GetCompanySerializer

from .UserSerializer1 import UserSerializer1



from .UserSerializer1 import UserSerializer1

from .UserSerializer1 import UserSerializer1







from .GetBrandResponseSerializer import GetBrandResponseSerializer








class CompanyBrandSerializer(BaseSchema):

    
    company = fields.Nested(GetCompanySerializer, required=False)
    
    created_by = fields.Nested(UserSerializer1, required=False)
    
    created_on = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer1, required=False)
    
    verified_by = fields.Nested(UserSerializer1, required=False)
    
    warnings = fields.Dict(required=False)
    
    uid = fields.Int(required=False)
    
    verified_on = fields.Str(required=False)
    
    brand = fields.Nested(GetBrandResponseSerializer, required=False)
    
    stage = fields.Str(required=False)
    
    reject_reason = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    

