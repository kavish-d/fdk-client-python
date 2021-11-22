"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *



from .TatReqProductArticles import TatReqProductArticles




class LocationDetailsReq(Schema):

    
    from_pincode = fields.Str(required=False)
    
    articles = fields.List(fields.Nested(TatReqProductArticles, required=False), required=False)
    
    fulfillment_id = fields.Int(required=False)
    

