"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class RupifiBannerData(BaseSchema):
    # Payment swagger.json

    
    kyc_url = fields.Str(required=False)
    
    status = fields.Str(required=False)
    

