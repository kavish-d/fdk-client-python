"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class ShipmentDates(Schema):

    
    due_date = fields.Str(required=False)
    

