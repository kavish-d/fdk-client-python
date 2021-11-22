"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class UpdateRefundTransferModeRequest(Schema):

    
    transfer_mode = fields.Str(required=False)
    
    enable = fields.Boolean(required=False)
    

