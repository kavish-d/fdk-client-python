"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .GoogleMapCredentials import GoogleMapCredentials


class GoogleMap(BaseSchema):

    
    credentials = fields.Nested(GoogleMapCredentials, required=False)
    

