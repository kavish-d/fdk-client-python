"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class CollectionItemRequest(Schema):

    
    page_size = fields.Int(required=False)
    
    page_no = fields.Int(required=False)
    

