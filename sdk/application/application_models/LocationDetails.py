"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *



from .TatProductArticles import TatProductArticles




class LocationDetails(Schema):

    
    from_pincode = fields.Str(required=False)
    
    articles = fields.List(fields.Nested(TatProductArticles, required=False), required=False)
    
    fulfillment_id = fields.Int(required=False)
    

