"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .StatusesBody import StatusesBody




class ShipmentStatusUpdateBody(Schema):

    
    statuses = fields.List(fields.Nested(StatusesBody, required=False), required=False)
    
    force_transition = fields.Boolean(required=False)
    

