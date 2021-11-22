"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class StatusesBody(Schema):

    
    status = fields.Str(required=False)
    
    shipments = fields.Dict(required=False)
    

