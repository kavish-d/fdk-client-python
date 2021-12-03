"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema








class ProductListingActionPage(BaseSchema):

    
    type = fields.Str(required=False)
    
    params = fields.Dict(required=False)
    
    query = fields.Dict(required=False)
    
