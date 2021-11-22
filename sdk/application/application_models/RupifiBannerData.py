"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class RupifiBannerData(Schema):

    
    kyc_url = fields.Str(required=False)
    
    status = fields.Str(required=False)
    

