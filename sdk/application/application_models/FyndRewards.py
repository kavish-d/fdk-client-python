"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .FyndRewardsCredentials import FyndRewardsCredentials


class FyndRewards(Schema):

    
    credentials = fields.Nested(FyndRewardsCredentials, required=False)
    

