"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema



from .ItemQuery import ItemQuery

from .InvSize import InvSize


class InventoryRequest(BaseSchema):

    
    company_id = fields.Int(required=False)
    
    item = fields.Nested(ItemQuery, required=False)
    
    sizes = fields.List(fields.Nested(InvSize, required=False), required=False)
    

