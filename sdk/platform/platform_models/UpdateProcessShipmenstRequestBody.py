"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class UpdateProcessShipmenstRequestBody(BaseSchema):

    
    shipment_ids = fields.List(fields.Str(required=False), required=False)
    
    expected_status = fields.Str(required=False)
    

