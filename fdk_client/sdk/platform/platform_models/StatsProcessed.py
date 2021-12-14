"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .StatsProcessedEmail import StatsProcessedEmail

from .StatsProcessedSms import StatsProcessedSms


class StatsProcessed(BaseSchema):
    # Communication swagger.json

    
    email = fields.Nested(StatsProcessedEmail, required=False)
    
    sms = fields.Nested(StatsProcessedSms, required=False)
    

