"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .Offer import Offer



from .ShareMessages import ShareMessages

from .ReferralDetailsUser import ReferralDetailsUser


class ReferralDetailsResponse(Schema):

    
    referral = fields.Nested(Offer, required=False)
    
    referrer_info = fields.Str(required=False)
    
    share = fields.Nested(ShareMessages, required=False)
    
    user = fields.Nested(ReferralDetailsUser, required=False)
    

