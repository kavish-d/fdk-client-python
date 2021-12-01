"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .CommunicationConsentChannelsEmail import CommunicationConsentChannelsEmail

from .CommunicationConsentChannelsSms import CommunicationConsentChannelsSms

from .CommunicationConsentChannelsWhatsapp import CommunicationConsentChannelsWhatsapp


class CommunicationConsentChannels(BaseSchema):

    
    email = fields.Nested(CommunicationConsentChannelsEmail, required=False)
    
    sms = fields.Nested(CommunicationConsentChannelsSms, required=False)
    
    whatsapp = fields.Nested(CommunicationConsentChannelsWhatsapp, required=False)
    

