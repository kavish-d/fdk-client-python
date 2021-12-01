"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema



from .DataShipmentAddress import DataShipmentAddress




class GetShipmentAddressResponse(BaseSchema):

    
    message = fields.Str(required=False)
    
    data = fields.Nested(DataShipmentAddress, required=False)
    
    success = fields.Boolean(required=False)
    

