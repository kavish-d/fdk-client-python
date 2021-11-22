"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .Address import Address


class GetAddressesResponse(Schema):

    
    address = fields.List(fields.Nested(Address, required=False), required=False)
    

