"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .PickupStoreDetail import PickupStoreDetail


class StoreDetailsResponse(Schema):

    
    items = fields.List(fields.Nested(PickupStoreDetail, required=False), required=False)
    

