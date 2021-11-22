"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class UpdateRefundTransferModeResponse(Schema):

    
    success = fields.Boolean(required=False)
    

