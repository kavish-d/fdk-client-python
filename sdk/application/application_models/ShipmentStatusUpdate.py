"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class ShipmentStatusUpdate(Schema):

    
    message = fields.List(fields.Dict(required=False), required=False)
    
    status = fields.Boolean(required=False)
    

