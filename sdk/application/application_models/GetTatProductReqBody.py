"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .LocationDetailsReq import LocationDetailsReq






class GetTatProductReqBody(Schema):

    
    location_details = fields.List(fields.Nested(LocationDetailsReq, required=False), required=False)
    
    to_pincode = fields.Str(required=False)
    
    action = fields.Str(required=False)
    

