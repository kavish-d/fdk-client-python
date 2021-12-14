"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema





from .AttributeMaster import AttributeMaster

from .AttributeMasterDetails import AttributeMasterDetails

from .AttributeMasterFilter import AttributeMasterFilter













from .AttributeMasterMeta import AttributeMasterMeta


class GenderDetail(BaseSchema):
    # Catalog swagger.json

    
    logo = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    schema = fields.Nested(AttributeMaster, required=False)
    
    details = fields.Nested(AttributeMasterDetails, required=False)
    
    filters = fields.Nested(AttributeMasterFilter, required=False)
    
    enabled_for_end_consumer = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    is_nested = fields.Boolean(required=False)
    
    meta = fields.Nested(AttributeMasterMeta, required=False)
    

