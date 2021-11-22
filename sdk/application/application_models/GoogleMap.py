"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .GoogleMapCredentials import GoogleMapCredentials


class GoogleMap(Schema):

    
    credentials = fields.Nested(GoogleMapCredentials, required=False)
    

