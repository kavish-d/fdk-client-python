"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *



from .Charges import Charges


class DeliveryCharges(Schema):

    
    enabled = fields.Boolean(required=False)
    
    charges = fields.Nested(Charges, required=False)
    

