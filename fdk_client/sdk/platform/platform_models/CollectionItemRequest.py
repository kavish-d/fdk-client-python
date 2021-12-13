"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class CollectionItemRequest(BaseSchema):

    
    page_size = fields.Int(required=False)
    
    page_no = fields.Int(required=False)
    

