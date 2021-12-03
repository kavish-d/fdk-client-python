"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .LogisticTimestamp import LogisticTimestamp

from .Formatted import Formatted


class LogisticPromise(BaseSchema):

    
    timestamp = fields.Nested(LogisticTimestamp, required=False)
    
    formatted = fields.Nested(Formatted, required=False)
    
