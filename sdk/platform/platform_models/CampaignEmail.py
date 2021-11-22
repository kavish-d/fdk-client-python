"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .CampaignEmailTemplate import CampaignEmailTemplate

from .CampignEmailProvider import CampignEmailProvider


class CampaignEmail(Schema):

    
    template = fields.Nested(CampaignEmailTemplate, required=False)
    
    provider = fields.Nested(CampignEmailProvider, required=False)
    

