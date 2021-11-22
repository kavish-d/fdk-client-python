"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class UpdateShipmentStatusResponse(Schema):

    
    shipments = fields.Dict(required=False)
    
    error_shipments = fields.List(fields.Raw(required=False), required=False)
    

