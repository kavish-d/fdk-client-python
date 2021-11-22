"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *



from .DataShipmentAddress import DataShipmentAddress




class GetShipmentAddressResponse(Schema):

    
    message = fields.Str(required=False)
    
    data = fields.Nested(DataShipmentAddress, required=False)
    
    success = fields.Boolean(required=False)
    

