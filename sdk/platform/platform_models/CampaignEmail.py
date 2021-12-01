"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .CampaignEmailTemplate import CampaignEmailTemplate

from .CampignEmailProvider import CampignEmailProvider


class CampaignEmail(BaseSchema):

    
    template = fields.Nested(CampaignEmailTemplate, required=False)
    
    provider = fields.Nested(CampignEmailProvider, required=False)
    

