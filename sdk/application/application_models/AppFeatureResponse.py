"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .AppFeature import AppFeature


class AppFeatureResponse(BaseSchema):

    
    feature = fields.Nested(AppFeature, required=False)
    

