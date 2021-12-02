"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema



from .TatReqProductArticles import TatReqProductArticles




class LocationDetailsReq(BaseSchema):

    
    from_pincode = fields.Str(required=False)
    
    articles = fields.List(fields.Nested(TatReqProductArticles, required=False), required=False)
    
    fulfillment_id = fields.Int(required=False)
    

