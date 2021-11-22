"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .SystemNotification import SystemNotification



from .Page import Page


class SystemNotifications(Schema):

    
    items = fields.List(fields.Nested(SystemNotification, required=False), required=False)
    
    last_read_anchor = fields.Int(required=False)
    
    page = fields.Nested(Page, required=False)
    

