"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class EditMobileRequestSchema(BaseSchema):

    
    country_code = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    

