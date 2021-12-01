"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class UpdateShipmentStatusResponse(BaseSchema):

    
    shipments = fields.Dict(required=False)
    
    error_shipments = fields.List(fields.Raw(required=False), required=False)
    

