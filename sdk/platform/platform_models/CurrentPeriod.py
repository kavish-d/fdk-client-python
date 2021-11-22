"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class CurrentPeriod(Schema):

    
    start_date = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    

