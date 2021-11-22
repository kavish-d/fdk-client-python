"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .Results import Results


class PlatformShipmentTrack(Schema):

    
    results = fields.Nested(Results, required=False)
    

