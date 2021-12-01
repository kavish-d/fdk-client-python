"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .PickupStoreDetail import PickupStoreDetail


class StoreDetailsResponse(BaseSchema):

    
    items = fields.List(fields.Nested(PickupStoreDetail, required=False), required=False)
    

