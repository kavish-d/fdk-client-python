"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .NotAvailable import NotAvailable

from .Sellable import Sellable

from .OrderCommitted import OrderCommitted

from .Damaged import Damaged


class Quantities(Schema):

    
    not_available = fields.Nested(NotAvailable, required=False)
    
    sellable = fields.Nested(Sellable, required=False)
    
    order_committed = fields.Nested(OrderCommitted, required=False)
    
    damaged = fields.Nested(Damaged, required=False)
    

