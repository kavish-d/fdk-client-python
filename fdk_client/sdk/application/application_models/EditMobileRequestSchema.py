"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class EditMobileRequestSchema(BaseSchema):

    
    country_code = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
