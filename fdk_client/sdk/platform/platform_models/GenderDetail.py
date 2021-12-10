"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .AttributeMasterDetails import AttributeMasterDetails











from .AttributeMasterMeta import AttributeMasterMeta

from .AttributeMasterFilter import AttributeMasterFilter







from .AttributeMaster import AttributeMaster


class GenderDetail(BaseSchema):

    
    details = fields.Nested(AttributeMasterDetails, required=False)
    
    description = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    enabled_for_end_consumer = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    meta = fields.Nested(AttributeMasterMeta, required=False)
    
    filters = fields.Nested(AttributeMasterFilter, required=False)
    
    logo = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    is_nested = fields.Boolean(required=False)
    
    schema = fields.Nested(AttributeMaster, required=False)
    

