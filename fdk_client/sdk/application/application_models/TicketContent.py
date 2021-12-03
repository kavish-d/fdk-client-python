"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema





from .TicketAsset import TicketAsset


class TicketContent(BaseSchema):

    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    attachments = fields.List(fields.Nested(TicketAsset, required=False), required=False)
    
