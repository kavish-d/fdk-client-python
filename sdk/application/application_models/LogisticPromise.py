"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .LogisticTimestamp import LogisticTimestamp

from .Formatted import Formatted


class LogisticPromise(Schema):

    
    timestamp = fields.Nested(LogisticTimestamp, required=False)
    
    formatted = fields.Nested(Formatted, required=False)
    

