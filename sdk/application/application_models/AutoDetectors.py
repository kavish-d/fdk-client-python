"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .TextDetector import TextDetector


class AutoDetectors(Schema):

    
    text_detector = fields.List(fields.Nested(TextDetector, required=False), required=False)
    

