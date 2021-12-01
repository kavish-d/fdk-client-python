"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class CurrentPeriod(BaseSchema):

    
    start_date = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    

