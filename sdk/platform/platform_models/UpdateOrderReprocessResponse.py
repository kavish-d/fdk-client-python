"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class UpdateOrderReprocessResponse(Schema):

    
    status = fields.Str(required=False)
    

