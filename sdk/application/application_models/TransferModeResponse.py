"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .TransferModeDetails import TransferModeDetails


class TransferModeResponse(Schema):

    
    data = fields.List(fields.Nested(TransferModeDetails, required=False), required=False)
    

