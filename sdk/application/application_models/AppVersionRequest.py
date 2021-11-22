"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .ApplicationVersionRequest import ApplicationVersionRequest

from .Device import Device






class AppVersionRequest(Schema):

    
    application = fields.Nested(ApplicationVersionRequest, required=False)
    
    device = fields.Nested(Device, required=False)
    
    locale = fields.Str(required=False)
    
    timezone = fields.Str(required=False)
    

