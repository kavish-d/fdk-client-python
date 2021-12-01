"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class UpdateRefundTransferModeRequest(BaseSchema):

    
    enable = fields.Boolean(required=False)
    
    transfer_mode = fields.Str(required=False)
    

