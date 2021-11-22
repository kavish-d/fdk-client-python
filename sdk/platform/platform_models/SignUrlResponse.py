"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .Urls import Urls


class SignUrlResponse(Schema):

    
    urls = fields.List(fields.Nested(Urls, required=False), required=False)
    

