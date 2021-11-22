"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *



from .Destination import Destination

from .ReqConfiguration import ReqConfiguration


class BulkRequest(Schema):

    
    urls = fields.List(fields.Str(required=False), required=False)
    
    destination = fields.Nested(Destination, required=False)
    
    configuration = fields.Nested(ReqConfiguration, required=False)
    

