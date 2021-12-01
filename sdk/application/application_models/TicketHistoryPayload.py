"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class TicketHistoryPayload(BaseSchema):

    
    value = fields.Dict(required=False)
    
    type = fields.Str(required=False, validate=OneOf(HistoryTypeEnum.__members__.keys()))
    

