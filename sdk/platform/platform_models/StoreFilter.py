"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *








class StoreFilter(Schema):

    
    include_tags = fields.List(fields.Str(required=False), required=False)
    
    exclude_tags = fields.List(fields.Str(required=False), required=False)
    
    query = fields.Dict(required=False)
    

