"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .KeyValue import KeyValue

from .TicketAsset import TicketAsset


class CustomFormSubmissionPayload(BaseSchema):

    
    response = fields.List(fields.Nested(KeyValue, required=False), required=False)
    
    attachments = fields.List(fields.Nested(TicketAsset, required=False), required=False)
    

