"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .FyndRewardsCredentials import FyndRewardsCredentials


class FyndRewards(BaseSchema):

    
    credentials = fields.Nested(FyndRewardsCredentials, required=False)
    

