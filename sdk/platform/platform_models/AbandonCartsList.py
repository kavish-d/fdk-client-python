"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .AbandonCartsDetail import AbandonCartsDetail



from .Page import Page


class AbandonCartsList(Schema):

    
    items = fields.List(fields.Nested(AbandonCartsDetail, required=False), required=False)
    
    cart_total = fields.Str(required=False)
    
    page = fields.Nested(Page, required=False)
    

