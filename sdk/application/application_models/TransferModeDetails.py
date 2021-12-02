"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema



from .TransferItemsDetails import TransferItemsDetails


class TransferModeDetails(BaseSchema):

    
    display_name = fields.Str(required=False)
    
    items = fields.List(fields.Nested(TransferItemsDetails, required=False), required=False)
    

