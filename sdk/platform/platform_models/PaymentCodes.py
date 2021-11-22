"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .PaymentModes import PaymentModes

from .PaymentModes import PaymentModes

from .PaymentModes import PaymentModes

from .PaymentModes import PaymentModes

from .PaymentModes import PaymentModes

from .PaymentModes import PaymentModes

from .PaymentModes import PaymentModes

from .PaymentModes import PaymentModes

from .PaymentModes import PaymentModes

from .PaymentModes import PaymentModes


class PaymentCodes(Schema):

    
    rupifipg = fields.Nested(PaymentModes, required=False)
    
    upi = fields.Nested(PaymentModes, required=False)
    
    nb = fields.Nested(PaymentModes, required=False)
    
    pl = fields.Nested(PaymentModes, required=False)
    
    simpl = fields.Nested(PaymentModes, required=False)
    
    stripepg = fields.Nested(PaymentModes, required=False)
    
    qr = fields.Nested(PaymentModes, required=False)
    
    card = fields.Nested(PaymentModes, required=False)
    
    ps = fields.Nested(PaymentModes, required=False)
    
    wl = fields.Nested(PaymentModes, required=False)
    

