"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .InvSize import InvSize



from .ItemQuery import ItemQuery


class InventoryRequest(BaseSchema):

    
    sizes = fields.List(fields.Nested(InvSize, required=False), required=False)
    
    company_id = fields.Int(required=False)
    
    item = fields.Nested(ItemQuery, required=False)
    

