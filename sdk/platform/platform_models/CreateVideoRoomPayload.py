"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema



from .NotifyUser import NotifyUser


class CreateVideoRoomPayload(BaseSchema):

    
    unique_name = fields.Str(required=False)
    
    notify = fields.List(fields.Nested(NotifyUser, required=False), required=False)
    

