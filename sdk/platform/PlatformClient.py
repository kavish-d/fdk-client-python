"""Platform Client."""

import base64

from .PlatformApplicationClient import PlatformApplicationClient
from ..common.aiohttp_helper import AiohttpHelper
from ..common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .platform_models.CommonValidator import CommonValidator
from .platform_models.LeadValidator import LeadValidator
from .platform_models.FeedbackValidator import FeedbackValidator
from .platform_models.ThemeValidator import ThemeValidator
from .platform_models.UserValidator import UserValidator
from .platform_models.ContentValidator import ContentValidator
from .platform_models.BillingValidator import BillingValidator
from .platform_models.CommunicationValidator import CommunicationValidator
from .platform_models.PaymentValidator import PaymentValidator
from .platform_models.OrderValidator import OrderValidator
from .platform_models.CatalogValidator import CatalogValidator
from .platform_models.CompanyProfileValidator import CompanyProfileValidator
from .platform_models.FileStorageValidator import FileStorageValidator
from .platform_models.ShareValidator import ShareValidator
from .platform_models.InventoryValidator import InventoryValidator
from .platform_models.ConfigurationValidator import ConfigurationValidator
from .platform_models.CartValidator import CartValidator
from .platform_models.RewardsValidator import RewardsValidator
from .platform_models.AnalyticsValidator import AnalyticsValidator
from .platform_models.DiscountValidator import DiscountValidator
from .platform_models.PartnerValidator import PartnerValidator
from .platform_models.WebhookValidator import WebhookValidator



class Common:
    def __init__(self, config):
        self._conf = config
    # async def ():
    
    async def getLocations(self, location_type=None, id=None, body=""):
        """
        :param location_type : Provide location type to query on. Possible values : country, state, city : type string
        :param id : Field is optional when location_type is country. If querying for state, provide id of country. If querying for city, provide id of state. : type string
        """
        payload = {}
        
        if location_type:
            payload["location_type"] = location_type
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommonValidator.getLocations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/common/configuration/v1.0/location", """{"required":[],"optional":[{"in":"query","name":"location_type","schema":{"type":"string","enum":["country","state","city"]},"description":"Provide location type to query on. Possible values : country, state, city"},{"in":"query","name":"id","schema":{"type":"string"},"description":"Field is optional when location_type is country. If querying for state, provide id of country. If querying for city, provide id of state."}],"query":[{"in":"query","name":"location_type","schema":{"type":"string","enum":["country","state","city"]},"description":"Provide location type to query on. Possible values : country, state, city"},{"in":"query","name":"id","schema":{"type":"string"},"description":"Field is optional when location_type is country. If querying for state, provide id of country. If querying for city, provide id of state."}],"headers":[]}""", location_type=location_type, id=id)
        query_string = await create_query_string(location_type=location_type, id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/common/configuration/v1.0/location", location_type=location_type, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    

class Lead:
    def __init__(self, config):
        self._conf = config
    # async def ():
    
    async def getTickets(self, company_id=None, items=None, filters=None, q=None, status=None, priority=None, category=None, page_no=None, page_size=None, body=""):
        """Gets the list of company level tickets and/or ticket filters
        :param company_id : Company ID for which the data will be returned : type string
        :param items : Decides that the reponse will contain the list of tickets : type boolean
        :param filters : Decides that the reponse will contain the ticket filters : type boolean
        :param q : Search through ticket titles and description : type string
        :param status : Filter tickets on status : type string
        :param priority : Filter tickets on priority : type 
        :param category : Filter tickets on category : type string
        :param page_no : The page number to navigate through the given set of results. : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if items:
            payload["items"] = items
        
        if filters:
            payload["filters"] = filters
        
        if q:
            payload["q"] = q
        
        if status:
            payload["status"] = status
        
        if priority:
            payload["priority"] = priority
        
        if category:
            payload["category"] = category
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = LeadValidator.getTickets()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/lead/v1.0/company/{company_id}/ticket", """{"required":[{"name":"company_id","in":"path","description":"Company ID for which the data will be returned","required":true,"schema":{"type":"string"}}],"optional":[{"name":"items","in":"query","description":"Decides that the reponse will contain the list of tickets","schema":{"type":"boolean"}},{"name":"filters","in":"query","description":"Decides that the reponse will contain the ticket filters","schema":{"type":"boolean"}},{"name":"q","in":"query","description":"Search through ticket titles and description","schema":{"type":"string"}},{"name":"status","in":"query","description":"Filter tickets on status","schema":{"type":"string"}},{"name":"priority","in":"query","description":"Filter tickets on priority","schema":{"$ref":"#/components/schemas/PriorityEnum"}},{"name":"category","in":"query","description":"Filter tickets on category","schema":{"type":"string"}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results.","schema":{"type":"integer"},"required":false},{"name":"page_size","in":"query","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false}],"query":[{"name":"items","in":"query","description":"Decides that the reponse will contain the list of tickets","schema":{"type":"boolean"}},{"name":"filters","in":"query","description":"Decides that the reponse will contain the ticket filters","schema":{"type":"boolean"}},{"name":"q","in":"query","description":"Search through ticket titles and description","schema":{"type":"string"}},{"name":"status","in":"query","description":"Filter tickets on status","schema":{"type":"string"}},{"name":"priority","in":"query","description":"Filter tickets on priority","schema":{"$ref":"#/components/schemas/PriorityEnum"}},{"name":"category","in":"query","description":"Filter tickets on category","schema":{"type":"string"}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results.","schema":{"type":"integer"},"required":false},{"name":"page_size","in":"query","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false}],"headers":[]}""", company_id=company_id, items=items, filters=filters, q=q, status=status, priority=priority, category=category, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(company_id=company_id, items=items, filters=filters, q=q, status=status, priority=priority, category=category, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/lead/v1.0/company/{company_id}/ticket", company_id=company_id, items=items, filters=filters, q=q, status=status, priority=priority, category=category, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createTicket(self, company_id=None, body=""):
        """Creates a company level ticket
        :param company_id : Company ID for which the data will be returned : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = LeadValidator.createTicket()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.AddTicketPayload import AddTicketPayload
        schema = AddTicketPayload()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/lead/v1.0/company/{company_id}/ticket", """{"required":[{"name":"company_id","in":"path","description":"Company ID for which the data will be returned","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/lead/v1.0/company/{company_id}/ticket", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getTickets(self, company_id=None, application_id=None, items=None, filters=None, q=None, status=None, priority=None, category=None, body=""):
        """Gets the list of Application level Tickets and/or ticket filters
        :param company_id : Company ID of the application : type string
        :param application_id : Application ID for which the data will be returned : type string
        :param items : Decides that the reponse will contain the list of tickets : type boolean
        :param filters : Decides that the reponse will contain the ticket filters : type boolean
        :param q : Search through ticket titles and description : type string
        :param status : Filter tickets on status : type string
        :param priority : Filter tickets on priority : type 
        :param category : Filter tickets on category : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if items:
            payload["items"] = items
        
        if filters:
            payload["filters"] = filters
        
        if q:
            payload["q"] = q
        
        if status:
            payload["status"] = status
        
        if priority:
            payload["priority"] = priority
        
        if category:
            payload["category"] = category
        

        # Parameter validation
        schema = LeadValidator.getTickets()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/lead/v1.0/company/{company_id}/application/{application_id}/ticket", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for which the data will be returned","required":true,"schema":{"type":"string"}}],"optional":[{"name":"items","in":"query","description":"Decides that the reponse will contain the list of tickets","schema":{"type":"boolean"}},{"name":"filters","in":"query","description":"Decides that the reponse will contain the ticket filters","schema":{"type":"boolean"}},{"name":"q","in":"query","description":"Search through ticket titles and description","schema":{"type":"string"}},{"name":"status","in":"query","description":"Filter tickets on status","schema":{"type":"string"}},{"name":"priority","in":"query","description":"Filter tickets on priority","schema":{"$ref":"#/components/schemas/PriorityEnum"}},{"name":"category","in":"query","description":"Filter tickets on category","schema":{"type":"string"}}],"query":[{"name":"items","in":"query","description":"Decides that the reponse will contain the list of tickets","schema":{"type":"boolean"}},{"name":"filters","in":"query","description":"Decides that the reponse will contain the ticket filters","schema":{"type":"boolean"}},{"name":"q","in":"query","description":"Search through ticket titles and description","schema":{"type":"string"}},{"name":"status","in":"query","description":"Filter tickets on status","schema":{"type":"string"}},{"name":"priority","in":"query","description":"Filter tickets on priority","schema":{"$ref":"#/components/schemas/PriorityEnum"}},{"name":"category","in":"query","description":"Filter tickets on category","schema":{"type":"string"}}],"headers":[]}""", company_id=company_id, application_id=application_id, items=items, filters=filters, q=q, status=status, priority=priority, category=category)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, items=items, filters=filters, q=q, status=status, priority=priority, category=category)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/lead/v1.0/company/{company_id}/application/{application_id}/ticket", company_id=company_id, application_id=application_id, items=items, filters=filters, q=q, status=status, priority=priority, category=category), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getTicket(self, company_id=None, id=None, body=""):
        """Retreives ticket details of a company level ticket
        :param company_id : Company ID for which the data will be returned : type string
        :param id : Tiket ID of the ticket to be fetched : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = LeadValidator.getTicket()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/lead/v1.0/company/{company_id}/ticket/{id}", """{"required":[{"name":"company_id","in":"path","description":"Company ID for which the data will be returned","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Tiket ID of the ticket to be fetched","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, id=id)
        query_string = await create_query_string(company_id=company_id, id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/lead/v1.0/company/{company_id}/ticket/{id}", company_id=company_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def editTicket(self, company_id=None, id=None, body=""):
        """Edits ticket details of a company level ticket such as status, priority, category, tags, attachments, assigne & ticket content changes
        :param company_id : Company ID for ticket : type string
        :param id : Ticket ID of ticket to be edited : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = LeadValidator.editTicket()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.EditTicketPayload import EditTicketPayload
        schema = EditTicketPayload()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/lead/v1.0/company/{company_id}/ticket/{id}", """{"required":[{"name":"company_id","in":"path","description":"Company ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID of ticket to be edited","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, id=id)
        query_string = await create_query_string(company_id=company_id, id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/lead/v1.0/company/{company_id}/ticket/{id}", company_id=company_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getTicket(self, company_id=None, application_id=None, id=None, body=""):
        """Retreives ticket details of a application level ticket with ticket ID
        :param company_id : Company ID of the application : type string
        :param application_id : Application ID for which the data will be returned : type string
        :param id : Tiket ID of the ticket to be fetched : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = LeadValidator.getTicket()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/lead/v1.0/company/{company_id}/application/{application_id}/ticket/{id}", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for which the data will be returned","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Tiket ID of the ticket to be fetched","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/lead/v1.0/company/{company_id}/application/{application_id}/ticket/{id}", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def editTicket(self, company_id=None, application_id=None, id=None, body=""):
        """Edits ticket details of a application level ticket such as status, priority, category, tags, attachments, assigne & ticket content changes
        :param company_id : Company ID of the application : type string
        :param application_id : Application ID for ticket : type string
        :param id : Ticket ID of ticket to be edited : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = LeadValidator.editTicket()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.EditTicketPayload import EditTicketPayload
        schema = EditTicketPayload()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/lead/v1.0/company/{company_id}/application/{application_id}/ticket/{id}", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID of ticket to be edited","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/lead/v1.0/company/{company_id}/application/{application_id}/ticket/{id}", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createHistory(self, company_id=None, id=None, body=""):
        """Create history for specific company level ticket, this history is seen on ticket detail page, this can be comment, log or rating.
        :param company_id : Company ID for ticket : type string
        :param id : Ticket ID for which history is created : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = LeadValidator.createHistory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.TicketHistoryPayload import TicketHistoryPayload
        schema = TicketHistoryPayload()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/lead/v1.0/company/{company_id}/ticket/{id}/history", """{"required":[{"name":"company_id","in":"path","description":"Company ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID for which history is created","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, id=id)
        query_string = await create_query_string(company_id=company_id, id=id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/lead/v1.0/company/{company_id}/ticket/{id}/history", company_id=company_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getTicketHistory(self, company_id=None, id=None, body=""):
        """Gets history list for specific company level ticket, this history is seen on ticket detail page, this can be comment, log or rating.
        :param company_id : Company ID for ticket : type string
        :param id : Ticket ID for which history is to be fetched : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = LeadValidator.getTicketHistory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/lead/v1.0/company/{company_id}/ticket/{id}/history", """{"required":[{"name":"company_id","in":"path","description":"Company ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID for which history is to be fetched","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, id=id)
        query_string = await create_query_string(company_id=company_id, id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/lead/v1.0/company/{company_id}/ticket/{id}/history", company_id=company_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getFeedbacks(self, company_id=None, id=None, body=""):
        """Gets a list of feedback submitted against that ticket
        :param company_id : Company ID for ticket : type string
        :param id : Ticket ID for which feedbacks are to be fetched : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = LeadValidator.getFeedbacks()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/lead/v1.0/company/{company_id}/ticket/{id}/feedback", """{"required":[{"name":"company_id","in":"path","description":"Company ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID for which feedbacks are to be fetched","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, id=id)
        query_string = await create_query_string(company_id=company_id, id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/lead/v1.0/company/{company_id}/ticket/{id}/feedback", company_id=company_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def submitFeedback(self, company_id=None, id=None, body=""):
        """Submit a response for feeback form against that ticket
        :param company_id : Company ID for ticket : type string
        :param id : Ticket ID for which feedback is to be submitted : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = LeadValidator.submitFeedback()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.TicketFeedbackPayload import TicketFeedbackPayload
        schema = TicketFeedbackPayload()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/lead/v1.0/company/{company_id}/ticket/{id}/feedback", """{"required":[{"name":"company_id","in":"path","description":"Company ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID for which feedback is to be submitted","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, id=id)
        query_string = await create_query_string(company_id=company_id, id=id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/lead/v1.0/company/{company_id}/ticket/{id}/feedback", company_id=company_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createHistory(self, company_id=None, application_id=None, id=None, body=""):
        """Create history for specific application level ticket, this history is seen on ticket detail page, this can be comment, log or rating.
        :param company_id : Company ID of the application : type string
        :param application_id : Application ID for ticket : type string
        :param id : Ticket ID for which history is created : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = LeadValidator.createHistory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.TicketHistoryPayload import TicketHistoryPayload
        schema = TicketHistoryPayload()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/lead/v1.0/company/{company_id}/application/{application_id}/ticket/{id}/history", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID for which history is created","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/lead/v1.0/company/{company_id}/application/{application_id}/ticket/{id}/history", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getTicketHistory(self, company_id=None, application_id=None, id=None, body=""):
        """Gets history list for specific application level ticket, this history is seen on ticket detail page, this can be comment, log or rating.
        :param company_id : Company ID of application : type string
        :param application_id : Application ID for ticket : type string
        :param id : Ticket ID for which history is to be fetched : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = LeadValidator.getTicketHistory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/lead/v1.0/company/{company_id}/application/{application_id}/ticket/{id}/history", """{"required":[{"name":"company_id","in":"path","description":"Company ID of application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for ticket","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Ticket ID for which history is to be fetched","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/lead/v1.0/company/{company_id}/application/{application_id}/ticket/{id}/history", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getCustomForm(self, company_id=None, application_id=None, slug=None, body=""):
        """Get specific custom form using it's slug, this is used to view the form.
        :param company_id : Company ID of the application : type string
        :param application_id : Application ID for the form : type string
        :param slug : Slug of form whose response is getting submitted : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if slug:
            payload["slug"] = slug
        

        # Parameter validation
        schema = LeadValidator.getCustomForm()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/lead/v1.0/company/{company_id}/application/{application_id}/form/{slug}", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for the form","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"Slug of form whose response is getting submitted","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, slug=slug)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, slug=slug)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/lead/v1.0/company/{company_id}/application/{application_id}/form/{slug}", company_id=company_id, application_id=application_id, slug=slug), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def editCustomForm(self, company_id=None, application_id=None, slug=None, body=""):
        """Edit the given custom form field such as adding or deleting input, assignee, title, decription, notification and polling information.
        :param company_id : Company ID of the application : type string
        :param application_id : Application ID for the form : type string
        :param slug : Slug of form whose response is getting submitted : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if slug:
            payload["slug"] = slug
        

        # Parameter validation
        schema = LeadValidator.editCustomForm()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.EditCustomFormPayload import EditCustomFormPayload
        schema = EditCustomFormPayload()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/lead/v1.0/company/{company_id}/application/{application_id}/form/{slug}", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for the form","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"Slug of form whose response is getting submitted","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, slug=slug)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, slug=slug)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/lead/v1.0/company/{company_id}/application/{application_id}/form/{slug}", company_id=company_id, application_id=application_id, slug=slug), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getCustomForms(self, company_id=None, application_id=None, body=""):
        """Get list of custom form for given application
        :param company_id : Company ID of the application : type string
        :param application_id : Application ID for the form : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = LeadValidator.getCustomForms()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/lead/v1.0/company/{company_id}/application/{application_id}/form", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for the form","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/lead/v1.0/company/{company_id}/application/{application_id}/form", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createCustomForm(self, company_id=None, application_id=None, body=""):
        """Creates a new custom form for given application
        :param company_id : Company ID of the application : type string
        :param application_id : Application ID for the form : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = LeadValidator.createCustomForm()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.CreateCustomFormPayload import CreateCustomFormPayload
        schema = CreateCustomFormPayload()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/lead/v1.0/company/{company_id}/application/{application_id}/form", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for the form","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/lead/v1.0/company/{company_id}/application/{application_id}/form", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getTokenForVideoRoom(self, company_id=None, unique_name=None, body=""):
        """Get Token to join a specific Video Room using it's unqiue name, this Token is your ticket to Room and also creates your identity there.
        :param company_id : Company Id for video room : type string
        :param unique_name : Unique name of video room : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if unique_name:
            payload["unique_name"] = unique_name
        

        # Parameter validation
        schema = LeadValidator.getTokenForVideoRoom()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/lead/v1.0/company/{company_id}/video/room/{unique_name}/token", """{"required":[{"name":"company_id","in":"path","description":"Company Id for video room","required":true,"schema":{"type":"string"}},{"name":"unique_name","in":"path","description":"Unique name of video room","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, unique_name=unique_name)
        query_string = await create_query_string(company_id=company_id, unique_name=unique_name)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/lead/v1.0/company/{company_id}/video/room/{unique_name}/token", company_id=company_id, unique_name=unique_name), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getTokenForVideoRoom(self, company_id=None, application_id=None, unique_name=None, body=""):
        """Get Token to join a specific Video Room using it's unqiue name, this Token is your ticket to Room and also creates your identity there.
        :param company_id : Company ID of the application : type string
        :param application_id : Application ID for video room : type string
        :param unique_name : Unique name of video room : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if unique_name:
            payload["unique_name"] = unique_name
        

        # Parameter validation
        schema = LeadValidator.getTokenForVideoRoom()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/lead/v1.0/company/{company_id}/application/{application_id}/video/room/{unique_name}/token", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for video room","required":true,"schema":{"type":"string"}},{"name":"unique_name","in":"path","description":"Unique name of video room","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, unique_name=unique_name)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, unique_name=unique_name)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/lead/v1.0/company/{company_id}/application/{application_id}/video/room/{unique_name}/token", company_id=company_id, application_id=application_id, unique_name=unique_name), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getVideoParticipants(self, company_id=None, unique_name=None, body=""):
        """Get participants of a specific Video Room using it's unique name, this can be used to check if people are already there in the room and also to show their names.
        :param company_id : Company Id for video room : type string
        :param unique_name : Unique name of Video Room : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if unique_name:
            payload["unique_name"] = unique_name
        

        # Parameter validation
        schema = LeadValidator.getVideoParticipants()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/lead/v1.0/company/{company_id}/video/room/{unique_name}/participants", """{"required":[{"name":"company_id","in":"path","description":"Company Id for video room","required":true,"schema":{"type":"string"}},{"name":"unique_name","in":"path","description":"Unique name of Video Room","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, unique_name=unique_name)
        query_string = await create_query_string(company_id=company_id, unique_name=unique_name)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/lead/v1.0/company/{company_id}/video/room/{unique_name}/participants", company_id=company_id, unique_name=unique_name), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getVideoParticipants(self, company_id=None, application_id=None, unique_name=None, body=""):
        """Get participants of a specific Video Room using it's unique name, this can be used to check if people are already there in the room and also to show their names.
        :param company_id : Company ID of the application : type string
        :param application_id : Application ID for video room : type string
        :param unique_name : Unique name of Video Room : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if unique_name:
            payload["unique_name"] = unique_name
        

        # Parameter validation
        schema = LeadValidator.getVideoParticipants()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/lead/v1.0/company/{company_id}/application/{application_id}/video/room/{unique_name}/participants", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for video room","required":true,"schema":{"type":"string"}},{"name":"unique_name","in":"path","description":"Unique name of Video Room","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, unique_name=unique_name)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, unique_name=unique_name)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/lead/v1.0/company/{company_id}/application/{application_id}/video/room/{unique_name}/participants", company_id=company_id, application_id=application_id, unique_name=unique_name), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def openVideoRoom(self, company_id=None, application_id=None, body=""):
        """Open a video room.
        :param company_id : Company ID of the application : type string
        :param application_id : Application ID for video room : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = LeadValidator.openVideoRoom()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.CreateVideoRoomPayload import CreateVideoRoomPayload
        schema = CreateVideoRoomPayload()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/lead/v1.0/company/{company_id}/application/{application_id}/video/room", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for video room","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/lead/v1.0/company/{company_id}/application/{application_id}/video/room", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def closeVideoRoom(self, company_id=None, application_id=None, unique_name=None, body=""):
        """Close the video room and force all participants to leave.
        :param company_id : Company ID of the application : type string
        :param application_id : Application ID for video room : type string
        :param unique_name : Unique name of Video Room : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if unique_name:
            payload["unique_name"] = unique_name
        

        # Parameter validation
        schema = LeadValidator.closeVideoRoom()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/lead/v1.0/company/{company_id}/application/{application_id}/video/room/{unique_name}", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID for video room","required":true,"schema":{"type":"string"}},{"name":"unique_name","in":"path","description":"Unique name of Video Room","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, unique_name=unique_name)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, unique_name=unique_name)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain("/service/platform/lead/v1.0/company/{company_id}/application/{application_id}/video/room/{unique_name}", company_id=company_id, application_id=application_id, unique_name=unique_name), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    

class Feedback:
    def __init__(self, config):
        self._conf = config
    # async def ():
    
    async def getAttributes(self, company_id=None, application_id=None, page_no=None, page_size=None, body=""):
        """Provides a list of all attribute data.
        :param company_id : company id : type string
        :param application_id : application id : type string
        :param page_no : pagination page no : type integer
        :param page_size : pagination page size : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = FeedbackValidator.getAttributes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/feedback/v1.0/company/{company_id}/application/{application_id}/attributes/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"pagination page no","in":"query","name":"page_no","schema":{"type":"integer"}},{"description":"pagination page size","in":"query","name":"page_size","schema":{"type":"integer"}}],"query":[{"description":"pagination page no","in":"query","name":"page_no","schema":{"type":"integer"}},{"description":"pagination page size","in":"query","name":"page_size","schema":{"type":"integer"}}],"headers":[]}""", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/feedback/v1.0/company/{company_id}/application/{application_id}/attributes/", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getCustomerReviews(self, company_id=None, application_id=None, id=None, entity_id=None, entity_type=None, user_id=None, media=None, rating=None, attribute_rating=None, facets=None, sort=None, next=None, start=None, limit=None, count=None, page_id=None, page_size=None, body=""):
        """The endpoint provides a list of customer reviews based on entity and provided filters
        :param company_id : company id : type string
        :param application_id : application id : type string
        :param id : review id : type string
        :param entity_id : entity id : type string
        :param entity_type : entity type : type string
        :param user_id : user id : type string
        :param media : media type e.g. image | video | video_file | video_link : type string
        :param rating : rating filter, 1-5 : type array
        :param attribute_rating : attribute rating filter with ma,e of attribute : type array
        :param facets : facets (true|false) : type boolean
        :param sort : sort by : default | top | recent : type string
        :param next : pagination next : type string
        :param start : pagination start : type string
        :param limit : pagination limit : type string
        :param count : pagination count : type string
        :param page_id : pagination page id : type string
        :param page_size : pagination page size : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        
        if entity_id:
            payload["entity_id"] = entity_id
        
        if entity_type:
            payload["entity_type"] = entity_type
        
        if user_id:
            payload["user_id"] = user_id
        
        if media:
            payload["media"] = media
        
        if rating:
            payload["rating"] = rating
        
        if attribute_rating:
            payload["attribute_rating"] = attribute_rating
        
        if facets:
            payload["facets"] = facets
        
        if sort:
            payload["sort"] = sort
        
        if next:
            payload["next"] = next
        
        if start:
            payload["start"] = start
        
        if limit:
            payload["limit"] = limit
        
        if count:
            payload["count"] = count
        
        if page_id:
            payload["page_id"] = page_id
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = FeedbackValidator.getCustomerReviews()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/feedback/v1.0/company/{company_id}/application/{application_id}/reviews/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"review id","in":"query","name":"id","schema":{"type":"string"}},{"description":"entity id","in":"query","name":"entity_id","schema":{"type":"string"}},{"description":"entity type","in":"query","name":"entity_type","schema":{"type":"string"}},{"description":"user id","in":"query","name":"user_id","schema":{"type":"string"}},{"description":"media type e.g. image | video | video_file | video_link","in":"query","name":"media","schema":{"type":"string"}},{"description":"rating filter, 1-5","explode":false,"in":"query","name":"rating","schema":{"items":{"type":"number"},"type":"array"},"style":"form"},{"description":"attribute rating filter with ma,e of attribute","explode":false,"in":"query","name":"attribute_rating","schema":{"items":{"type":"string"},"type":"array"},"style":"form"},{"description":"facets (true|false)","in":"query","name":"facets","schema":{"type":"boolean"}},{"description":"sort by : default | top | recent","in":"query","name":"sort","schema":{"type":"string"}},{"description":"pagination next","in":"query","name":"next","schema":{"type":"string"}},{"description":"pagination start","in":"query","name":"start","schema":{"type":"string"}},{"description":"pagination limit","in":"query","name":"limit","schema":{"type":"string"}},{"description":"pagination count","in":"query","name":"count","schema":{"type":"string"}},{"description":"pagination page id","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"pagination page size","in":"query","name":"page_size","schema":{"type":"integer"}}],"query":[{"description":"review id","in":"query","name":"id","schema":{"type":"string"}},{"description":"entity id","in":"query","name":"entity_id","schema":{"type":"string"}},{"description":"entity type","in":"query","name":"entity_type","schema":{"type":"string"}},{"description":"user id","in":"query","name":"user_id","schema":{"type":"string"}},{"description":"media type e.g. image | video | video_file | video_link","in":"query","name":"media","schema":{"type":"string"}},{"description":"rating filter, 1-5","explode":false,"in":"query","name":"rating","schema":{"items":{"type":"number"},"type":"array"},"style":"form"},{"description":"attribute rating filter with ma,e of attribute","explode":false,"in":"query","name":"attribute_rating","schema":{"items":{"type":"string"},"type":"array"},"style":"form"},{"description":"facets (true|false)","in":"query","name":"facets","schema":{"type":"boolean"}},{"description":"sort by : default | top | recent","in":"query","name":"sort","schema":{"type":"string"}},{"description":"pagination next","in":"query","name":"next","schema":{"type":"string"}},{"description":"pagination start","in":"query","name":"start","schema":{"type":"string"}},{"description":"pagination limit","in":"query","name":"limit","schema":{"type":"string"}},{"description":"pagination count","in":"query","name":"count","schema":{"type":"string"}},{"description":"pagination page id","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"pagination page size","in":"query","name":"page_size","schema":{"type":"integer"}}],"headers":[]}""", company_id=company_id, application_id=application_id, id=id, entity_id=entity_id, entity_type=entity_type, user_id=user_id, media=media, rating=rating, attribute_rating=attribute_rating, facets=facets, sort=sort, next=next, start=start, limit=limit, count=count, page_id=page_id, page_size=page_size)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id, entity_id=entity_id, entity_type=entity_type, user_id=user_id, media=media, rating=rating, attribute_rating=attribute_rating, facets=facets, sort=sort, next=next, start=start, limit=limit, count=count, page_id=page_id, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/feedback/v1.0/company/{company_id}/application/{application_id}/reviews/", company_id=company_id, application_id=application_id, id=id, entity_id=entity_id, entity_type=entity_type, user_id=user_id, media=media, rating=rating, attribute_rating=attribute_rating, facets=facets, sort=sort, next=next, start=start, limit=limit, count=count, page_id=page_id, page_size=page_size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateApprove(self, company_id=None, application_id=None, review_id=None, body=""):
        """The is used to update approve details like status and description text
        :param company_id : company id : type string
        :param application_id : application id : type string
        :param review_id : review id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if review_id:
            payload["review_id"] = review_id
        

        # Parameter validation
        schema = FeedbackValidator.updateApprove()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.ApproveRequest import ApproveRequest
        schema = ApproveRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/feedback/v1.0/company/{company_id}/application/{application_id}/reviews/{review_id}/approve/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"review id","in":"path","name":"review_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, review_id=review_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, review_id=review_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/feedback/v1.0/company/{company_id}/application/{application_id}/reviews/{review_id}/approve/", company_id=company_id, application_id=application_id, review_id=review_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getHistory(self, company_id=None, application_id=None, review_id=None, body=""):
        """The is used to get the history details like status and description text
        :param company_id : company id : type string
        :param application_id : application id : type string
        :param review_id : review id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if review_id:
            payload["review_id"] = review_id
        

        # Parameter validation
        schema = FeedbackValidator.getHistory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/feedback/v1.0/company/{company_id}/application/{application_id}/reviews/{review_id}/history/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"review id","in":"path","name":"review_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, review_id=review_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, review_id=review_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/feedback/v1.0/company/{company_id}/application/{application_id}/reviews/{review_id}/history/", company_id=company_id, application_id=application_id, review_id=review_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getApplicationTemplates(self, company_id=None, application_id=None, page_id=None, page_size=None, body=""):
        """Get all templates of application
        :param company_id : company id : type string
        :param application_id : application id : type string
        :param page_id : pagination page id : type string
        :param page_size : pagination page size : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if page_id:
            payload["page_id"] = page_id
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = FeedbackValidator.getApplicationTemplates()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/feedback/v1.0/company/{company_id}/application/{application_id}/templates/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"pagination page id","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"pagination page size","in":"query","name":"page_size","schema":{"type":"integer"}}],"query":[{"description":"pagination page id","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"pagination page size","in":"query","name":"page_size","schema":{"type":"integer"}}],"headers":[]}""", company_id=company_id, application_id=application_id, page_id=page_id, page_size=page_size)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, page_id=page_id, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/feedback/v1.0/company/{company_id}/application/{application_id}/templates/", company_id=company_id, application_id=application_id, page_id=page_id, page_size=page_size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createTemplate(self, company_id=None, application_id=None, body=""):
        """Create a new template for review with following data:
- Enable media, rating and review
- Rating - active/inactive/selected rate choices, attributes, text on rate, comment for each rate, type
- Review - header, title, description, image and video meta, enable votes
        :param company_id : company id : type string
        :param application_id : application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = FeedbackValidator.createTemplate()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.TemplateRequestList import TemplateRequestList
        schema = TemplateRequestList()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/feedback/v1.0/company/{company_id}/application/{application_id}/templates/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/feedback/v1.0/company/{company_id}/application/{application_id}/templates/", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getTemplateById(self, company_id=None, application_id=None, id=None, body=""):
        """Get the template for product or l3 type by ID
        :param company_id : company id : type string
        :param application_id : application id : type string
        :param id : template id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = FeedbackValidator.getTemplateById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/feedback/v1.0/company/{company_id}/application/{application_id}/templates/{id}/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"template id","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/feedback/v1.0/company/{company_id}/application/{application_id}/templates/{id}/", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateTemplate(self, company_id=None, application_id=None, id=None, body=""):
        """Update existing template status, active/archive
        :param company_id : company id : type string
        :param application_id : application id : type string
        :param id : template id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = FeedbackValidator.updateTemplate()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.UpdateTemplateRequest import UpdateTemplateRequest
        schema = UpdateTemplateRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/feedback/v1.0/company/{company_id}/application/{application_id}/templates/{id}/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"template id","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/feedback/v1.0/company/{company_id}/application/{application_id}/templates/{id}/", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateTemplateStatus(self, company_id=None, application_id=None, id=None, body=""):
        """Update existing template status, active/archive
        :param company_id : company id : type string
        :param application_id : application id : type string
        :param id : template id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = FeedbackValidator.updateTemplateStatus()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.UpdateTemplateStatusRequest import UpdateTemplateStatusRequest
        schema = UpdateTemplateStatusRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/feedback/v1.0/company/{company_id}/application/{application_id}/templates/{id}/status/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"template id","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain("/service/platform/feedback/v1.0/company/{company_id}/application/{application_id}/templates/{id}/status/", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    

class Theme:
    def __init__(self, config):
        self._conf = config
    # async def ():
    
    async def getAllPages(self, company_id=None, application_id=None, theme_id=None, body=""):
        """Use this API to retrieve all the available pages of a theme by its ID.
        :param company_id : Company ID : type string
        :param application_id : Application ID : type string
        :param theme_id : ID of the theme to be retrieved : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.getAllPages()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/{theme_id}/page", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, theme_id=theme_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, theme_id=theme_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/{theme_id}/page", company_id=company_id, application_id=application_id, theme_id=theme_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createPage(self, company_id=None, application_id=None, theme_id=None, body=""):
        """Use this API to create a page for a theme by its ID.
        :param company_id : Company ID : type string
        :param application_id : Application ID : type string
        :param theme_id : ID of the theme : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.createPage()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.AvailablePageSchema import AvailablePageSchema
        schema = AvailablePageSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/{theme_id}/page", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, theme_id=theme_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, theme_id=theme_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/{theme_id}/page", company_id=company_id, application_id=application_id, theme_id=theme_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateMultiplePages(self, company_id=None, application_id=None, theme_id=None, body=""):
        """Use this API to update multiple pages of a theme by its ID.
        :param company_id : Company ID : type string
        :param application_id : Application ID : type string
        :param theme_id : ID of the theme to be retrieved : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.updateMultiplePages()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.AllAvailablePageSchema import AllAvailablePageSchema
        schema = AllAvailablePageSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/{theme_id}/page", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, theme_id=theme_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, theme_id=theme_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/{theme_id}/page", company_id=company_id, application_id=application_id, theme_id=theme_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getPage(self, company_id=None, application_id=None, theme_id=None, page_value=None, body=""):
        """Use this API to retrieve a page of a theme.
        :param company_id : Company ID : type string
        :param application_id : Application ID : type string
        :param theme_id : ID of the theme to be retrieved : type string
        :param page_value : Value of the page to be retrieved : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if theme_id:
            payload["theme_id"] = theme_id
        
        if page_value:
            payload["page_value"] = page_value
        

        # Parameter validation
        schema = ThemeValidator.getPage()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/{theme_id}/{page_value}", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be retrieved","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, theme_id=theme_id, page_value=page_value)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, theme_id=theme_id, page_value=page_value)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/{theme_id}/{page_value}", company_id=company_id, application_id=application_id, theme_id=theme_id, page_value=page_value), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updatePage(self, company_id=None, application_id=None, theme_id=None, page_value=None, body=""):
        """Use this API to update a page for a theme by its ID.
        :param company_id : Company ID : type string
        :param application_id : Application ID : type string
        :param theme_id : ID of the theme : type string
        :param page_value : Value of the page to be updated : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if theme_id:
            payload["theme_id"] = theme_id
        
        if page_value:
            payload["page_value"] = page_value
        

        # Parameter validation
        schema = ThemeValidator.updatePage()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.AvailablePageSchema import AvailablePageSchema
        schema = AvailablePageSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/{theme_id}/{page_value}", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be updated","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, theme_id=theme_id, page_value=page_value)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, theme_id=theme_id, page_value=page_value)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/{theme_id}/{page_value}", company_id=company_id, application_id=application_id, theme_id=theme_id, page_value=page_value), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def deletePage(self, company_id=None, application_id=None, theme_id=None, page_value=None, body=""):
        """Use this API to delete a page for a theme by its ID and page_value.
        :param company_id : Company ID : type string
        :param application_id : Application ID : type string
        :param theme_id : ID of the theme : type string
        :param page_value : Value of the page to be updated : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if theme_id:
            payload["theme_id"] = theme_id
        
        if page_value:
            payload["page_value"] = page_value
        

        # Parameter validation
        schema = ThemeValidator.deletePage()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/{theme_id}/{page_value}", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID of the theme","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be updated","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, theme_id=theme_id, page_value=page_value)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, theme_id=theme_id, page_value=page_value)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain("/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/{theme_id}/{page_value}", company_id=company_id, application_id=application_id, theme_id=theme_id, page_value=page_value), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getThemeLibrary(self, company_id=None, application_id=None, page_size=None, page_no=None, body=""):
        """Theme library is a personalized collection of themes that are chosen and added from the available themes. Use this API to fetch a list of themes from the library along with their configuration details. 
        :param company_id : Numeric ID allotted to a business account on Fynd Platform. : type string
        :param application_id : Alphanumeric ID allotted to an application created within a business account. : type string
        :param page_size : The number of items to retrieve in each page. Default value is 10.  : type integer
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if page_size:
            payload["page_size"] = page_size
        
        if page_no:
            payload["page_no"] = page_no
        

        # Parameter validation
        schema = ThemeValidator.getThemeLibrary()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/library", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10. ","required":false,"schema":{"type":"integer","default":10}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}}],"query":[{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10. ","required":false,"schema":{"type":"integer","default":10}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}}],"headers":[]}""", company_id=company_id, application_id=application_id, page_size=page_size, page_no=page_no)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, page_size=page_size, page_no=page_no)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/library", company_id=company_id, application_id=application_id, page_size=page_size, page_no=page_no), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def addToThemeLibrary(self, company_id=None, application_id=None, body=""):
        """Theme library is a personalized collection of themes that are chosen and added from the available themes. Use this API to choose a theme and add it to the theme library.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform. : type string
        :param application_id : Alphanumeric ID allotted to an application created within a business account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ThemeValidator.addToThemeLibrary()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.AddThemeRequestSchema import AddThemeRequestSchema
        schema = AddThemeRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/library", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/library", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def applyTheme(self, company_id=None, application_id=None, body=""):
        """Use this API to apply a theme to the website.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform. : type string
        :param application_id : Alphanumeric ID allotted to an application created within a business account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ThemeValidator.applyTheme()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.AddThemeRequestSchema import AddThemeRequestSchema
        schema = AddThemeRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/apply", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/apply", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def isUpgradable(self, company_id=None, application_id=None, theme_id=None, body=""):
        """There's always a possibility that new features get added to a theme. Use this API to check if the applied theme has an upgrade available.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform. : type string
        :param application_id : Alphanumeric ID allotted to an application created within a business account. : type string
        :param theme_id : Theme ID : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.isUpgradable()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/{theme_id}/upgradable", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"Theme ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, theme_id=theme_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, theme_id=theme_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/{theme_id}/upgradable", company_id=company_id, application_id=application_id, theme_id=theme_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def upgradeTheme(self, company_id=None, application_id=None, theme_id=None, body=""):
        """Use this API to upgrade the current theme to its latest version.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform. : type string
        :param application_id : Alphanumeric ID allotted to an application created within a business account. : type string
        :param theme_id : ID allotted to the theme. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.upgradeTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/{theme_id}/upgrade", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, theme_id=theme_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, theme_id=theme_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/{theme_id}/upgrade", company_id=company_id, application_id=application_id, theme_id=theme_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getPublicThemes(self, company_id=None, application_id=None, page_size=None, page_no=None, body=""):
        """Use this API to get a list of free themes that you can apply to your website.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform. : type string
        :param application_id : Alphanumeric ID allotted to an application created within a business account. : type string
        :param page_size : The number of items to retrieve in each page. Default value is 10.  : type integer
        :param page_no : The page number to navigate through the given set of results. Default value is 1.  : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if page_size:
            payload["page_size"] = page_size
        
        if page_no:
            payload["page_no"] = page_no
        

        # Parameter validation
        schema = ThemeValidator.getPublicThemes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/list/public", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10. ","required":false,"schema":{"type":"integer","default":10}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1. ","required":false,"schema":{"type":"integer","default":1}}],"query":[{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10. ","required":false,"schema":{"type":"integer","default":10}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1. ","required":false,"schema":{"type":"integer","default":1}}],"headers":[]}""", company_id=company_id, application_id=application_id, page_size=page_size, page_no=page_no)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, page_size=page_size, page_no=page_no)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/list/public", company_id=company_id, application_id=application_id, page_size=page_size, page_no=page_no), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createTheme(self, company_id=None, application_id=None, body=""):
        """Themes improve the look and appearance of a website. Use this API to create a theme.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform. : type string
        :param application_id : Alphanumeric ID allotted to an application created within a business account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ThemeValidator.createTheme()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.ThemesSchema import ThemesSchema
        schema = ThemesSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getAppliedTheme(self, company_id=None, application_id=None, body=""):
        """Use this API to retrieve the theme that is currently applied to the website along with its details.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform. : type string
        :param application_id : Alphanumeric ID allotted to an application created within a business account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ThemeValidator.getAppliedTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getFonts(self, company_id=None, application_id=None, body=""):
        """Font is a collection of characters with a similar design. Use this API to retrieve a list of website fonts.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform. : type string
        :param application_id : Alphanumeric ID allotted to an application created within a business account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ThemeValidator.getFonts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/fonts", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/fonts", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getThemeById(self, company_id=None, application_id=None, theme_id=None, body=""):
        """Use this API to retrieve the details of a specific theme by using its ID.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform. : type string
        :param application_id : Alphanumeric ID allotted to an application created within a business account. : type string
        :param theme_id : ID allotted to the theme. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.getThemeById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/{theme_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, theme_id=theme_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, theme_id=theme_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/{theme_id}", company_id=company_id, application_id=application_id, theme_id=theme_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateTheme(self, company_id=None, application_id=None, theme_id=None, body=""):
        """Use this API to edit an existing theme. You can customize the website font, sections, images, styles, and many more.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform. : type string
        :param application_id : Alphanumeric ID allotted to an application created within a business account. : type string
        :param theme_id : ID allotted to the theme. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.updateTheme()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.ThemesSchema import ThemesSchema
        schema = ThemesSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/{theme_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, theme_id=theme_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, theme_id=theme_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/{theme_id}", company_id=company_id, application_id=application_id, theme_id=theme_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def deleteTheme(self, company_id=None, application_id=None, theme_id=None, body=""):
        """Use this API to delete a theme from the theme library.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform. : type string
        :param application_id : Alphanumeric ID allotted to an application created within a business account. : type string
        :param theme_id : ID allotted to the theme. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.deleteTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/{theme_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, theme_id=theme_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, theme_id=theme_id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain("/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/{theme_id}", company_id=company_id, application_id=application_id, theme_id=theme_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getThemeForPreview(self, company_id=None, application_id=None, theme_id=None, body=""):
        """A theme can be previewed before applying it. Use this API to retrieve the theme preview by using its ID.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform. : type string
        :param application_id : Alphanumeric ID allotted to an application created within a business account. : type string
        :param theme_id : ID allotted to the theme. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.getThemeForPreview()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/{theme_id}/preview", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, theme_id=theme_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, theme_id=theme_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/{theme_id}/preview", company_id=company_id, application_id=application_id, theme_id=theme_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def publishTheme(self, company_id=None, application_id=None, theme_id=None, body=""):
        """Use this API to publish a theme that is either newly created or edited.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform. : type string
        :param application_id : Alphanumeric ID allotted to an application created within a business account. : type string
        :param theme_id : ID allotted to the theme. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.publishTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/{theme_id}/publish", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, theme_id=theme_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, theme_id=theme_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/{theme_id}/publish", company_id=company_id, application_id=application_id, theme_id=theme_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def unpublishTheme(self, company_id=None, application_id=None, theme_id=None, body=""):
        """Use this API to remove an existing theme from the list of available themes.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform. : type string
        :param application_id : Alphanumeric ID allotted to an application created within a business account. : type string
        :param theme_id : ID allotted to the theme. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.unpublishTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/{theme_id}/unpublish", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, theme_id=theme_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, theme_id=theme_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/{theme_id}/unpublish", company_id=company_id, application_id=application_id, theme_id=theme_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def archiveTheme(self, company_id=None, application_id=None, theme_id=None, body=""):
        """Use this API to store an existing theme but not delete it so that it can be used in future if required. 
        :param company_id : Numeric ID allotted to a business account on Fynd Platform. : type string
        :param application_id : Alphanumeric ID allotted to an application created within a business account. : type string
        :param theme_id : ID allotted to the theme. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.archiveTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/{theme_id}/archive", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, theme_id=theme_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, theme_id=theme_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/{theme_id}/archive", company_id=company_id, application_id=application_id, theme_id=theme_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def unarchiveTheme(self, company_id=None, application_id=None, theme_id=None, body=""):
        """Use this API to restore an archived theme and bring it back for editing or publishing. 
        :param company_id : Numeric ID allotted to a business account on Fynd Platform. : type string
        :param application_id : Alphanumeric ID allotted to an application created within a business account. : type string
        :param theme_id : ID allotted to the theme. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if theme_id:
            payload["theme_id"] = theme_id
        

        # Parameter validation
        schema = ThemeValidator.unarchiveTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/{theme_id}/unarchive", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"theme_id","in":"path","description":"ID allotted to the theme.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, theme_id=theme_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, theme_id=theme_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/theme/v1.0/company/{company_id}/application/{application_id}/{theme_id}/unarchive", company_id=company_id, application_id=application_id, theme_id=theme_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    

class User:
    def __init__(self, config):
        self._conf = config
    # async def ():
    
    async def getCustomers(self, company_id=None, application_id=None, q=None, page_size=None, page_no=None, body=""):
        """Use this API to retrieve a list of customers who have registered in the application.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform. : type string
        :param application_id : Alphanumeric ID allotted to an application created within a business account. : type string
        :param q : The search query. Mobile number or email ID of a customer. : type string
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        :param page_no : The page number to navigate through the given set of results. Default value is 1.  : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if q:
            payload["q"] = q
        
        if page_size:
            payload["page_size"] = page_size
        
        if page_no:
            payload["page_no"] = page_no
        

        # Parameter validation
        schema = UserValidator.getCustomers()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/user/v1.0/company/{company_id}/application/{application_id}/customers/list", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"q","in":"query","description":"The search query. Mobile number or email ID of a customer.","required":false,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1. ","required":false,"schema":{"type":"integer","default":1}}],"query":[{"name":"q","in":"query","description":"The search query. Mobile number or email ID of a customer.","required":false,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1. ","required":false,"schema":{"type":"integer","default":1}}],"headers":[]}""", company_id=company_id, application_id=application_id, q=q, page_size=page_size, page_no=page_no)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, q=q, page_size=page_size, page_no=page_no)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/user/v1.0/company/{company_id}/application/{application_id}/customers/list", company_id=company_id, application_id=application_id, q=q, page_size=page_size, page_no=page_no), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def searchUsers(self, company_id=None, application_id=None, q=None, body=""):
        """Use this API to retrieve an existing user from a list.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform. : type string
        :param application_id : Alphanumeric ID allotted to an application created within a business account. : type string
        :param q : The search query. Mobile number or email ID of a customer. : type object
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if q:
            payload["q"] = q
        

        # Parameter validation
        schema = UserValidator.searchUsers()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/user/v1.0/company/{company_id}/application/{application_id}/customers/search", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"q","in":"query","description":"The search query. Mobile number or email ID of a customer.","required":false,"schema":{"type":"object"}}],"query":[{"name":"q","in":"query","description":"The search query. Mobile number or email ID of a customer.","required":false,"schema":{"type":"object"}}],"headers":[]}""", company_id=company_id, application_id=application_id, q=q)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, q=q)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/user/v1.0/company/{company_id}/application/{application_id}/customers/search", company_id=company_id, application_id=application_id, q=q), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createUser(self, company_id=None, application_id=None, body=""):
        """Create user
        :param company_id : Company ID : type string
        :param application_id : Application ID : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = UserValidator.createUser()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.CreateUserRequestSchema import CreateUserRequestSchema
        schema = CreateUserRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/user/v1.0/company/{company_id}/application/{application_id}/customers", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/user/v1.0/company/{company_id}/application/{application_id}/customers", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateUser(self, company_id=None, application_id=None, user_id=None, body=""):
        """Update user
        :param company_id : Company ID : type string
        :param application_id : Application ID : type string
        :param user_id : User ID : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if user_id:
            payload["user_id"] = user_id
        

        # Parameter validation
        schema = UserValidator.updateUser()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.UpdateUserRequestSchema import UpdateUserRequestSchema
        schema = UpdateUserRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/user/v1.0/company/{company_id}/application/{application_id}/customers/{user_id}", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}},{"name":"user_id","in":"path","description":"User ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, user_id=user_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, user_id=user_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/user/v1.0/company/{company_id}/application/{application_id}/customers/{user_id}", company_id=company_id, application_id=application_id, user_id=user_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createUserSession(self, company_id=None, application_id=None, body=""):
        """Create user session
        :param company_id : Company ID : type string
        :param application_id : Application ID : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = UserValidator.createUserSession()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.CreateUserSessionRequestSchema import CreateUserSessionRequestSchema
        schema = CreateUserSessionRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/user/v1.0/company/{company_id}/application/{application_id}/customers/session", """{"required":[{"name":"company_id","in":"path","description":"Company ID","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/user/v1.0/company/{company_id}/application/{application_id}/customers/session", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getPlatformConfig(self, company_id=None, application_id=None, body=""):
        """Use this API to get all the platform configurations such as mobile image, desktop image, social logins, and all other text.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform. : type string
        :param application_id : Alphanumeric ID allotted to an application created within a business account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = UserValidator.getPlatformConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/user/v1.0/company/{company_id}/application/{application_id}/platform/config", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/user/v1.0/company/{company_id}/application/{application_id}/platform/config", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updatePlatformConfig(self, company_id=None, application_id=None, body=""):
        """Use this API to edit the existing platform configurations such as mobile image, desktop image, social logins, and all other text.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform. : type string
        :param application_id : Alphanumeric ID allotted to an application created within a business account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = UserValidator.updatePlatformConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.PlatformSchema import PlatformSchema
        schema = PlatformSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/user/v1.0/company/{company_id}/application/{application_id}/platform/config", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/user/v1.0/company/{company_id}/application/{application_id}/platform/config", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    

class Content:
    def __init__(self, config):
        self._conf = config
    # async def ():
    
    async def getAnnouncementsList(self, company_id=None, application_id=None, page_no=None, page_size=None, body=""):
        """Announcements are useful to highlight a message or information on top of a webpage. Use this API to retrieve a list of announcements.	
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ContentValidator.getAnnouncementsList()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/announcements", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"headers":[]}""", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/announcements", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createAnnouncement(self, company_id=None, application_id=None, body=""):
        """Announcements are useful to highlight a message or information on top of a webpage. Use this API to create an announcement.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ContentValidator.createAnnouncement()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.AdminAnnouncementSchema import AdminAnnouncementSchema
        schema = AdminAnnouncementSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/announcements", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/announcements", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getAnnouncementById(self, company_id=None, application_id=None, announcement_id=None, body=""):
        """Use this API to retrieve an announcement and its details such as the target platform and pages on which it's applicable
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        :param announcement_id : ID allotted to the announcement. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if announcement_id:
            payload["announcement_id"] = announcement_id
        

        # Parameter validation
        schema = ContentValidator.getAnnouncementById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/announcements/{announcement_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"announcement_id","in":"path","description":"ID allotted to the announcement.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, announcement_id=announcement_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, announcement_id=announcement_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/announcements/{announcement_id}", company_id=company_id, application_id=application_id, announcement_id=announcement_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateAnnouncement(self, company_id=None, application_id=None, announcement_id=None, body=""):
        """Use this API to edit an existing announcement and its details such as the target platform and pages on which it's applicable
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        :param announcement_id : ID allotted to the announcement. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if announcement_id:
            payload["announcement_id"] = announcement_id
        

        # Parameter validation
        schema = ContentValidator.updateAnnouncement()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.AdminAnnouncementSchema import AdminAnnouncementSchema
        schema = AdminAnnouncementSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/announcements/{announcement_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"announcement_id","in":"path","description":"ID allotted to the announcement.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, announcement_id=announcement_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, announcement_id=announcement_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/announcements/{announcement_id}", company_id=company_id, application_id=application_id, announcement_id=announcement_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateAnnouncementSchedule(self, company_id=None, application_id=None, announcement_id=None, body=""):
        """Use this API to edit the duration, i.e. start date-time and end date-time of an announcement. Moreover, you can enable/disable an announcement using this API.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        :param announcement_id : ID allotted to the announcement. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if announcement_id:
            payload["announcement_id"] = announcement_id
        

        # Parameter validation
        schema = ContentValidator.updateAnnouncementSchedule()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.ScheduleSchema import ScheduleSchema
        schema = ScheduleSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/announcements/{announcement_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"announcement_id","in":"path","description":"ID allotted to the announcement.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, announcement_id=announcement_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, announcement_id=announcement_id)
        return await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/announcements/{announcement_id}", company_id=company_id, application_id=application_id, announcement_id=announcement_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def deleteAnnouncement(self, company_id=None, application_id=None, announcement_id=None, body=""):
        """Use this API to delete an existing announcement.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        :param announcement_id : ID allotted to the announcement. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if announcement_id:
            payload["announcement_id"] = announcement_id
        

        # Parameter validation
        schema = ContentValidator.deleteAnnouncement()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/announcements/{announcement_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"announcement_id","in":"path","description":"ID allotted to the announcement.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, announcement_id=announcement_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, announcement_id=announcement_id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/announcements/{announcement_id}", company_id=company_id, application_id=application_id, announcement_id=announcement_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createBlog(self, company_id=None, application_id=None, body=""):
        """Use this API to create a blog.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ContentValidator.createBlog()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.BlogRequest import BlogRequest
        schema = BlogRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/blogs/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/blogs/", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getBlogs(self, company_id=None, application_id=None, page_no=None, page_size=None, body=""):
        """Use this API to get a list of blogs along with their details, such as the title, reading time, publish status, feature image, tags, author, etc.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ContentValidator.getBlogs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/blogs/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"headers":[]}""", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/blogs/", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateBlog(self, company_id=None, application_id=None, id=None, body=""):
        """Use this API to update the details of an existing blog which includes title, feature image, content, SEO details, expiry, etc.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        :param id : ID allotted to the blog. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ContentValidator.updateBlog()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.BlogRequest import BlogRequest
        schema = BlogRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/blogs/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the blog.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/blogs/{id}", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def deleteBlog(self, company_id=None, application_id=None, id=None, body=""):
        """Use this API to delete a blog.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        :param id : ID allotted to the blog. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ContentValidator.deleteBlog()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/blogs/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the blog.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/blogs/{id}", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getComponentById(self, company_id=None, application_id=None, slug=None, body=""):
        """Use this API to retrieve the components of a blog, such as title, slug, feature image, content, schedule, publish status, author, etc.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        :param slug : A short, human-readable, URL-friendly identifier of a blog page. You can get slug value of a blog from `getBlogs` API. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if slug:
            payload["slug"] = slug
        

        # Parameter validation
        schema = ContentValidator.getComponentById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/blogs/{slug}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a blog page. You can get slug value of a blog from `getBlogs` API.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, slug=slug)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, slug=slug)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/blogs/{slug}", company_id=company_id, application_id=application_id, slug=slug), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getFaqCategories(self, company_id=None, application_id=None, body=""):
        """FAQs can be divided into categories. Use this API to get a list of FAQ categories.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ContentValidator.getFaqCategories()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/faq/categories", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/faq/categories", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getFaqCategoryBySlugOrId(self, company_id=None, application_id=None, id_or_slug=None, body=""):
        """FAQs can be divided into categories. Use this API to get an FAQ categories using its slug or ID.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        :param id_or_slug : ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id_or_slug:
            payload["id_or_slug"] = id_or_slug
        

        # Parameter validation
        schema = ContentValidator.getFaqCategoryBySlugOrId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/faq/category/{id_or_slug}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id_or_slug","in":"path","description":"ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id_or_slug=id_or_slug)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id_or_slug=id_or_slug)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/faq/category/{id_or_slug}", company_id=company_id, application_id=application_id, id_or_slug=id_or_slug), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createFaqCategory(self, company_id=None, application_id=None, body=""):
        """FAQs help users to solve an issue or know more about a process. FAQs can be categorized separately, for e.g. some questions can be related to payment, some could be related to purchase, shipping, navigating, etc. Use this API to create an FAQ category.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ContentValidator.createFaqCategory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.CreateFaqCategoryRequestSchema import CreateFaqCategoryRequestSchema
        schema = CreateFaqCategoryRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/faq/category", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/faq/category", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateFaqCategory(self, company_id=None, application_id=None, id=None, body=""):
        """Use this API to edit an existing FAQ category.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        :param id : ID allotted to an FAQ category. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ContentValidator.updateFaqCategory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.UpdateFaqCategoryRequestSchema import UpdateFaqCategoryRequestSchema
        schema = UpdateFaqCategoryRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/faq/category/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/faq/category/{id}", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def deleteFaqCategory(self, company_id=None, application_id=None, id=None, body=""):
        """Use this API to delete an FAQ category.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        :param id : ID allotted to an FAQ category. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ContentValidator.deleteFaqCategory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/faq/category/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/faq/category/{id}", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getFaqsByCategoryIdOrSlug(self, company_id=None, application_id=None, id_or_slug=None, body=""):
        """Use this API to retrieve all the commonly asked question and answers belonging to an FAQ category.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        :param id_or_slug : ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id_or_slug:
            payload["id_or_slug"] = id_or_slug
        

        # Parameter validation
        schema = ContentValidator.getFaqsByCategoryIdOrSlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/faq/category/{id_or_slug}/faqs", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id_or_slug","in":"path","description":"ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id_or_slug=id_or_slug)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id_or_slug=id_or_slug)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/faq/category/{id_or_slug}/faqs", company_id=company_id, application_id=application_id, id_or_slug=id_or_slug), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def addFaq(self, company_id=None, application_id=None, category_id=None, body=""):
        """FAQs help users to solve an issue or know more about a process. Use this API to create an FAQ for a given FAQ category.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        :param category_id : ID allotted to an FAQ category. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if category_id:
            payload["category_id"] = category_id
        

        # Parameter validation
        schema = ContentValidator.addFaq()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.CreateFaqSchema import CreateFaqSchema
        schema = CreateFaqSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/faq/category/{category_id}/faqs", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"category_id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, category_id=category_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, category_id=category_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/faq/category/{category_id}/faqs", company_id=company_id, application_id=application_id, category_id=category_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateFaq(self, company_id=None, application_id=None, category_id=None, faq_id=None, body=""):
        """Use this API to edit an existing FAQ.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        :param category_id : ID allotted to an FAQ category. : type string
        :param faq_id : ID allotted to an FAQ. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if category_id:
            payload["category_id"] = category_id
        
        if faq_id:
            payload["faq_id"] = faq_id
        

        # Parameter validation
        schema = ContentValidator.updateFaq()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.CreateFaqSchema import CreateFaqSchema
        schema = CreateFaqSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/faq/category/{category_id}/faq/{faq_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"category_id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}},{"name":"faq_id","in":"path","description":"ID allotted to an FAQ.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, category_id=category_id, faq_id=faq_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, category_id=category_id, faq_id=faq_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/faq/category/{category_id}/faq/{faq_id}", company_id=company_id, application_id=application_id, category_id=category_id, faq_id=faq_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def deleteFaq(self, company_id=None, application_id=None, category_id=None, faq_id=None, body=""):
        """Use this API to delete an existing FAQ.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        :param category_id : ID allotted to an FAQ category. : type string
        :param faq_id : ID allotted to an FAQ. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if category_id:
            payload["category_id"] = category_id
        
        if faq_id:
            payload["faq_id"] = faq_id
        

        # Parameter validation
        schema = ContentValidator.deleteFaq()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/faq/category/{category_id}/faq/{faq_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"category_id","in":"path","description":"ID allotted to an FAQ category.","required":true,"schema":{"type":"string"}},{"name":"faq_id","in":"path","description":"ID allotted to an FAQ.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, category_id=category_id, faq_id=faq_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, category_id=category_id, faq_id=faq_id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/faq/category/{category_id}/faq/{faq_id}", company_id=company_id, application_id=application_id, category_id=category_id, faq_id=faq_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getFaqByIdOrSlug(self, company_id=None, application_id=None, id_or_slug=None, body=""):
        """Use this API to retrieve a specific FAQ. You will get the question and answer of that FAQ.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        :param id_or_slug : ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id_or_slug:
            payload["id_or_slug"] = id_or_slug
        

        # Parameter validation
        schema = ContentValidator.getFaqByIdOrSlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/faq/{id_or_slug}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id_or_slug","in":"path","description":"ID or the slug allotted to an FAQ category. Slug is a short, human-readable, URL-friendly identifier of an object. You can get slug value of an FAQ category from `getFaqCategories` API.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id_or_slug=id_or_slug)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id_or_slug=id_or_slug)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/faq/{id_or_slug}", company_id=company_id, application_id=application_id, id_or_slug=id_or_slug), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getLandingPages(self, company_id=None, application_id=None, page_no=None, page_size=None, body=""):
        """Landing page is the first page that a prospect lands upon while visiting a website. Use this API to fetch a list of landing pages.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ContentValidator.getLandingPages()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/landing-page/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"headers":[]}""", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/landing-page/", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createLandingPage(self, company_id=None, application_id=None, body=""):
        """Landing page is the first page that a prospect lands upon while visiting a website. Use this API to create a landing page.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ContentValidator.createLandingPage()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.LandingPageSchema import LandingPageSchema
        schema = LandingPageSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/landing-page/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/landing-page/", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateLandingPage(self, company_id=None, application_id=None, id=None, body=""):
        """Use this API to edit the details of an existing landing page.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        :param id : ID allotted to a landing page. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ContentValidator.updateLandingPage()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.LandingPageSchema import LandingPageSchema
        schema = LandingPageSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/landing-page/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to a landing page.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/landing-page/{id}", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def deleteLandingPage(self, company_id=None, application_id=None, id=None, body=""):
        """Use this API to delete an existing landing page.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        :param id : ID allotted to a landing page. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ContentValidator.deleteLandingPage()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/landing-page/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to a landing page.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/landing-page/{id}", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getLegalInformation(self, company_id=None, application_id=None, body=""):
        """Use this API to get the legal information of an application, which includes Policy, Terms and Conditions, Shipping Policy and FAQ regarding the application.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ContentValidator.getLegalInformation()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/legal", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/legal", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateLegalInformation(self, company_id=None, application_id=None, body=""):
        """Use this API to edit, update and save the legal information of an application, which includes Policy, Terms and Conditions, Shipping Policy and FAQ regarding the application.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ContentValidator.updateLegalInformation()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.ApplicationLegal import ApplicationLegal
        schema = ApplicationLegal()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/legal", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/legal", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getNavigations(self, company_id=None, application_id=None, device_platform=None, page_no=None, page_size=None, body=""):
        """Use this API to fetch the navigations details which includes the items of the navigation pane. It also shows the orientation, links, sub-navigations, etc.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        :param device_platform : Filter navigations by platform. Acceptable values are: web, android, ios, all : type string
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if device_platform:
            payload["device_platform"] = device_platform
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ContentValidator.getNavigations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/navigations/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"device_platform","in":"query","description":"Filter navigations by platform. Acceptable values are: web, android, ios, all","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"device_platform","in":"query","description":"Filter navigations by platform. Acceptable values are: web, android, ios, all","required":true,"schema":{"type":"string"}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"headers":[]}""", company_id=company_id, application_id=application_id, device_platform=device_platform, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, device_platform=device_platform, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/navigations/", company_id=company_id, application_id=application_id, device_platform=device_platform, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createNavigation(self, company_id=None, application_id=None, body=""):
        """Navigation is the arrangement of navigational items to ease the accessibility of resources for users on a website. Use this API to create a navigation.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ContentValidator.createNavigation()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.NavigationRequest import NavigationRequest
        schema = NavigationRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/navigations/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/navigations/", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getDefaultNavigations(self, company_id=None, application_id=None, body=""):
        """On any website (application), there are navigations that are present by default. Use this API to retrieve those default navigations.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ContentValidator.getDefaultNavigations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/navigations/default", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/navigations/default", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getNavigationBySlug(self, company_id=None, application_id=None, slug=None, device_platform=None, body=""):
        """Use this API to retrieve a navigation by its slug.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        :param slug : A short, human-readable, URL-friendly identifier of a navigation. You can get slug value of a navigation from `getNavigations` API. : type string
        :param device_platform : Filter navigations by platform. Acceptable values are: web, android, ios, all : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if slug:
            payload["slug"] = slug
        
        if device_platform:
            payload["device_platform"] = device_platform
        

        # Parameter validation
        schema = ContentValidator.getNavigationBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/navigations/{slug}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a navigation. You can get slug value of a navigation from `getNavigations` API.","required":true,"schema":{"type":"string"}},{"name":"device_platform","in":"query","description":"Filter navigations by platform. Acceptable values are: web, android, ios, all","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"device_platform","in":"query","description":"Filter navigations by platform. Acceptable values are: web, android, ios, all","required":true,"schema":{"type":"string"}}],"headers":[]}""", company_id=company_id, application_id=application_id, slug=slug, device_platform=device_platform)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, slug=slug, device_platform=device_platform)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/navigations/{slug}", company_id=company_id, application_id=application_id, slug=slug, device_platform=device_platform), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateNavigation(self, company_id=None, application_id=None, id=None, body=""):
        """Use this API to edit the details of an existing navigation.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        :param id : ID allotted to the navigation. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ContentValidator.updateNavigation()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.NavigationRequest import NavigationRequest
        schema = NavigationRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/navigations/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the navigation.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/navigations/{id}", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def deleteNavigation(self, company_id=None, application_id=None, id=None, body=""):
        """Use this API to delete an existing navigation.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        :param id : ID allotted to the navigation. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ContentValidator.deleteNavigation()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/navigations/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the navigation.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/navigations/{id}", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getPageMeta(self, company_id=None, application_id=None, page_type=None, cart_pages=None, body=""):
        """Use this API to get the meta of custom pages (blog, page) and default system pages (e.g. home/brand/category/collection).
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        :param page_type : Fetch meta by page type. Acceptable values are: system, custom and all : type string
        :param cart_pages : Pass this param value as `true` to fetch meta with cart pages : type boolean
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if page_type:
            payload["page_type"] = page_type
        
        if cart_pages:
            payload["cart_pages"] = cart_pages
        

        # Parameter validation
        schema = ContentValidator.getPageMeta()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/pages/meta", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_type","in":"query","description":"Fetch meta by page type. Acceptable values are: system, custom and all","required":false,"schema":{"type":"string","default":"all"}},{"name":"cart_pages","in":"query","description":"Pass this param value as `true` to fetch meta with cart pages","required":false,"schema":{"type":"boolean","default":"false"}}],"query":[{"name":"page_type","in":"query","description":"Fetch meta by page type. Acceptable values are: system, custom and all","required":false,"schema":{"type":"string","default":"all"}},{"name":"cart_pages","in":"query","description":"Pass this param value as `true` to fetch meta with cart pages","required":false,"schema":{"type":"boolean","default":"false"}}],"headers":[]}""", company_id=company_id, application_id=application_id, page_type=page_type, cart_pages=cart_pages)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, page_type=page_type, cart_pages=cart_pages)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/pages/meta", company_id=company_id, application_id=application_id, page_type=page_type, cart_pages=cart_pages), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getPageSpec(self, company_id=None, application_id=None, body=""):
        """Use this API to get the specifications of a page, such as page type, display name, params and query.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ContentValidator.getPageSpec()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/pages/spec", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/pages/spec", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createPagePreview(self, company_id=None, application_id=None, body=""):
        """Use this API to create a page preview to check the appearance of a custom page.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ContentValidator.createPagePreview()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.PageRequest import PageRequest
        schema = PageRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/pages/preview/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/pages/preview/", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updatePagePreview(self, company_id=None, application_id=None, slug=None, body=""):
        """Use this API to change the publish status of an existing page. Allows you to publish and unpublish the page.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        :param slug : A short, human-readable, URL-friendly identifier of a page. You can get slug value of a page from `getPages` API. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if slug:
            payload["slug"] = slug
        

        # Parameter validation
        schema = ContentValidator.updatePagePreview()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.PagePublishRequest import PagePublishRequest
        schema = PagePublishRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/pages/publish/{slug}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a page. You can get slug value of a page from `getPages` API.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, slug=slug)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, slug=slug)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/pages/publish/{slug}", company_id=company_id, application_id=application_id, slug=slug), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def deletePage(self, company_id=None, application_id=None, id=None, body=""):
        """Use this API to delete an existing page.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        :param id : ID allotted to the page. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ContentValidator.deletePage()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/pages/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the page.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/pages/{id}", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updatePathRedirectionRules(self, company_id=None, application_id=None, body=""):
        """Use this API to add, update or delete path-based redirection rules
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ContentValidator.updatePathRedirectionRules()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.PathMappingSchema import PathMappingSchema
        schema = PathMappingSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/path-mappings", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/path-mappings", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getPathRedirectionRules(self, company_id=None, application_id=None, body=""):
        """Use this API to get path based redirection rules.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ContentValidator.getPathRedirectionRules()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/path-mappings", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/path-mappings", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getSEOConfiguration(self, company_id=None, application_id=None, body=""):
        """Use this API to know how the SEO is configured in the application. This includes the sitemap, robot.txt, custom meta tags, etc.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ContentValidator.getSEOConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/seo", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/seo", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateSEOConfiguration(self, company_id=None, application_id=None, body=""):
        """Use this API to edit the SEO details of an application. This includes the sitemap, robot.txt, custom meta tags, etc.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ContentValidator.updateSEOConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.SeoComponent import SeoComponent
        schema = SeoComponent()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/seo", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/seo", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getSlideshows(self, company_id=None, application_id=None, device_platform=None, page_no=None, page_size=None, body=""):
        """A slideshow is a group of images, videos or a combination of both that are shown on the website in the form of slides. Use this API to fetch a list of slideshows.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        :param device_platform : Filter slideshows by platform. Acceptable values are: web, android, ios and all : type string
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if device_platform:
            payload["device_platform"] = device_platform
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ContentValidator.getSlideshows()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/slideshows/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"device_platform","in":"query","description":"Filter slideshows by platform. Acceptable values are: web, android, ios and all","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"device_platform","in":"query","description":"Filter slideshows by platform. Acceptable values are: web, android, ios and all","required":true,"schema":{"type":"string"}},{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"headers":[]}""", company_id=company_id, application_id=application_id, device_platform=device_platform, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, device_platform=device_platform, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/slideshows/", company_id=company_id, application_id=application_id, device_platform=device_platform, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createSlideshow(self, company_id=None, application_id=None, body=""):
        """A slideshow is a group of images, videos or a combination of both that are shown on the website in the form of slides. Use this API to create a slideshow.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ContentValidator.createSlideshow()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.SlideshowRequest import SlideshowRequest
        schema = SlideshowRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/slideshows/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/slideshows/", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getSlideshowBySlug(self, company_id=None, application_id=None, slug=None, device_platform=None, body=""):
        """Use this API to retrieve the details of a slideshow by its slug.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        :param slug : A short, human-readable, URL-friendly identifier of a slideshow. You can get slug value of a page from `getSlideshows` API. : type string
        :param device_platform : Filter slideshows by platform. Acceptable values are: web, android, ios and all : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if slug:
            payload["slug"] = slug
        
        if device_platform:
            payload["device_platform"] = device_platform
        

        # Parameter validation
        schema = ContentValidator.getSlideshowBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/slideshows/{slug}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a slideshow. You can get slug value of a page from `getSlideshows` API.","required":true,"schema":{"type":"string"}},{"name":"device_platform","in":"query","description":"Filter slideshows by platform. Acceptable values are: web, android, ios and all","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"device_platform","in":"query","description":"Filter slideshows by platform. Acceptable values are: web, android, ios and all","required":true,"schema":{"type":"string"}}],"headers":[]}""", company_id=company_id, application_id=application_id, slug=slug, device_platform=device_platform)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, slug=slug, device_platform=device_platform)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/slideshows/{slug}", company_id=company_id, application_id=application_id, slug=slug, device_platform=device_platform), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateSlideshow(self, company_id=None, application_id=None, id=None, body=""):
        """Use this API to edit the details of an existing slideshow.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        :param id : ID allotted to the slideshow. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ContentValidator.updateSlideshow()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.SlideshowRequest import SlideshowRequest
        schema = SlideshowRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/slideshows/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the slideshow.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/slideshows/{id}", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def deleteSlideshow(self, company_id=None, application_id=None, id=None, body=""):
        """Use this API to delete an existing slideshow.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        :param id : ID allotted to the slideshow. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ContentValidator.deleteSlideshow()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/slideshows/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the slideshow.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/slideshows/{id}", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getSupportInformation(self, company_id=None, application_id=None, body=""):
        """Use this API to get the contact details for customer support, including emails and phone numbers.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform. : type string
        :param application_id : Alphanumeric ID allotted to an application created within a business account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ContentValidator.getSupportInformation()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/support", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/support", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateSupportInformation(self, company_id=None, application_id=None, body=""):
        """Use this API to edit the existing contact details for customer support, including emails and phone numbers.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform. : type string
        :param application_id : Alphanumeric ID allotted to an application created within a business account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ContentValidator.updateSupportInformation()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.Support import Support
        schema = Support()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/support", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/support", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateInjectableTag(self, company_id=None, application_id=None, body=""):
        """Use this API to edit the details of an existing tag. This includes the tag name, tag type (css/js), url and position of the tag.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform. : type string
        :param application_id : Alphanumeric ID allotted to an application created within a business account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ContentValidator.updateInjectableTag()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.CreateTagRequestSchema import CreateTagRequestSchema
        schema = CreateTagRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/tags", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/tags", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def deleteAllInjectableTags(self, company_id=None, application_id=None, body=""):
        """Use this API to delete all the existing tags at once.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform. : type string
        :param application_id : Alphanumeric ID allotted to an application created within a business account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ContentValidator.deleteAllInjectableTags()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/tags", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/tags", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getInjectableTags(self, company_id=None, application_id=None, body=""):
        """Use this API to get all the CSS and JS injected in the application in the form of tags.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform. : type string
        :param application_id : Alphanumeric ID allotted to an application created within a business account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ContentValidator.getInjectableTags()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/tags", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/tags", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def addInjectableTag(self, company_id=None, application_id=None, body=""):
        """CSS and JS can be injected in the application (website) with the help of tags. Use this API to create such tags by entering the tag name, tag type (css/js), url and position of the tag.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform. : type string
        :param application_id : Alphanumeric ID allotted to an application created within a business account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ContentValidator.addInjectableTag()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.CreateTagRequestSchema import CreateTagRequestSchema
        schema = CreateTagRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/tags/add", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/tags/add", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def removeInjectableTag(self, company_id=None, application_id=None, body=""):
        """Use this API to delete an existing tag.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform. : type string
        :param application_id : Alphanumeric ID allotted to an application created within a business account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ContentValidator.removeInjectableTag()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.RemoveHandpickedSchema import RemoveHandpickedSchema
        schema = RemoveHandpickedSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/tags/remove/handpicked", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/tags/remove/handpicked", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def editInjectableTag(self, company_id=None, application_id=None, tag_id=None, body=""):
        """Use this API to edit the details of an existing tag by its ID.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform. : type string
        :param application_id : Alphanumeric ID allotted to an application created within a business account. : type string
        :param tag_id : ID allotted to the tag. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if tag_id:
            payload["tag_id"] = tag_id
        

        # Parameter validation
        schema = ContentValidator.editInjectableTag()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.UpdateHandpickedSchema import UpdateHandpickedSchema
        schema = UpdateHandpickedSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v1.0/company/{company_id}/application/{application_id}/tags/edit/handpicked/{tag_id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform.","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Alphanumeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"tag_id","in":"path","description":"ID allotted to the tag.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, tag_id=tag_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, tag_id=tag_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/content/v1.0/company/{company_id}/application/{application_id}/tags/edit/handpicked/{tag_id}", company_id=company_id, application_id=application_id, tag_id=tag_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createPage(self, company_id=None, application_id=None, body=""):
        """Use this API to create a custom page using a title, seo, publish status, feature image, tags, meta, etc.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ContentValidator.createPage()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.PageRequest import PageRequest
        schema = PageRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v2.0/company/{company_id}/application/{application_id}/pages/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/content/v2.0/company/{company_id}/application/{application_id}/pages/", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getPages(self, company_id=None, application_id=None, page_no=None, page_size=None, body=""):
        """Use this API to retrieve a list of pages.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ContentValidator.getPages()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v2.0/company/{company_id}/application/{application_id}/pages/", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer","default":10}}],"headers":[]}""", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/content/v2.0/company/{company_id}/application/{application_id}/pages/", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updatePage(self, company_id=None, application_id=None, id=None, body=""):
        """Use this API to edit the details of an existing page, such as its title, seo, publish status, feature image, tags, schedule, etc.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        :param id : ID allotted to the page. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ContentValidator.updatePage()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.PageSchema import PageSchema
        schema = PageSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v2.0/company/{company_id}/application/{application_id}/pages/{id}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"ID allotted to the page.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/content/v2.0/company/{company_id}/application/{application_id}/pages/{id}", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getPageBySlug(self, company_id=None, application_id=None, slug=None, body=""):
        """Use this API to retrieve the components of a page, such as its title, seo, publish status, feature image, tags, schedule, etc.
        :param company_id : Numeric ID allotted to a business account on Fynd Platform : type string
        :param application_id : Numeric ID allotted to an application created within a business account. : type string
        :param slug : A short, human-readable, URL-friendly identifier of a page. You can get slug value of a page from `getPages` API. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if slug:
            payload["slug"] = slug
        

        # Parameter validation
        schema = ContentValidator.getPageBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/content/v2.0/company/{company_id}/application/{application_id}/pages/{slug}", """{"required":[{"name":"company_id","in":"path","description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Numeric ID allotted to an application created within a business account.","required":true,"schema":{"type":"string"}},{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a page. You can get slug value of a page from `getPages` API.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, slug=slug)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, slug=slug)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/content/v2.0/company/{company_id}/application/{application_id}/pages/{slug}", company_id=company_id, application_id=application_id, slug=slug), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    

class Billing:
    def __init__(self, config):
        self._conf = config
    # async def ():
    
    async def createSubscriptionCharge(self, company_id=None, extension_id=None, body=""):
        """Register subscription charge for a seller of your extension.
        :param company_id : Customer unique id. In case of company it will be company id. : type string
        :param extension_id : Extension _id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if extension_id:
            payload["extension_id"] = extension_id
        

        # Parameter validation
        schema = BillingValidator.createSubscriptionCharge()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.CreateSubscriptionCharge import CreateSubscriptionCharge
        schema = CreateSubscriptionCharge()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/billing/v1.0/company/{company_id}/extension/{extension_id}/subscription", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"extension_id","description":"Extension _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, extension_id=extension_id)
        query_string = await create_query_string(company_id=company_id, extension_id=extension_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/billing/v1.0/company/{company_id}/extension/{extension_id}/subscription", company_id=company_id, extension_id=extension_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getSubscriptionCharge(self, company_id=None, extension_id=None, subscription_id=None, body=""):
        """Get created subscription charge details
        :param company_id : Customer unique id. In case of company it will be company id. : type string
        :param extension_id : Extension _id : type string
        :param subscription_id : Subscription charge _id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if extension_id:
            payload["extension_id"] = extension_id
        
        if subscription_id:
            payload["subscription_id"] = subscription_id
        

        # Parameter validation
        schema = BillingValidator.getSubscriptionCharge()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/billing/v1.0/company/{company_id}/extension/{extension_id}/subscription/{subscription_id}", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"extension_id","description":"Extension _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}},{"in":"path","name":"subscription_id","description":"Subscription charge _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, extension_id=extension_id, subscription_id=subscription_id)
        query_string = await create_query_string(company_id=company_id, extension_id=extension_id, subscription_id=subscription_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/billing/v1.0/company/{company_id}/extension/{extension_id}/subscription/{subscription_id}", company_id=company_id, extension_id=extension_id, subscription_id=subscription_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def cancelSubscriptionCharge(self, company_id=None, extension_id=None, subscription_id=None, body=""):
        """Cancel subscription and attached charges.
        :param company_id : Customer unique id. In case of company it will be company id. : type string
        :param extension_id : Extension _id : type string
        :param subscription_id : Subscription charge _id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if extension_id:
            payload["extension_id"] = extension_id
        
        if subscription_id:
            payload["subscription_id"] = subscription_id
        

        # Parameter validation
        schema = BillingValidator.cancelSubscriptionCharge()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/billing/v1.0/company/{company_id}/extension/{extension_id}/subscription/{subscription_id}/cancel", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"extension_id","description":"Extension _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}},{"in":"path","name":"subscription_id","description":"Subscription charge _id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, extension_id=extension_id, subscription_id=subscription_id)
        query_string = await create_query_string(company_id=company_id, extension_id=extension_id, subscription_id=subscription_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/billing/v1.0/company/{company_id}/extension/{extension_id}/subscription/{subscription_id}/cancel", company_id=company_id, extension_id=extension_id, subscription_id=subscription_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getInvoices(self, company_id=None, body=""):
        """Get invoices.
        :param company_id : Customer unique id. In case of company it will be company id. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = BillingValidator.getInvoices()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/billing/v1.0/company/{company_id}/invoice/list", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/billing/v1.0/company/{company_id}/invoice/list", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getInvoiceById(self, company_id=None, invoice_id=None, body=""):
        """Get invoice by id.
        :param company_id : Customer unique id. In case of company it will be company id. : type string
        :param invoice_id : Invoice id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if invoice_id:
            payload["invoice_id"] = invoice_id
        

        # Parameter validation
        schema = BillingValidator.getInvoiceById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/billing/v1.0/company/{company_id}/invoice/{invoice_id}", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"invoice_id","description":"Invoice id","required":true,"schema":{"type":"string","example":"5f7acb709e76da30e3b92cdb"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, invoice_id=invoice_id)
        query_string = await create_query_string(company_id=company_id, invoice_id=invoice_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/billing/v1.0/company/{company_id}/invoice/{invoice_id}", company_id=company_id, invoice_id=invoice_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getCustomerDetail(self, company_id=None, body=""):
        """Get subscription customer detail.
        :param company_id : Customer unique id. In case of company it will be company id. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = BillingValidator.getCustomerDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/billing/v1.0/company/{company_id}/subscription/customer-detail", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/billing/v1.0/company/{company_id}/subscription/customer-detail", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def upsertCustomerDetail(self, company_id=None, body=""):
        """Upsert subscription customer detail.
        :param company_id : Customer unique id. In case of company it will be company id. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = BillingValidator.upsertCustomerDetail()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.SubscriptionCustomerCreate import SubscriptionCustomerCreate
        schema = SubscriptionCustomerCreate()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/billing/v1.0/company/{company_id}/subscription/customer-detail", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/billing/v1.0/company/{company_id}/subscription/customer-detail", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getSubscription(self, company_id=None, body=""):
        """If subscription is active then it will return is_enabled true and return subscription object. If subscription is not active then is_enabled false and message.

        :param company_id : Customer unique id. In case of company it will be company id. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = BillingValidator.getSubscription()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/billing/v1.0/company/{company_id}/subscription/current", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/billing/v1.0/company/{company_id}/subscription/current", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getFeatureLimitConfig(self, company_id=None, body=""):
        """Get subscription subscription limits.
        :param company_id : Customer unique id. In case of company it will be company id. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = BillingValidator.getFeatureLimitConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/billing/v1.0/company/{company_id}/subscription/current-limit", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/billing/v1.0/company/{company_id}/subscription/current-limit", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def activateSubscriptionPlan(self, company_id=None, body=""):
        """It will activate subscription plan for customer
        :param company_id : Customer unique id. In case of company it will be company id. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = BillingValidator.activateSubscriptionPlan()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.SubscriptionActivateReq import SubscriptionActivateReq
        schema = SubscriptionActivateReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/billing/v1.0/company/{company_id}/subscription/activate", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/billing/v1.0/company/{company_id}/subscription/activate", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def cancelSubscriptionPlan(self, company_id=None, body=""):
        """It will cancel current active subscription.
        :param company_id : Customer unique id. In case of company it will be company id. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = BillingValidator.cancelSubscriptionPlan()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.CancelSubscriptionReq import CancelSubscriptionReq
        schema = CancelSubscriptionReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/billing/v1.0/company/{company_id}/subscription/cancel", """{"required":[{"in":"path","name":"company_id","description":"Customer unique id. In case of company it will be company id.","required":true,"schema":{"type":"string","example":"1"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/billing/v1.0/company/{company_id}/subscription/cancel", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    

class Communication:
    def __init__(self, config):
        self._conf = config
    # async def ():
    
    async def getCampaigns(self, company_id=None, application_id=None, page_no=None, page_size=None, sort=None, body=""):
        """Get campaigns
        :param company_id : Company id : type string
        :param application_id : Application id : type string
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if sort:
            payload["sort"] = sort
        

        # Parameter validation
        schema = CommunicationValidator.getCampaigns()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/campaigns/campaigns", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"headers":[]}""", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, sort=sort)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, sort=sort)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/campaigns/campaigns", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, sort=sort), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createCampaign(self, company_id=None, application_id=None, body=""):
        """Create campaign
        :param company_id : Company id : type string
        :param application_id : Application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = CommunicationValidator.createCampaign()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.CampaignReq import CampaignReq
        schema = CampaignReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/campaigns/campaigns", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/campaigns/campaigns", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getCampaignById(self, company_id=None, application_id=None, id=None, body=""):
        """Get campaign by id
        :param company_id : Company id : type string
        :param application_id : Application id : type string
        :param id : Campaign id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.getCampaignById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/campaigns/campaigns/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Campaign id","required":true,"schema":{"type":"string","example":"6009a1ea1f6a61d88e80a867"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/campaigns/campaigns/{id}", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateCampaignById(self, company_id=None, application_id=None, id=None, body=""):
        """Update campaign by id
        :param company_id : Company id : type string
        :param application_id : Application id : type string
        :param id : Campaign id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.updateCampaignById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.CampaignReq import CampaignReq
        schema = CampaignReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/campaigns/campaigns/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Campaign id","required":true,"schema":{"type":"string","example":"6009a1ea1f6a61d88e80a867"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/campaigns/campaigns/{id}", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getStatsOfCampaignById(self, company_id=None, application_id=None, id=None, body=""):
        """Get stats of campaign by id
        :param company_id : Company id : type string
        :param application_id : Application id : type string
        :param id : Campaign id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.getStatsOfCampaignById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/campaigns/get-stats/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Campaign id","required":true,"schema":{"type":"string","example":"6009a1ea1f6a61d88e80a867"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/campaigns/get-stats/{id}", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getAudiences(self, company_id=None, application_id=None, page_no=None, page_size=None, sort=None, body=""):
        """Get audiences
        :param company_id : Company id : type string
        :param application_id : Application id : type string
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if sort:
            payload["sort"] = sort
        

        # Parameter validation
        schema = CommunicationValidator.getAudiences()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/sources/datasources", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"headers":[]}""", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, sort=sort)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, sort=sort)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/sources/datasources", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, sort=sort), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createAudience(self, company_id=None, application_id=None, body=""):
        """Create audience
        :param company_id : Company id : type string
        :param application_id : Application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = CommunicationValidator.createAudience()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.AudienceReq import AudienceReq
        schema = AudienceReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/sources/datasources", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/sources/datasources", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getBigqueryHeaders(self, company_id=None, application_id=None, body=""):
        """Get bigquery headers
        :param company_id : Company id : type string
        :param application_id : Application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = CommunicationValidator.getBigqueryHeaders()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.BigqueryHeadersReq import BigqueryHeadersReq
        schema = BigqueryHeadersReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/sources/bigquery-headers", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/sources/bigquery-headers", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getAudienceById(self, company_id=None, application_id=None, id=None, body=""):
        """Get audience by id
        :param company_id : Company id : type string
        :param application_id : Application id : type string
        :param id : Audience id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.getAudienceById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/sources/datasources/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Audience id","required":true,"schema":{"type":"string","example":"5fb6675c09fd901023917a5f"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/sources/datasources/{id}", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateAudienceById(self, company_id=None, application_id=None, id=None, body=""):
        """Update audience by id
        :param company_id : Company id : type string
        :param application_id : Application id : type string
        :param id : Audience id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.updateAudienceById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.AudienceReq import AudienceReq
        schema = AudienceReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/sources/datasources/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Audience id","required":true,"schema":{"type":"string","example":"5fb6675c09fd901023917a5f"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/sources/datasources/{id}", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getNSampleRecordsFromCsv(self, company_id=None, application_id=None, body=""):
        """Get n sample records from csv
        :param company_id : Company id : type string
        :param application_id : Application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = CommunicationValidator.getNSampleRecordsFromCsv()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.GetNRecordsCsvReq import GetNRecordsCsvReq
        schema = GetNRecordsCsvReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/sources/get-n-records", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/sources/get-n-records", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getEmailProviders(self, company_id=None, application_id=None, page_no=None, page_size=None, sort=None, body=""):
        """Get email providers
        :param company_id : Company id : type string
        :param application_id : Application id : type string
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if sort:
            payload["sort"] = sort
        

        # Parameter validation
        schema = CommunicationValidator.getEmailProviders()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/email/providers", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"headers":[]}""", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, sort=sort)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, sort=sort)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/email/providers", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, sort=sort), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createEmailProvider(self, company_id=None, application_id=None, body=""):
        """Create email provider
        :param company_id : Company id : type string
        :param application_id : Application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = CommunicationValidator.createEmailProvider()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.EmailProviderReq import EmailProviderReq
        schema = EmailProviderReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/email/providers", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/email/providers", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getEmailProviderById(self, company_id=None, application_id=None, id=None, body=""):
        """Get email provider by id
        :param company_id : Company id : type string
        :param application_id : Application id : type string
        :param id : Email provider id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.getEmailProviderById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/email/providers/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Email provider id","required":true,"schema":{"type":"string","example":"5fd9fd44c474a7e3d5d376d6"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/email/providers/{id}", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateEmailProviderById(self, company_id=None, application_id=None, id=None, body=""):
        """Update email provider by id
        :param company_id : Company id : type string
        :param application_id : Application id : type string
        :param id : Email provider id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.updateEmailProviderById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.EmailProviderReq import EmailProviderReq
        schema = EmailProviderReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/email/providers/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Email provider id","required":true,"schema":{"type":"string","example":"5fd9fd44c474a7e3d5d376d6"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/email/providers/{id}", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getEmailTemplates(self, company_id=None, application_id=None, page_no=None, page_size=None, sort=None, body=""):
        """Get email templates
        :param company_id : Company id : type string
        :param application_id : Application id : type string
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if sort:
            payload["sort"] = sort
        

        # Parameter validation
        schema = CommunicationValidator.getEmailTemplates()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/email/templates", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"headers":[]}""", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, sort=sort)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, sort=sort)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/email/templates", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, sort=sort), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createEmailTemplate(self, company_id=None, application_id=None, body=""):
        """Create email template
        :param company_id : Company id : type string
        :param application_id : Application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = CommunicationValidator.createEmailTemplate()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.EmailTemplateReq import EmailTemplateReq
        schema = EmailTemplateReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/email/templates", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/email/templates", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getSystemEmailTemplates(self, company_id=None, application_id=None, page_no=None, page_size=None, sort=None, body=""):
        """Get system email templates
        :param company_id : Company id : type string
        :param application_id : Application id : type string
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if sort:
            payload["sort"] = sort
        

        # Parameter validation
        schema = CommunicationValidator.getSystemEmailTemplates()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/email/system-templates", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"headers":[]}""", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, sort=sort)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, sort=sort)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/email/system-templates", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, sort=sort), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getEmailTemplateById(self, company_id=None, application_id=None, id=None, body=""):
        """Get email template by id
        :param company_id : Company id : type string
        :param application_id : Application id : type string
        :param id : Email template id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.getEmailTemplateById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/email/templates/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Email template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/email/templates/{id}", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateEmailTemplateById(self, company_id=None, application_id=None, id=None, body=""):
        """Update email template by id
        :param company_id : Company id : type string
        :param application_id : Application id : type string
        :param id : Email template id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.updateEmailTemplateById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.EmailTemplateReq import EmailTemplateReq
        schema = EmailTemplateReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/email/templates/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Email template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/email/templates/{id}", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def deleteEmailTemplateById(self, company_id=None, application_id=None, id=None, body=""):
        """Delete email template by id
        :param company_id : Company id : type string
        :param application_id : Application id : type string
        :param id : Email template id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.deleteEmailTemplateById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/email/templates/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Email template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/email/templates/{id}", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getEventSubscriptions(self, company_id=None, application_id=None, page_no=None, page_size=None, populate=None, body=""):
        """Get event subscriptions
        :param company_id : Company id : type string
        :param application_id : Application id : type string
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param populate : populate fields : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if populate:
            payload["populate"] = populate
        

        # Parameter validation
        schema = CommunicationValidator.getEventSubscriptions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/event/event-subscriptions", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"populate","in":"query","schema":{"type":"string"},"description":"populate fields"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"populate","in":"query","schema":{"type":"string"},"description":"populate fields"}],"headers":[]}""", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, populate=populate)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, populate=populate)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/event/event-subscriptions", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, populate=populate), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getJobs(self, company_id=None, application_id=None, page_no=None, page_size=None, sort=None, body=""):
        """Get jobs
        :param company_id : Company id : type string
        :param application_id : Application id : type string
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if sort:
            payload["sort"] = sort
        

        # Parameter validation
        schema = CommunicationValidator.getJobs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/jobs/jobs", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"headers":[]}""", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, sort=sort)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, sort=sort)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/jobs/jobs", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, sort=sort), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def triggerCampaignJob(self, company_id=None, application_id=None, body=""):
        """Trigger campaign job
        :param company_id : Company id : type string
        :param application_id : Application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = CommunicationValidator.triggerCampaignJob()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.TriggerJobRequest import TriggerJobRequest
        schema = TriggerJobRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/jobs/trigger-job", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/jobs/trigger-job", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getJobLogs(self, company_id=None, application_id=None, page_no=None, page_size=None, sort=None, body=""):
        """Get job logs
        :param company_id : Company id : type string
        :param application_id : Application id : type string
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if sort:
            payload["sort"] = sort
        

        # Parameter validation
        schema = CommunicationValidator.getJobLogs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/jobs/logs", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"headers":[]}""", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, sort=sort)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, sort=sort)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/jobs/logs", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, sort=sort), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getCommunicationLogs(self, company_id=None, application_id=None, page_id=None, page_size=None, sort=None, query=None, body=""):
        """Get communication logs
        :param company_id : Company id : type string
        :param application_id : Application id : type string
        :param page_id : Current page no : type string
        :param page_size : Current request items count : type integer
        :param sort : To sort based on _id : type object
        :param query :  : type object
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if page_id:
            payload["page_id"] = page_id
        
        if page_size:
            payload["page_size"] = page_size
        
        if sort:
            payload["sort"] = sort
        
        if query:
            payload["query"] = query
        

        # Parameter validation
        schema = CommunicationValidator.getCommunicationLogs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/log", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[{"name":"page_id","in":"query","schema":{"type":"string"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"_id":{"type":"integer"}}},"description":"To sort based on _id"},{"name":"query","in":"query","schema":{"type":"object"}}],"query":[{"name":"page_id","in":"query","schema":{"type":"string"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"_id":{"type":"integer"}}},"description":"To sort based on _id"},{"name":"query","in":"query","schema":{"type":"object"}}],"headers":[]}""", company_id=company_id, application_id=application_id, page_id=page_id, page_size=page_size, sort=sort, query=query)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, page_id=page_id, page_size=page_size, sort=sort, query=query)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/log", company_id=company_id, application_id=application_id, page_id=page_id, page_size=page_size, sort=sort, query=query), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getSystemNotifications(self, company_id=None, page_no=None, page_size=None, body=""):
        """Get system notifications
        :param company_id : Company id : type string
        :param page_no :  : type integer
        :param page_size :  : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = CommunicationValidator.getSystemNotifications()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/notification/system-notifications/", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}}],"optional":[{"in":"query","name":"page_no","schema":{"type":"integer","format":"int32","example":1}},{"in":"query","name":"page_size","schema":{"type":"integer","format":"int32","example":10}}],"query":[{"in":"query","name":"page_no","schema":{"type":"integer","format":"int32","example":1}},{"in":"query","name":"page_size","schema":{"type":"integer","format":"int32","example":10}}],"headers":[]}""", company_id=company_id, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(company_id=company_id, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/notification/system-notifications/", company_id=company_id, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getSmsProviders(self, company_id=None, application_id=None, page_no=None, page_size=None, sort=None, body=""):
        """Get sms providers
        :param company_id : Company id : type string
        :param application_id : Application id : type string
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if sort:
            payload["sort"] = sort
        

        # Parameter validation
        schema = CommunicationValidator.getSmsProviders()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/sms/providers", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"headers":[]}""", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, sort=sort)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, sort=sort)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/sms/providers", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, sort=sort), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createSmsProvider(self, company_id=None, application_id=None, body=""):
        """Create sms provider
        :param company_id : Company id : type string
        :param application_id : Application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = CommunicationValidator.createSmsProvider()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.SmsProviderReq import SmsProviderReq
        schema = SmsProviderReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/sms/providers", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/sms/providers", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getSmsProviderById(self, company_id=None, application_id=None, id=None, body=""):
        """Get sms provider by id
        :param company_id : Company id : type string
        :param application_id : Application id : type string
        :param id : Sms provider id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.getSmsProviderById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/sms/providers/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Sms provider id","required":true,"schema":{"type":"string","example":"5fd9fd07c474a7710dd376d5"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/sms/providers/{id}", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateSmsProviderById(self, company_id=None, application_id=None, id=None, body=""):
        """Update sms provider by id
        :param company_id : Company id : type string
        :param application_id : Application id : type string
        :param id : Sms provider id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.updateSmsProviderById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.SmsProviderReq import SmsProviderReq
        schema = SmsProviderReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/sms/providers/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Sms provider id","required":true,"schema":{"type":"string","example":"5fd9fd07c474a7710dd376d5"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/sms/providers/{id}", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getSmsTemplates(self, company_id=None, application_id=None, page_no=None, page_size=None, sort=None, body=""):
        """Get sms templates
        :param company_id : Company id : type string
        :param application_id : Application id : type string
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if sort:
            payload["sort"] = sort
        

        # Parameter validation
        schema = CommunicationValidator.getSmsTemplates()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/sms/templates", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"headers":[]}""", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, sort=sort)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, sort=sort)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/sms/templates", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, sort=sort), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createSmsTemplate(self, company_id=None, application_id=None, body=""):
        """Create sms template
        :param company_id : Company id : type string
        :param application_id : Application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = CommunicationValidator.createSmsTemplate()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.SmsTemplateReq import SmsTemplateReq
        schema = SmsTemplateReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/sms/templates", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/sms/templates", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getSmsTemplateById(self, company_id=None, application_id=None, id=None, body=""):
        """Get sms template by id
        :param company_id : Company id : type string
        :param application_id : Application id : type string
        :param id : Sms template id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.getSmsTemplateById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/sms/templates/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Sms template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/sms/templates/{id}", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateSmsTemplateById(self, company_id=None, application_id=None, id=None, body=""):
        """Update sms template by id
        :param company_id : Company id : type string
        :param application_id : Application id : type string
        :param id : Sms template id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.updateSmsTemplateById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.SmsTemplateReq import SmsTemplateReq
        schema = SmsTemplateReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/sms/templates/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Sms template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/sms/templates/{id}", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def deleteSmsTemplateById(self, company_id=None, application_id=None, id=None, body=""):
        """Delete sms template by id
        :param company_id : Company id : type string
        :param application_id : Application id : type string
        :param id : Sms template id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.deleteSmsTemplateById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/sms/templates/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Sms template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/sms/templates/{id}", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getSystemSystemTemplates(self, company_id=None, application_id=None, page_no=None, page_size=None, sort=None, body=""):
        """Get system sms templates
        :param company_id : Company id : type string
        :param application_id : Application id : type string
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if sort:
            payload["sort"] = sort
        

        # Parameter validation
        schema = CommunicationValidator.getSystemSystemTemplates()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/sms/system-templates", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"headers":[]}""", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, sort=sort)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, sort=sort)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/communication/v1.0/company/{company_id}/application/{application_id}/sms/system-templates", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, sort=sort), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    

class Payment:
    def __init__(self, config):
        self._conf = config
    # async def ():
    
    async def getBrandPaymentGatewayConfig(self, company_id=None, application_id=None, body=""):
        """Get All Brand Payment Gateway Config Secret
        :param company_id : Company Id : type integer
        :param application_id : Application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = PaymentValidator.getBrandPaymentGatewayConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/payment/v1.0/company/{company_id}/application/{application_id}/aggregator/request", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/payment/v1.0/company/{company_id}/application/{application_id}/aggregator/request", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def saveBrandPaymentGatewayConfig(self, company_id=None, application_id=None, body=""):
        """Save Config Secret For Brand Payment Gateway
        :param company_id : Company Id : type integer
        :param application_id : Application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = PaymentValidator.saveBrandPaymentGatewayConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.PaymentGatewayConfigRequest import PaymentGatewayConfigRequest
        schema = PaymentGatewayConfigRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/payment/v1.0/company/{company_id}/application/{application_id}/aggregator/request", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/payment/v1.0/company/{company_id}/application/{application_id}/aggregator/request", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateBrandPaymentGatewayConfig(self, company_id=None, application_id=None, body=""):
        """Save Config Secret For Brand Payment Gateway
        :param company_id : Company Id : type integer
        :param application_id : Application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = PaymentValidator.updateBrandPaymentGatewayConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.PaymentGatewayConfigRequest import PaymentGatewayConfigRequest
        schema = PaymentGatewayConfigRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/payment/v1.0/company/{company_id}/application/{application_id}/aggregator/request", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/payment/v1.0/company/{company_id}/application/{application_id}/aggregator/request", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getPaymentModeRoutes(self, company_id=None, application_id=None, refresh=None, request_type=None, body=""):
        """Use this API to get Get All Valid Payment Options for making payment
        :param company_id : Company Id : type integer
        :param application_id : Application id : type string
        :param refresh :  : type boolean
        :param request_type :  : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if refresh:
            payload["refresh"] = refresh
        
        if request_type:
            payload["request_type"] = request_type
        

        # Parameter validation
        schema = PaymentValidator.getPaymentModeRoutes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/payment/v1.0/company/{company_id}/application/{application_id}/payment/options", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true},{"name":"refresh","in":"query","required":true,"schema":{"type":"boolean"}},{"name":"request_type","in":"query","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"refresh","in":"query","required":true,"schema":{"type":"boolean"}},{"name":"request_type","in":"query","required":true,"schema":{"type":"string"}}],"headers":[]}""", company_id=company_id, application_id=application_id, refresh=refresh, request_type=request_type)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, refresh=refresh, request_type=request_type)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/payment/v1.0/company/{company_id}/application/{application_id}/payment/options", company_id=company_id, application_id=application_id, refresh=refresh, request_type=request_type), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getAllPayouts(self, company_id=None, unique_external_id=None, body=""):
        """Get All Payouts
        :param company_id : Company Id : type integer
        :param unique_external_id : Fetch payouts using unique external id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if unique_external_id:
            payload["unique_external_id"] = unique_external_id
        

        # Parameter validation
        schema = PaymentValidator.getAllPayouts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/payment/v1.0/company/{company_id}/payouts", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true}],"optional":[{"name":"unique_external_id","in":"query","description":"Fetch payouts using unique external id","schema":{"type":"string"}}],"query":[{"name":"unique_external_id","in":"query","description":"Fetch payouts using unique external id","schema":{"type":"string"}}],"headers":[]}""", company_id=company_id, unique_external_id=unique_external_id)
        query_string = await create_query_string(company_id=company_id, unique_external_id=unique_external_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/payment/v1.0/company/{company_id}/payouts", company_id=company_id, unique_external_id=unique_external_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def savePayout(self, company_id=None, body=""):
        """Save Payout
        :param company_id : Company Id : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = PaymentValidator.savePayout()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.PayoutRequest import PayoutRequest
        schema = PayoutRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/payment/v1.0/company/{company_id}/payouts", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/payment/v1.0/company/{company_id}/payouts", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updatePayout(self, company_id=None, unique_transfer_no=None, body=""):
        """Update Payout
        :param company_id : Company Id : type integer
        :param unique_transfer_no : Unique transfer id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if unique_transfer_no:
            payload["unique_transfer_no"] = unique_transfer_no
        

        # Parameter validation
        schema = PaymentValidator.updatePayout()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.PayoutRequest import PayoutRequest
        schema = PayoutRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/payment/v1.0/company/{company_id}/payouts/{unique_transfer_no}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"unique_transfer_no","in":"path","description":"Unique transfer id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, unique_transfer_no=unique_transfer_no)
        query_string = await create_query_string(company_id=company_id, unique_transfer_no=unique_transfer_no)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/payment/v1.0/company/{company_id}/payouts/{unique_transfer_no}", company_id=company_id, unique_transfer_no=unique_transfer_no), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def activateAndDectivatePayout(self, company_id=None, unique_transfer_no=None, body=""):
        """Partial Update Payout
        :param company_id : Company Id : type integer
        :param unique_transfer_no : Unique transfer id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if unique_transfer_no:
            payload["unique_transfer_no"] = unique_transfer_no
        

        # Parameter validation
        schema = PaymentValidator.activateAndDectivatePayout()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.UpdatePayoutRequest import UpdatePayoutRequest
        schema = UpdatePayoutRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/payment/v1.0/company/{company_id}/payouts/{unique_transfer_no}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"unique_transfer_no","in":"path","description":"Unique transfer id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, unique_transfer_no=unique_transfer_no)
        query_string = await create_query_string(company_id=company_id, unique_transfer_no=unique_transfer_no)
        return await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain("/service/platform/payment/v1.0/company/{company_id}/payouts/{unique_transfer_no}", company_id=company_id, unique_transfer_no=unique_transfer_no), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def deletePayout(self, company_id=None, unique_transfer_no=None, body=""):
        """Delete Payout
        :param company_id : Company Id : type integer
        :param unique_transfer_no : Unique transfer id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if unique_transfer_no:
            payload["unique_transfer_no"] = unique_transfer_no
        

        # Parameter validation
        schema = PaymentValidator.deletePayout()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/payment/v1.0/company/{company_id}/payouts/{unique_transfer_no}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"unique_transfer_no","in":"path","description":"Unique transfer id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, unique_transfer_no=unique_transfer_no)
        query_string = await create_query_string(company_id=company_id, unique_transfer_no=unique_transfer_no)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain("/service/platform/payment/v1.0/company/{company_id}/payouts/{unique_transfer_no}", company_id=company_id, unique_transfer_no=unique_transfer_no), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getSubscriptionPaymentMethod(self, company_id=None, unique_external_id=None, body=""):
        """Get all  Subscription  Payment Method
        :param company_id : Company Id : type integer
        :param unique_external_id : Unique external id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if unique_external_id:
            payload["unique_external_id"] = unique_external_id
        

        # Parameter validation
        schema = PaymentValidator.getSubscriptionPaymentMethod()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/payment/v1.0/company/{company_id}/subscription/methods", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true}],"optional":[{"name":"unique_external_id","in":"query","description":"Unique external id","schema":{"type":"string"}}],"query":[{"name":"unique_external_id","in":"query","description":"Unique external id","schema":{"type":"string"}}],"headers":[]}""", company_id=company_id, unique_external_id=unique_external_id)
        query_string = await create_query_string(company_id=company_id, unique_external_id=unique_external_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/payment/v1.0/company/{company_id}/subscription/methods", company_id=company_id, unique_external_id=unique_external_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def deleteSubscriptionPaymentMethod(self, company_id=None, unique_external_id=None, payment_method_id=None, body=""):
        """Uses this api to Delete Subscription Payment Method
        :param company_id : Company Id : type integer
        :param unique_external_id :  : type string
        :param payment_method_id :  : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if unique_external_id:
            payload["unique_external_id"] = unique_external_id
        
        if payment_method_id:
            payload["payment_method_id"] = payment_method_id
        

        # Parameter validation
        schema = PaymentValidator.deleteSubscriptionPaymentMethod()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/payment/v1.0/company/{company_id}/subscription/methods", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"unique_external_id","in":"query","required":true,"schema":{"type":"string"}},{"name":"payment_method_id","in":"query","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"unique_external_id","in":"query","required":true,"schema":{"type":"string"}},{"name":"payment_method_id","in":"query","required":true,"schema":{"type":"string"}}],"headers":[]}""", company_id=company_id, unique_external_id=unique_external_id, payment_method_id=payment_method_id)
        query_string = await create_query_string(company_id=company_id, unique_external_id=unique_external_id, payment_method_id=payment_method_id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain("/service/platform/payment/v1.0/company/{company_id}/subscription/methods", company_id=company_id, unique_external_id=unique_external_id, payment_method_id=payment_method_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getSubscriptionConfig(self, company_id=None, body=""):
        """Get all  Subscription Config details
        :param company_id : Company Id : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = PaymentValidator.getSubscriptionConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/payment/v1.0/company/{company_id}/subscription/configs", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/payment/v1.0/company/{company_id}/subscription/configs", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def saveSubscriptionSetupIntent(self, company_id=None, body=""):
        """Uses this api to Save Subscription Setup Intent
        :param company_id : Company Id : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = PaymentValidator.saveSubscriptionSetupIntent()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.SaveSubscriptionSetupIntentRequest import SaveSubscriptionSetupIntentRequest
        schema = SaveSubscriptionSetupIntentRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/payment/v1.0/company/{company_id}/subscription/setup/intent", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/payment/v1.0/company/{company_id}/subscription/setup/intent", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def addBeneficiaryDetails(self, company_id=None, application_id=None, body=""):
        """Use this API to save bank details for returned/cancelled order to refund amount in his account.
        :param company_id : Company Id : type integer
        :param application_id : Application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = PaymentValidator.addBeneficiaryDetails()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.AddBeneficiaryDetailsRequest import AddBeneficiaryDetailsRequest
        schema = AddBeneficiaryDetailsRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/payment/v1.0/company/{company_id}/application/{application_id}/refund/account", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/payment/v1.0/company/{company_id}/application/{application_id}/refund/account", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def verifyIfscCode(self, company_id=None, ifsc_code=None, body=""):
        """Get True/False for correct IFSC Code for adding bank details for refund
        :param company_id : Company Id : type integer
        :param ifsc_code :  : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if ifsc_code:
            payload["ifsc_code"] = ifsc_code
        

        # Parameter validation
        schema = PaymentValidator.verifyIfscCode()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/payment/v1.0/company/{company_id}/ifsc-code/verify", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true}],"optional":[{"name":"ifsc_code","in":"query","schema":{"type":"string","description":"Fetch bank details for correct ifsc code"}}],"query":[{"name":"ifsc_code","in":"query","schema":{"type":"string","description":"Fetch bank details for correct ifsc code"}}],"headers":[]}""", company_id=company_id, ifsc_code=ifsc_code)
        query_string = await create_query_string(company_id=company_id, ifsc_code=ifsc_code)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/payment/v1.0/company/{company_id}/ifsc-code/verify", company_id=company_id, ifsc_code=ifsc_code), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getUserOrderBeneficiaries(self, order_id=None, company_id=None, application_id=None, body=""):
        """Get all active  beneficiary details added by the user for refund
        :param order_id :  : type string
        :param company_id : Company Id : type integer
        :param application_id : Application id : type string
        """
        payload = {}
        
        if order_id:
            payload["order_id"] = order_id
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = PaymentValidator.getUserOrderBeneficiaries()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/payment/v1.0/company/{company_id}/application/{application_id}/refund/accounts/order", """{"required":[{"in":"query","name":"order_id","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[{"in":"query","name":"order_id","required":true,"schema":{"type":"string"}}],"headers":[]}""", order_id=order_id, company_id=company_id, application_id=application_id)
        query_string = await create_query_string(order_id=order_id, company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/payment/v1.0/company/{company_id}/application/{application_id}/refund/accounts/order", order_id=order_id, company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getUserBeneficiaries(self, order_id=None, company_id=None, application_id=None, body=""):
        """Get all active  beneficiary details added by the user for refund
        :param order_id :  : type string
        :param company_id : Company Id : type integer
        :param application_id : Application id : type string
        """
        payload = {}
        
        if order_id:
            payload["order_id"] = order_id
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = PaymentValidator.getUserBeneficiaries()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/payment/v1.0/company/{company_id}/application/{application_id}/refund/accounts/user", """{"required":[{"in":"query","name":"order_id","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[{"in":"query","name":"order_id","required":true,"schema":{"type":"string"}}],"headers":[]}""", order_id=order_id, company_id=company_id, application_id=application_id)
        query_string = await create_query_string(order_id=order_id, company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/payment/v1.0/company/{company_id}/application/{application_id}/refund/accounts/user", order_id=order_id, company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def confirmPayment(self, company_id=None, application_id=None, body=""):
        """Use this API to confirm payment after payment gateway accepted payment.
        :param company_id : Company Id : type integer
        :param application_id : Application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = PaymentValidator.confirmPayment()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.PaymentConfirmationRequest import PaymentConfirmationRequest
        schema = PaymentConfirmationRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/payment/v1.0/company/{company_id}/application/{application_id}/payment/confirm", """{"required":[{"name":"company_id","in":"path","description":"Company Id","schema":{"type":"integer"},"required":true},{"name":"application_id","in":"path","description":"Application id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/payment/v1.0/company/{company_id}/application/{application_id}/payment/confirm", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    

class Order:
    def __init__(self, config):
        self._conf = config
    # async def ():
    
    async def shipmentStatusUpdate(self, company_id=None, body=""):
        """Update Shipment Status
        :param company_id : Company Id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = OrderValidator.shipmentStatusUpdate()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.UpdateShipmentStatusBody import UpdateShipmentStatusBody
        schema = UpdateShipmentStatusBody()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/order/v1.0/company/{company_id}/actions/status", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/order/v1.0/company/{company_id}/actions/status", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def activityStatus(self, company_id=None, bag_id=None, body=""):
        """Get Activity Status
        :param company_id : Company Id : type string
        :param bag_id : Bag Id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if bag_id:
            payload["bag_id"] = bag_id
        

        # Parameter validation
        schema = OrderValidator.activityStatus()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/order/v1.0/company/{company_id}/actions/activity/status", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"bag_id","in":"query","description":"Bag Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"bag_id","in":"query","description":"Bag Id","required":true,"schema":{"type":"string"}}],"headers":[]}""", company_id=company_id, bag_id=bag_id)
        query_string = await create_query_string(company_id=company_id, bag_id=bag_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/order/v1.0/company/{company_id}/actions/activity/status", company_id=company_id, bag_id=bag_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def storeProcessShipmentUpdate(self, company_id=None, body=""):
        """Update Store Process-Shipment
        :param company_id : Company Id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = OrderValidator.storeProcessShipmentUpdate()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.UpdateProcessShipmenstRequestBody import UpdateProcessShipmenstRequestBody
        schema = UpdateProcessShipmenstRequestBody()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/order/v1.0/company/{company_id}/actions/store/process-shipments", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/order/v1.0/company/{company_id}/actions/store/process-shipments", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def checkRefund(self, company_id=None, shipment_id=None, body=""):
        """Check Refund is available or not
        :param company_id : Company Id : type string
        :param shipment_id : Shipment Id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        

        # Parameter validation
        schema = OrderValidator.checkRefund()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/order/v1.0/company/{company_id}/actions/check-refund/{shipment_id}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"Shipment Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, shipment_id=shipment_id)
        query_string = await create_query_string(company_id=company_id, shipment_id=shipment_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/order/v1.0/company/{company_id}/actions/check-refund/{shipment_id}", company_id=company_id, shipment_id=shipment_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def ShipmentBagsCanBreak(self, company_id=None, body=""):
        """Decides if Shipment bags can break
        :param company_id : Company Id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = OrderValidator.ShipmentBagsCanBreak()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.CanBreakRequestBody import CanBreakRequestBody
        schema = CanBreakRequestBody()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/order/v1.0/company/{company_id}/actions/can-break", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/order/v1.0/company/{company_id}/actions/can-break", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getOrdersByCompanyId(self, company_id=None, page_no=None, page_size=None, from_date=None, to_date=None, is_priority_sort=None, lock_status=None, q=None, stage=None, sales_channels=None, order_id=None, stores=None, deployment_stores=None, status=None, dp=None, shorten_urls=None, filter_type=None, body=""):
        """Get Orders
        :param company_id : Company Id : type string
        :param page_no : Current page number : type string
        :param page_size : Page limit : type string
        :param from_date : From Date : type string
        :param to_date : To Date : type string
        :param is_priority_sort : Sorting Order : type boolean
        :param lock_status : Hide Lock Status : type boolean
        :param q : Keyword for Search : type string
        :param stage : Specefic Order Stage : type string
        :param sales_channels : Selected Sales Channel : type string
        :param order_id : Order Id : type string
        :param stores : Selected Stores : type string
        :param deployment_stores : Selected Deployment Stores : type string
        :param status : Status of order : type string
        :param dp : Delivery Partners : type string
        :param shorten_urls : Shorten URL option : type boolean
        :param filter_type : Filters : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if from_date:
            payload["from_date"] = from_date
        
        if to_date:
            payload["to_date"] = to_date
        
        if is_priority_sort:
            payload["is_priority_sort"] = is_priority_sort
        
        if lock_status:
            payload["lock_status"] = lock_status
        
        if q:
            payload["q"] = q
        
        if stage:
            payload["stage"] = stage
        
        if sales_channels:
            payload["sales_channels"] = sales_channels
        
        if order_id:
            payload["order_id"] = order_id
        
        if stores:
            payload["stores"] = stores
        
        if deployment_stores:
            payload["deployment_stores"] = deployment_stores
        
        if status:
            payload["status"] = status
        
        if dp:
            payload["dp"] = dp
        
        if shorten_urls:
            payload["shorten_urls"] = shorten_urls
        
        if filter_type:
            payload["filter_type"] = filter_type
        

        # Parameter validation
        schema = OrderValidator.getOrdersByCompanyId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/order/v1.0/company/{company_id}/orders", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"Page limit","required":false,"schema":{"type":"string"}},{"name":"from_date","in":"query","description":"From Date","required":false,"schema":{"type":"string"}},{"name":"to_date","in":"query","description":"To Date","required":false,"schema":{"type":"string"}},{"name":"is_priority_sort","in":"query","description":"Sorting Order","required":false,"schema":{"type":"boolean"}},{"name":"lock_status","in":"query","description":"Hide Lock Status","required":false,"schema":{"type":"boolean"}},{"name":"q","in":"query","description":"Keyword for Search","required":false,"schema":{"type":"string"}},{"name":"stage","in":"query","description":"Specefic Order Stage","required":false,"schema":{"type":"string"}},{"name":"sales_channels","in":"query","description":"Selected Sales Channel","required":false,"schema":{"type":"string"}},{"name":"order_id","in":"query","description":"Order Id","required":false,"schema":{"type":"string"}},{"name":"stores","in":"query","description":"Selected Stores","required":false,"schema":{"type":"string"}},{"name":"deployment_stores","in":"query","description":"Selected Deployment Stores","required":false,"schema":{"type":"string"}},{"name":"status","in":"query","description":"Status of order","required":false,"schema":{"type":"string"}},{"name":"dp","in":"query","description":"Delivery Partners","required":false,"schema":{"type":"string"}},{"name":"shorten_urls","in":"query","description":"Shorten URL option","required":false,"schema":{"type":"boolean"}},{"name":"filter_type","in":"query","description":"Filters","required":false,"schema":{"type":"string"}}],"query":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"Page limit","required":false,"schema":{"type":"string"}},{"name":"from_date","in":"query","description":"From Date","required":false,"schema":{"type":"string"}},{"name":"to_date","in":"query","description":"To Date","required":false,"schema":{"type":"string"}},{"name":"is_priority_sort","in":"query","description":"Sorting Order","required":false,"schema":{"type":"boolean"}},{"name":"lock_status","in":"query","description":"Hide Lock Status","required":false,"schema":{"type":"boolean"}},{"name":"q","in":"query","description":"Keyword for Search","required":false,"schema":{"type":"string"}},{"name":"stage","in":"query","description":"Specefic Order Stage","required":false,"schema":{"type":"string"}},{"name":"sales_channels","in":"query","description":"Selected Sales Channel","required":false,"schema":{"type":"string"}},{"name":"order_id","in":"query","description":"Order Id","required":false,"schema":{"type":"string"}},{"name":"stores","in":"query","description":"Selected Stores","required":false,"schema":{"type":"string"}},{"name":"deployment_stores","in":"query","description":"Selected Deployment Stores","required":false,"schema":{"type":"string"}},{"name":"status","in":"query","description":"Status of order","required":false,"schema":{"type":"string"}},{"name":"dp","in":"query","description":"Delivery Partners","required":false,"schema":{"type":"string"}},{"name":"shorten_urls","in":"query","description":"Shorten URL option","required":false,"schema":{"type":"boolean"}},{"name":"filter_type","in":"query","description":"Filters","required":false,"schema":{"type":"string"}}],"headers":[]}""", company_id=company_id, page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, is_priority_sort=is_priority_sort, lock_status=lock_status, q=q, stage=stage, sales_channels=sales_channels, order_id=order_id, stores=stores, deployment_stores=deployment_stores, status=status, dp=dp, shorten_urls=shorten_urls, filter_type=filter_type)
        query_string = await create_query_string(company_id=company_id, page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, is_priority_sort=is_priority_sort, lock_status=lock_status, q=q, stage=stage, sales_channels=sales_channels, order_id=order_id, stores=stores, deployment_stores=deployment_stores, status=status, dp=dp, shorten_urls=shorten_urls, filter_type=filter_type)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/order/v1.0/company/{company_id}/orders", company_id=company_id, page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, is_priority_sort=is_priority_sort, lock_status=lock_status, q=q, stage=stage, sales_channels=sales_channels, order_id=order_id, stores=stores, deployment_stores=deployment_stores, status=status, dp=dp, shorten_urls=shorten_urls, filter_type=filter_type), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getOrderLanesCountByCompanyId(self, company_id=None, page_no=None, page_size=None, from_date=None, to_date=None, q=None, stage=None, sales_channels=None, order_id=None, stores=None, status=None, shorten_urls=None, filter_type=None, body=""):
        """Get Orders Seperate Lane Count
        :param company_id : Company Id : type string
        :param page_no : Current page number : type string
        :param page_size : Page limit : type string
        :param from_date : From Date : type string
        :param to_date : To Date : type string
        :param q : Keyword for Search : type string
        :param stage : Specefic Order Stage : type string
        :param sales_channels : Selected Sales Channel : type string
        :param order_id : Order Id : type string
        :param stores : Selected Stores : type string
        :param status : Status of order : type string
        :param shorten_urls : Shorten URL option : type boolean
        :param filter_type : Filters : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if from_date:
            payload["from_date"] = from_date
        
        if to_date:
            payload["to_date"] = to_date
        
        if q:
            payload["q"] = q
        
        if stage:
            payload["stage"] = stage
        
        if sales_channels:
            payload["sales_channels"] = sales_channels
        
        if order_id:
            payload["order_id"] = order_id
        
        if stores:
            payload["stores"] = stores
        
        if status:
            payload["status"] = status
        
        if shorten_urls:
            payload["shorten_urls"] = shorten_urls
        
        if filter_type:
            payload["filter_type"] = filter_type
        

        # Parameter validation
        schema = OrderValidator.getOrderLanesCountByCompanyId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/order/v1.0/company/{company_id}/orders/lane-count", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"Page limit","required":false,"schema":{"type":"string"}},{"name":"from_date","in":"query","description":"From Date","required":false,"schema":{"type":"string"}},{"name":"to_date","in":"query","description":"To Date","required":false,"schema":{"type":"string"}},{"name":"q","in":"query","description":"Keyword for Search","required":false,"schema":{"type":"string"}},{"name":"stage","in":"query","description":"Specefic Order Stage","required":false,"schema":{"type":"string"}},{"name":"sales_channels","in":"query","description":"Selected Sales Channel","required":false,"schema":{"type":"string"}},{"name":"order_id","in":"query","description":"Order Id","required":false,"schema":{"type":"string"}},{"name":"stores","in":"query","description":"Selected Stores","required":false,"schema":{"type":"string"}},{"name":"status","in":"query","description":"Status of order","required":false,"schema":{"type":"string"}},{"name":"shorten_urls","in":"query","description":"Shorten URL option","required":false,"schema":{"type":"boolean"}},{"name":"filter_type","in":"query","description":"Filters","required":false,"schema":{"type":"string"}}],"query":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"Page limit","required":false,"schema":{"type":"string"}},{"name":"from_date","in":"query","description":"From Date","required":false,"schema":{"type":"string"}},{"name":"to_date","in":"query","description":"To Date","required":false,"schema":{"type":"string"}},{"name":"q","in":"query","description":"Keyword for Search","required":false,"schema":{"type":"string"}},{"name":"stage","in":"query","description":"Specefic Order Stage","required":false,"schema":{"type":"string"}},{"name":"sales_channels","in":"query","description":"Selected Sales Channel","required":false,"schema":{"type":"string"}},{"name":"order_id","in":"query","description":"Order Id","required":false,"schema":{"type":"string"}},{"name":"stores","in":"query","description":"Selected Stores","required":false,"schema":{"type":"string"}},{"name":"status","in":"query","description":"Status of order","required":false,"schema":{"type":"string"}},{"name":"shorten_urls","in":"query","description":"Shorten URL option","required":false,"schema":{"type":"boolean"}},{"name":"filter_type","in":"query","description":"Filters","required":false,"schema":{"type":"string"}}],"headers":[]}""", company_id=company_id, page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, q=q, stage=stage, sales_channels=sales_channels, order_id=order_id, stores=stores, status=status, shorten_urls=shorten_urls, filter_type=filter_type)
        query_string = await create_query_string(company_id=company_id, page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, q=q, stage=stage, sales_channels=sales_channels, order_id=order_id, stores=stores, status=status, shorten_urls=shorten_urls, filter_type=filter_type)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/order/v1.0/company/{company_id}/orders/lane-count", company_id=company_id, page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, q=q, stage=stage, sales_channels=sales_channels, order_id=order_id, stores=stores, status=status, shorten_urls=shorten_urls, filter_type=filter_type), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getOrderDetails(self, company_id=None, order_id=None, next=None, previous=None, body=""):
        """Get Orders
        :param company_id : Company Id : type string
        :param order_id : Order Id : type string
        :param next : Next : type string
        :param previous : Previous : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if order_id:
            payload["order_id"] = order_id
        
        if next:
            payload["next"] = next
        
        if previous:
            payload["previous"] = previous
        

        # Parameter validation
        schema = OrderValidator.getOrderDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/order/v1.0/company/{company_id}/orders/details", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}],"optional":[{"name":"order_id","in":"query","description":"Order Id","required":false,"schema":{"type":"string"}},{"name":"next","in":"query","description":"Next","required":false,"schema":{"type":"string"}},{"name":"previous","in":"query","description":"Previous","required":false,"schema":{"type":"string"}}],"query":[{"name":"order_id","in":"query","description":"Order Id","required":false,"schema":{"type":"string"}},{"name":"next","in":"query","description":"Next","required":false,"schema":{"type":"string"}},{"name":"previous","in":"query","description":"Previous","required":false,"schema":{"type":"string"}}],"headers":[]}""", company_id=company_id, order_id=order_id, next=next, previous=previous)
        query_string = await create_query_string(company_id=company_id, order_id=order_id, next=next, previous=previous)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/order/v1.0/company/{company_id}/orders/details", company_id=company_id, order_id=order_id, next=next, previous=previous), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getPicklistOrdersByCompanyId(self, company_id=None, page_no=None, page_size=None, from_date=None, to_date=None, q=None, stage=None, sales_channels=None, order_id=None, stores=None, status=None, shorten_urls=None, filter_type=None, body=""):
        """Get Orders
        :param company_id : Company Id : type string
        :param page_no : Current page number : type string
        :param page_size : Page limit : type string
        :param from_date : From Date : type string
        :param to_date : To Date : type string
        :param q : Keyword for Search : type string
        :param stage : Specefic Order Stage : type string
        :param sales_channels : Selected Sales Channel : type string
        :param order_id : Order Id : type string
        :param stores : Selected Stores : type string
        :param status : Status of order : type string
        :param shorten_urls : Shorten URL option : type boolean
        :param filter_type : Filters : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if from_date:
            payload["from_date"] = from_date
        
        if to_date:
            payload["to_date"] = to_date
        
        if q:
            payload["q"] = q
        
        if stage:
            payload["stage"] = stage
        
        if sales_channels:
            payload["sales_channels"] = sales_channels
        
        if order_id:
            payload["order_id"] = order_id
        
        if stores:
            payload["stores"] = stores
        
        if status:
            payload["status"] = status
        
        if shorten_urls:
            payload["shorten_urls"] = shorten_urls
        
        if filter_type:
            payload["filter_type"] = filter_type
        

        # Parameter validation
        schema = OrderValidator.getPicklistOrdersByCompanyId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/order/v1.0/company/{company_id}/orders/picklist", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"Page limit","required":false,"schema":{"type":"string"}},{"name":"from_date","in":"query","description":"From Date","required":false,"schema":{"type":"string"}},{"name":"to_date","in":"query","description":"To Date","required":false,"schema":{"type":"string"}},{"name":"q","in":"query","description":"Keyword for Search","required":false,"schema":{"type":"string"}},{"name":"stage","in":"query","description":"Specefic Order Stage","required":false,"schema":{"type":"string"}},{"name":"sales_channels","in":"query","description":"Selected Sales Channel","required":false,"schema":{"type":"string"}},{"name":"order_id","in":"query","description":"Order Id","required":false,"schema":{"type":"string"}},{"name":"stores","in":"query","description":"Selected Stores","required":false,"schema":{"type":"string"}},{"name":"status","in":"query","description":"Status of order","required":false,"schema":{"type":"string"}},{"name":"shorten_urls","in":"query","description":"Shorten URL option","required":false,"schema":{"type":"boolean"}},{"name":"filter_type","in":"query","description":"Filters","required":false,"schema":{"type":"string"}}],"query":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"Page limit","required":false,"schema":{"type":"string"}},{"name":"from_date","in":"query","description":"From Date","required":false,"schema":{"type":"string"}},{"name":"to_date","in":"query","description":"To Date","required":false,"schema":{"type":"string"}},{"name":"q","in":"query","description":"Keyword for Search","required":false,"schema":{"type":"string"}},{"name":"stage","in":"query","description":"Specefic Order Stage","required":false,"schema":{"type":"string"}},{"name":"sales_channels","in":"query","description":"Selected Sales Channel","required":false,"schema":{"type":"string"}},{"name":"order_id","in":"query","description":"Order Id","required":false,"schema":{"type":"string"}},{"name":"stores","in":"query","description":"Selected Stores","required":false,"schema":{"type":"string"}},{"name":"status","in":"query","description":"Status of order","required":false,"schema":{"type":"string"}},{"name":"shorten_urls","in":"query","description":"Shorten URL option","required":false,"schema":{"type":"boolean"}},{"name":"filter_type","in":"query","description":"Filters","required":false,"schema":{"type":"string"}}],"headers":[]}""", company_id=company_id, page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, q=q, stage=stage, sales_channels=sales_channels, order_id=order_id, stores=stores, status=status, shorten_urls=shorten_urls, filter_type=filter_type)
        query_string = await create_query_string(company_id=company_id, page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, q=q, stage=stage, sales_channels=sales_channels, order_id=order_id, stores=stores, status=status, shorten_urls=shorten_urls, filter_type=filter_type)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/order/v1.0/company/{company_id}/orders/picklist", company_id=company_id, page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, q=q, stage=stage, sales_channels=sales_channels, order_id=order_id, stores=stores, status=status, shorten_urls=shorten_urls, filter_type=filter_type), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def trackShipmentPlatform(self, company_id=None, application_id=None, shipment_id=None, body=""):
        """Shipment Track
        :param company_id : Company Id : type string
        :param application_id : Application Id : type string
        :param shipment_id : Shipment Id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        

        # Parameter validation
        schema = OrderValidator.trackShipmentPlatform()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/order/v1.0/company/{company_id}/application/{application_id}/orders/shipments/{shipment_id}/track", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"Shipment Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, shipment_id=shipment_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, shipment_id=shipment_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/order/v1.0/company/{company_id}/application/{application_id}/orders/shipments/{shipment_id}/track", company_id=company_id, application_id=application_id, shipment_id=shipment_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def trackOrder(self, company_id=None, application_id=None, order_id=None, body=""):
        """Order Track
        :param company_id : Company Id : type string
        :param application_id : Application Id : type string
        :param order_id : Order Id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if order_id:
            payload["order_id"] = order_id
        

        # Parameter validation
        schema = OrderValidator.trackOrder()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/order/v1.0/company/{company_id}/application/{application_id}/orders/{order_id}/track", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"order_id","in":"path","description":"Order Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, order_id=order_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, order_id=order_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/order/v1.0/company/{company_id}/application/{application_id}/orders/{order_id}/track", company_id=company_id, application_id=application_id, order_id=order_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def failedOrders(self, company_id=None, application_id=None, body=""):
        """Failed Orders
        :param company_id : Company Id : type string
        :param application_id : Application Id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = OrderValidator.failedOrders()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/order/v1.0/company/{company_id}/application/{application_id}/orders/failed", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/order/v1.0/company/{company_id}/application/{application_id}/orders/failed", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def reprocessOrder(self, company_id=None, application_id=None, order_id=None, body=""):
        """Order Reprocess
        :param company_id : Company Id : type string
        :param application_id : Application Id : type string
        :param order_id : Order Id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if order_id:
            payload["order_id"] = order_id
        

        # Parameter validation
        schema = OrderValidator.reprocessOrder()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/order/v1.0/company/{company_id}/application/{application_id}/orders/{order_id}/reprocess", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"order_id","in":"path","description":"Order Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, order_id=order_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, order_id=order_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/order/v1.0/company/{company_id}/application/{application_id}/orders/{order_id}/reprocess", company_id=company_id, application_id=application_id, order_id=order_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateShipment(self, company_id=None, application_id=None, shipment_id=None, body=""):
        """Update the shipment
        :param company_id : Company Id : type string
        :param application_id : Application Id : type string
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        

        # Parameter validation
        schema = OrderValidator.updateShipment()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.ShipmentUpdateRequest import ShipmentUpdateRequest
        schema = ShipmentUpdateRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/order/v1.0/company/{company_id}/application/{application_id}/orders/shipments/{shipment_id}/update", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, shipment_id=shipment_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, shipment_id=shipment_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/order/v1.0/company/{company_id}/application/{application_id}/orders/shipments/{shipment_id}/update", company_id=company_id, application_id=application_id, shipment_id=shipment_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getPlatformShipmentReasons(self, company_id=None, application_id=None, action=None, body=""):
        """Get reasons behind full or partial cancellation of a shipment
        :param company_id : Company Id : type string
        :param application_id : Application Id : type string
        :param action : Action : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if action:
            payload["action"] = action
        

        # Parameter validation
        schema = OrderValidator.getPlatformShipmentReasons()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/order/v1.0/company/{company_id}/application/{application_id}/orders/shipments/reasons/{action}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"action","in":"path","description":"Action","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, action=action)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, action=action)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/order/v1.0/company/{company_id}/application/{application_id}/orders/shipments/reasons/{action}", company_id=company_id, application_id=application_id, action=action), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getShipmentTrackDetails(self, company_id=None, application_id=None, order_id=None, shipment_id=None, body=""):
        """Track shipment
        :param company_id : Company Id : type string
        :param application_id : Application Id : type string
        :param order_id : ID of the order. : type string
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if order_id:
            payload["order_id"] = order_id
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        

        # Parameter validation
        schema = OrderValidator.getShipmentTrackDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/order/v1.0/company/{company_id}/application/{application_id}/orders/{order_id}/shipments/{shipment_id}/track", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"order_id","in":"path","description":"ID of the order.","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, order_id=order_id, shipment_id=shipment_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, order_id=order_id, shipment_id=shipment_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/order/v1.0/company/{company_id}/application/{application_id}/orders/{order_id}/shipments/{shipment_id}/track", company_id=company_id, application_id=application_id, order_id=order_id, shipment_id=shipment_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getShipmentAddress(self, company_id=None, shipment_id=None, address_category=None, body=""):
        """Get Shipment Address
        :param company_id : Company Id : type string
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        :param address_category : Category of the address it falls into(billing or delivery). : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        
        if address_category:
            payload["address_category"] = address_category
        

        # Parameter validation
        schema = OrderValidator.getShipmentAddress()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/order/v1.0/company/{company_id}/orders/shipments/{shipment_id}/address/{address_category}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}},{"name":"address_category","in":"path","description":"Category of the address it falls into(billing or delivery).","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, shipment_id=shipment_id, address_category=address_category)
        query_string = await create_query_string(company_id=company_id, shipment_id=shipment_id, address_category=address_category)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/order/v1.0/company/{company_id}/orders/shipments/{shipment_id}/address/{address_category}", company_id=company_id, shipment_id=shipment_id, address_category=address_category), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateShipmentAddress(self, company_id=None, shipment_id=None, address_category=None, body=""):
        """Update Shipment Address
        :param company_id : Company Id : type string
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        :param address_category : Category of the address it falls into(billing or delivery). : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        
        if address_category:
            payload["address_category"] = address_category
        

        # Parameter validation
        schema = OrderValidator.updateShipmentAddress()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.UpdateShipmentAddressRequest import UpdateShipmentAddressRequest
        schema = UpdateShipmentAddressRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/order/v1.0/company/{company_id}/orders/shipments/{shipment_id}/address/{address_category}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}},{"name":"address_category","in":"path","description":"Category of the address it falls into(billing or delivery).","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, shipment_id=shipment_id, address_category=address_category)
        query_string = await create_query_string(company_id=company_id, shipment_id=shipment_id, address_category=address_category)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/order/v1.0/company/{company_id}/orders/shipments/{shipment_id}/address/{address_category}", company_id=company_id, shipment_id=shipment_id, address_category=address_category), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getOrdersByApplicationId(self, company_id=None, application_id=None, page_no=None, page_size=None, from_date=None, to_date=None, q=None, stage=None, sales_channels=None, order_id=None, stores=None, status=None, dp=None, shorten_urls=None, filter_type=None, body=""):
        """Get Orders at Application Level
        :param company_id : Company Id : type string
        :param application_id : Application Id : type string
        :param page_no : Current page number : type string
        :param page_size : Page limit : type string
        :param from_date : From Date : type string
        :param to_date : To Date : type string
        :param q : Keyword for Search : type string
        :param stage : Specefic Order Stage : type string
        :param sales_channels : Selected Sales Channel : type string
        :param order_id : Order Id : type string
        :param stores : Selected Stores : type string
        :param status : Status of order : type string
        :param dp : Delivery Partners : type string
        :param shorten_urls : Shorten URL option : type boolean
        :param filter_type : Filters : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if from_date:
            payload["from_date"] = from_date
        
        if to_date:
            payload["to_date"] = to_date
        
        if q:
            payload["q"] = q
        
        if stage:
            payload["stage"] = stage
        
        if sales_channels:
            payload["sales_channels"] = sales_channels
        
        if order_id:
            payload["order_id"] = order_id
        
        if stores:
            payload["stores"] = stores
        
        if status:
            payload["status"] = status
        
        if dp:
            payload["dp"] = dp
        
        if shorten_urls:
            payload["shorten_urls"] = shorten_urls
        
        if filter_type:
            payload["filter_type"] = filter_type
        

        # Parameter validation
        schema = OrderValidator.getOrdersByApplicationId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/order/v1.0/company/{company_id}/application/{application_id}/orders", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"Page limit","required":false,"schema":{"type":"string"}},{"name":"from_date","in":"query","description":"From Date","required":false,"schema":{"type":"string"}},{"name":"to_date","in":"query","description":"To Date","required":false,"schema":{"type":"string"}},{"name":"q","in":"query","description":"Keyword for Search","required":false,"schema":{"type":"string"}},{"name":"stage","in":"query","description":"Specefic Order Stage","required":false,"schema":{"type":"string"}},{"name":"sales_channels","in":"query","description":"Selected Sales Channel","required":false,"schema":{"type":"string"}},{"name":"order_id","in":"query","description":"Order Id","required":false,"schema":{"type":"string"}},{"name":"stores","in":"query","description":"Selected Stores","required":false,"schema":{"type":"string"}},{"name":"status","in":"query","description":"Status of order","required":false,"schema":{"type":"string"}},{"name":"dp","in":"query","description":"Delivery Partners","required":false,"schema":{"type":"string"}},{"name":"shorten_urls","in":"query","description":"Shorten URL option","required":false,"schema":{"type":"boolean"}},{"name":"filter_type","in":"query","description":"Filters","required":false,"schema":{"type":"string"}}],"query":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"Page limit","required":false,"schema":{"type":"string"}},{"name":"from_date","in":"query","description":"From Date","required":false,"schema":{"type":"string"}},{"name":"to_date","in":"query","description":"To Date","required":false,"schema":{"type":"string"}},{"name":"q","in":"query","description":"Keyword for Search","required":false,"schema":{"type":"string"}},{"name":"stage","in":"query","description":"Specefic Order Stage","required":false,"schema":{"type":"string"}},{"name":"sales_channels","in":"query","description":"Selected Sales Channel","required":false,"schema":{"type":"string"}},{"name":"order_id","in":"query","description":"Order Id","required":false,"schema":{"type":"string"}},{"name":"stores","in":"query","description":"Selected Stores","required":false,"schema":{"type":"string"}},{"name":"status","in":"query","description":"Status of order","required":false,"schema":{"type":"string"}},{"name":"dp","in":"query","description":"Delivery Partners","required":false,"schema":{"type":"string"}},{"name":"shorten_urls","in":"query","description":"Shorten URL option","required":false,"schema":{"type":"boolean"}},{"name":"filter_type","in":"query","description":"Filters","required":false,"schema":{"type":"string"}}],"headers":[]}""", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, q=q, stage=stage, sales_channels=sales_channels, order_id=order_id, stores=stores, status=status, dp=dp, shorten_urls=shorten_urls, filter_type=filter_type)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, q=q, stage=stage, sales_channels=sales_channels, order_id=order_id, stores=stores, status=status, dp=dp, shorten_urls=shorten_urls, filter_type=filter_type)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/order/v1.0/company/{company_id}/application/{application_id}/orders", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, q=q, stage=stage, sales_channels=sales_channels, order_id=order_id, stores=stores, status=status, dp=dp, shorten_urls=shorten_urls, filter_type=filter_type), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getPing(self, company_id=None, body=""):
        """Get Ping
        :param company_id : Company Id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = OrderValidator.getPing()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/order/v1.0/company/{company_id}/ping", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/order/v1.0/company/{company_id}/ping", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def voiceCallback(self, company_id=None, body=""):
        """Voice Callback
        :param company_id : Company Id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = OrderValidator.voiceCallback()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/order/v1.0/company/{company_id}/voice/callback", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/order/v1.0/company/{company_id}/voice/callback", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def voiceClickToCall(self, company_id=None, caller=None, receiver=None, body=""):
        """Voice Click to Call
        :param company_id : Company Id : type string
        :param caller : Caller contact number : type string
        :param receiver : Receiver contact number : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if caller:
            payload["caller"] = caller
        
        if receiver:
            payload["receiver"] = receiver
        

        # Parameter validation
        schema = OrderValidator.voiceClickToCall()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/order/v1.0/company/{company_id}/voice/click-to-call", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"caller","in":"query","description":"Caller contact number","required":true,"schema":{"type":"string"}},{"name":"receiver","in":"query","description":"Receiver contact number","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"caller","in":"query","description":"Caller contact number","required":true,"schema":{"type":"string"}},{"name":"receiver","in":"query","description":"Receiver contact number","required":true,"schema":{"type":"string"}}],"headers":[]}""", company_id=company_id, caller=caller, receiver=receiver)
        query_string = await create_query_string(company_id=company_id, caller=caller, receiver=receiver)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/order/v1.0/company/{company_id}/voice/click-to-call", company_id=company_id, caller=caller, receiver=receiver), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    

class Catalog:
    def __init__(self, config):
        self._conf = config
    # async def ():
    
    async def deleteSearchKeywords(self, company_id=None, application_id=None, id=None, body=""):
        """Delete a keywords by it's id. Returns an object that tells whether the keywords was deleted successfully
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param application_id : A `application_id` is a unique identifier for a particular sale channel. : type string
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.deleteSearchKeywords()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/search/keyword/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/search/keyword/{id}/", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getSearchKeywords(self, company_id=None, application_id=None, id=None, body=""):
        """Get the details of a words by its `id`. If successful, returns a Collection resource in the response body specified in `GetSearchWordsDetailResponseSchema`
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param application_id : A `application_id` is a unique identifier for a particular sale channel. : type string
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.getSearchKeywords()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/search/keyword/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/search/keyword/{id}/", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateSearchKeywords(self, company_id=None, application_id=None, id=None, body=""):
        """Update Search Keyword by its id. On successful request, returns the updated collection
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param application_id : A `application_id` is a unique identifier for a particular sale channel. : type string
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.updateSearchKeywords()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.CreateSearchKeyword import CreateSearchKeyword
        schema = CreateSearchKeyword()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/search/keyword/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/search/keyword/{id}/", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getAllSearchKeyword(self, company_id=None, application_id=None, body=""):
        """Custom Search Keyword allows you to map conditions with keywords to give you the ultimate results
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param application_id : A `application_id` is a unique identifier for a particular sale channel. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = CatalogValidator.getAllSearchKeyword()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/search/keyword/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/search/keyword/", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createCustomKeyword(self, company_id=None, application_id=None, body=""):
        """Create a Custom Search Keywords. See `CreateSearchKeywordSchema` for the list of attributes needed to create a mapping and /collections/query-options for the available options to create a rule. On successful request, returns a paginated list of collections specified in `CreateSearchKeywordSchema`
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param application_id : A `application_id` is a unique identifier for a particular sale channel. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = CatalogValidator.createCustomKeyword()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.CreateSearchKeyword import CreateSearchKeyword
        schema = CreateSearchKeyword()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/search/keyword/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/search/keyword/", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def deleteAutocompleteKeyword(self, company_id=None, application_id=None, id=None, body=""):
        """Delete a keywords by it's id. Returns an object that tells whether the keywords was deleted successfully
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param application_id : A `application_id` is a unique identifier for a particular sale channel. : type string
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.deleteAutocompleteKeyword()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/search/autocomplete/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/search/autocomplete/{id}/", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getAutocompleteKeywordDetail(self, company_id=None, application_id=None, id=None, body=""):
        """Get the details of a words by its `id`. If successful, returns a keywords resource in the response body specified in `GetAutocompleteWordsResponseSchema`
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param application_id : A `application_id` is a unique identifier for a particular sale channel. : type string
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.getAutocompleteKeywordDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/search/autocomplete/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/search/autocomplete/{id}/", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateAutocompleteKeyword(self, company_id=None, application_id=None, id=None, body=""):
        """Update a mapping by it's id. On successful request, returns the updated Keyword mapping
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param application_id : A `application_id` is a unique identifier for a particular sale channel. : type string
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.updateAutocompleteKeyword()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.CreateAutocompleteKeyword import CreateAutocompleteKeyword
        schema = CreateAutocompleteKeyword()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/search/autocomplete/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/search/autocomplete/{id}/", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getAutocompleteConfig(self, company_id=None, application_id=None, body=""):
        """Custom Autocomplete Keyword allows you to map conditions with keywords to give you the ultimate results
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param application_id : A `application_id` is a unique identifier for a particular sale channel. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = CatalogValidator.getAutocompleteConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/search/autocomplete/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/search/autocomplete/", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createCustomAutocompleteRule(self, company_id=None, application_id=None, body=""):
        """Create a Custom Autocomplete Keywords. See `CreateAutocompleteKeywordSchema` for the list of attributes needed to create a mapping and /collections/query-options for the available options to create a rule. On successful request, returns a paginated list of collections specified in `CreateAutocompleteKeywordSchema`
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param application_id : A `application_id` is a unique identifier for a particular sale channel. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = CatalogValidator.createCustomAutocompleteRule()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.CreateAutocompleteKeyword import CreateAutocompleteKeyword
        schema = CreateAutocompleteKeyword()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/search/autocomplete/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/search/autocomplete/", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getProductBundle(self, company_id=None, q=None, body=""):
        """Get all product bundles for a particular company
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param q : A search string that is searched with product bundle name. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if q:
            payload["q"] = q
        

        # Parameter validation
        schema = CatalogValidator.getProductBundle()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/product-bundle/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"q","description":"A search string that is searched with product bundle name.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"q","description":"A search string that is searched with product bundle name.","schema":{"type":"string"},"required":false}],"headers":[]}""", company_id=company_id, q=q)
        query_string = await create_query_string(company_id=company_id, q=q)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/product-bundle/", company_id=company_id, q=q), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createProductBundle(self, company_id=None, body=""):
        """Create Product Bundle. See `ProductBundleRequest` for the request body parameter need to create a product bundle. On successful request, returns in `ProductBundleRequest` with id
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = CatalogValidator.createProductBundle()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.ProductBundleRequest import ProductBundleRequest
        schema = ProductBundleRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/product-bundle/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/product-bundle/", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getProductBundleDetail(self, company_id=None, id=None, body=""):
        """Get a particular Bundle details by its `id`. If successful, returns a Product bundle resource in the response body specified in `GetProductBundleResponse`
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.getProductBundleDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/product-bundle/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to retrieve.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, id=id)
        query_string = await create_query_string(company_id=company_id, id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/product-bundle/{id}/", company_id=company_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateProductBundle(self, company_id=None, id=None, body=""):
        """Update a Product Bundle by its id. On successful request, returns the updated product bundle
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param id : A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.updateProductBundle()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.ProductBundleUpdateRequest import ProductBundleUpdateRequest
        schema = ProductBundleUpdateRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/product-bundle/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier for a particular detail. Pass the `id` of the keywords which you want to delete.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, id=id)
        query_string = await create_query_string(company_id=company_id, id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/product-bundle/{id}/", company_id=company_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getSizeGuides(self, company_id=None, active=None, q=None, tag=None, page_no=None, page_size=None, body=""):
        """This API allows to view all the size guides associated to the seller.
        :param company_id : Id of the company for which the size guides are to be fetched. : type string
        :param active : filter size guide on basis of active, in-active : type boolean
        :param q : Query that is to be searched. : type string
        :param tag : to filter size guide on basis of tag. : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 10. : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if active:
            payload["active"] = active
        
        if q:
            payload["q"] = q
        
        if tag:
            payload["tag"] = tag
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = CatalogValidator.getSizeGuides()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/sizeguide", """{"required":[{"in":"path","name":"company_id","description":"Id of the company for which the size guides are to be fetched.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"active","description":"filter size guide on basis of active, in-active","schema":{"type":"boolean"},"required":false},{"in":"query","name":"q","description":"Query that is to be searched.","schema":{"type":"string"},"required":false},{"in":"query","name":"tag","description":"to filter size guide on basis of tag.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":10},"required":false}],"query":[{"in":"query","name":"active","description":"filter size guide on basis of active, in-active","schema":{"type":"boolean"},"required":false},{"in":"query","name":"q","description":"Query that is to be searched.","schema":{"type":"string"},"required":false},{"in":"query","name":"tag","description":"to filter size guide on basis of tag.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":10},"required":false}],"headers":[]}""", company_id=company_id, active=active, q=q, tag=tag, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(company_id=company_id, active=active, q=q, tag=tag, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/sizeguide", company_id=company_id, active=active, q=q, tag=tag, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createSizeGuide(self, company_id=None, body=""):
        """This API allows to create a size guide associated to a brand.
        :param company_id : Id of the company inside which the size guide is to be created. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = CatalogValidator.createSizeGuide()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.ValidateSizeGuide import ValidateSizeGuide
        schema = ValidateSizeGuide()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/sizeguide", """{"required":[{"in":"path","name":"company_id","description":"Id of the company inside which the size guide is to be created.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/sizeguide", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getSizeGuide(self, company_id=None, id=None, body=""):
        """This API helps to get data associated to a size guide.
        :param company_id : Id of the company associated to size guide. : type string
        :param id : Id of the size guide to be viewed. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.getSizeGuide()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/sizeguide/{id}/", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to size guide.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"Id of the size guide to be viewed.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, id=id)
        query_string = await create_query_string(company_id=company_id, id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/sizeguide/{id}/", company_id=company_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateSizeGuide(self, company_id=None, id=None, body=""):
        """This API allows to edit a size guide.
        :param company_id : Id of the company. : type string
        :param id : Mongo id of the size guide to be edited : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.updateSizeGuide()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.ValidateSizeGuide import ValidateSizeGuide
        schema = ValidateSizeGuide()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/sizeguide/{id}/", """{"required":[{"in":"path","name":"company_id","description":"Id of the company.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"Mongo id of the size guide to be edited","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, id=id)
        query_string = await create_query_string(company_id=company_id, id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/sizeguide/{id}/", company_id=company_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getCatalogConfiguration(self, company_id=None, application_id=None, body=""):
        """configuration meta  details for catalog.
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param application_id : A `application_id` is a unique identifier for a particular sale channel. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = CatalogValidator.getCatalogConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/product-configuration/metadata/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/product-configuration/metadata/", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getConfigurations(self, company_id=None, application_id=None, body=""):
        """configured details for catalog.
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param application_id : A `application_id` is a unique identifier for a particular sale channel. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = CatalogValidator.getConfigurations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/product-configuration/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/product-configuration/", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createConfigurationProductListing(self, company_id=None, application_id=None, body=""):
        """Add configuration for products & listing.
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param application_id : A `application_id` is a unique identifier for a particular sale channel. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = CatalogValidator.createConfigurationProductListing()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.AppConfiguration import AppConfiguration
        schema = AppConfiguration()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/product-configuration/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/product-configuration/", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getConfigurationByType(self, company_id=None, application_id=None, type=None, body=""):
        """configured details for catalog.
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param application_id : A `application_id` is a unique identifier for a particular sale channel. : type string
        :param type : type can be brands, categories etc. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if type:
            payload["type"] = type
        

        # Parameter validation
        schema = CatalogValidator.getConfigurationByType()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/product-configuration/{type}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"type","description":"type can be brands, categories etc.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, type=type)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, type=type)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/product-configuration/{type}/", company_id=company_id, application_id=application_id, type=type), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createConfigurationByType(self, company_id=None, application_id=None, type=None, body=""):
        """Add configuration for categories & brands.
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param application_id : A `application_id` is a unique identifier for a particular sale channel. : type string
        :param type : type can be brands, categories etc. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if type:
            payload["type"] = type
        

        # Parameter validation
        schema = CatalogValidator.createConfigurationByType()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.AppConfiguration import AppConfiguration
        schema = AppConfiguration()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/product-configuration/{type}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"type","description":"type can be brands, categories etc.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, type=type)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, type=type)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/product-configuration/{type}/", company_id=company_id, application_id=application_id, type=type), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getQueryFilters(self, company_id=None, application_id=None, body=""):
        """Get query filters to configure a collection
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param application_id : A `application_id` is a unique identifier for a particular sale channel. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = CatalogValidator.getQueryFilters()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/collections/query-options/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/collections/query-options/", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getAllCollections(self, company_id=None, application_id=None, body=""):
        """A Collection allows you to organize your products into hierarchical groups. For example, a dress might be in the category _Clothing_, the individual product might also be in the collection _Summer_. On successful request, returns all the collections as specified in `CollectionListingSchema`
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param application_id : A `application_id` is a unique identifier for a particular sale channel. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = CatalogValidator.getAllCollections()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/collections/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/collections/", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createCollection(self, company_id=None, application_id=None, body=""):
        """Create a collection. See `CreateCollectionRequestSchema` for the list of attributes needed to create a collection and collections/query-options for the available options to create a collection. On successful request, returns a paginated list of collections specified in `CollectionCreateResponse`
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param application_id : A `application_id` is a unique identifier for a particular sale channel. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = CatalogValidator.createCollection()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.CreateCollection import CreateCollection
        schema = CreateCollection()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/collections/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/collections/", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getCollectionDetail(self, company_id=None, application_id=None, slug=None, body=""):
        """Get the details of a collection by its `slug`. If successful, returns a Collection resource in the response body specified in `CollectionDetailResponse`
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param application_id : A `application_id` is a unique identifier for a particular sale channel. : type string
        :param slug : A `slug` is a human readable, URL friendly unique identifier of an object. Pass the `slug` of the collection which you want to retrieve. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if slug:
            payload["slug"] = slug
        

        # Parameter validation
        schema = CatalogValidator.getCollectionDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/collections/{slug}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"slug","description":"A `slug` is a human readable, URL friendly unique identifier of an object. Pass the `slug` of the collection which you want to retrieve.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, slug=slug)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, slug=slug)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/collections/{slug}/", company_id=company_id, application_id=application_id, slug=slug), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def deleteCollection(self, company_id=None, application_id=None, id=None, body=""):
        """Delete a collection by it's id. Returns an object that tells whether the collection was deleted successfully
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param application_id : A `application_id` is a unique identifier for a particular sale channel. : type string
        :param id : A `id` is a unique identifier of a collection. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.deleteCollection()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/collections/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier of a collection.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/collections/{id}/", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateCollection(self, company_id=None, application_id=None, id=None, body=""):
        """Update a collection by it's id. On successful request, returns the updated collection
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param application_id : A `application_id` is a unique identifier for a particular sale channel. : type string
        :param id : A `id` is a unique identifier of a collection. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.updateCollection()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.UpdateCollection import UpdateCollection
        schema = UpdateCollection()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/collections/{id}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier of a collection.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/collections/{id}/", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getCollectionItems(self, company_id=None, application_id=None, id=None, sort_on=None, page_id=None, page_size=None, body=""):
        """Get items from a collection specified by its `id`.
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param application_id : A `application_id` is a unique identifier for a particular sale channel. : type string
        :param id : A `id` is a unique identifier of a collection. : type string
        :param sort_on : Each response will contain sort_on param, which should be sent back to make pagination work. : type string
        :param page_id : Each response will contain next_id param, which should be sent back to make pagination work. : type string
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        
        if sort_on:
            payload["sort_on"] = sort_on
        
        if page_id:
            payload["page_id"] = page_id
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = CatalogValidator.getCollectionItems()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/collections/{id}/items/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier of a collection.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"sort_on","description":"Each response will contain sort_on param, which should be sent back to make pagination work.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_id","description":"Each response will contain next_id param, which should be sent back to make pagination work.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer"},"required":false}],"query":[{"in":"query","name":"sort_on","description":"Each response will contain sort_on param, which should be sent back to make pagination work.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_id","description":"Each response will contain next_id param, which should be sent back to make pagination work.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer"},"required":false}],"headers":[]}""", company_id=company_id, application_id=application_id, id=id, sort_on=sort_on, page_id=page_id, page_size=page_size)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id, sort_on=sort_on, page_id=page_id, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/collections/{id}/items/", company_id=company_id, application_id=application_id, id=id, sort_on=sort_on, page_id=page_id, page_size=page_size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def addCollectionItems(self, company_id=None, application_id=None, id=None, body=""):
        """Adds items to a collection specified by its `id`. See `CollectionItemRequest` for the list of attributes needed to add items to an collection.
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param application_id : A `application_id` is a unique identifier for a particular sale channel. : type string
        :param id : A `id` is a unique identifier of a collection. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.addCollectionItems()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.CollectionItemRequest import CollectionItemRequest
        schema = CollectionItemRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/collections/{id}/items/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"A `id` is a unique identifier of a collection.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/collections/{id}/items/", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getCatalogInsights(self, company_id=None, application_id=None, brand=None, body=""):
        """Catalog Insights api returns the count of catalog related data like products, brands, departments and categories that have been made live as per configuration of the app.
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param application_id : A `application_id` is a unique identifier for a particular sale channel. : type string
        :param brand : Brand slug : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if brand:
            payload["brand"] = brand
        

        # Parameter validation
        schema = CatalogValidator.getCatalogInsights()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/analytics/insights/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"brand","description":"Brand slug","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"brand","description":"Brand slug","schema":{"type":"string"},"required":false}],"headers":[]}""", company_id=company_id, application_id=application_id, brand=brand)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, brand=brand)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/analytics/insights/", company_id=company_id, application_id=application_id, brand=brand), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getSellerInsights(self, company_id=None, seller_app_id=None, body=""):
        """Analytics data of catalog and inventory that are being cross-selled.
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param seller_app_id : Id of the seller application which is serving the invetory/catalog of the company : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if seller_app_id:
            payload["seller_app_id"] = seller_app_id
        

        # Parameter validation
        schema = CatalogValidator.getSellerInsights()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/cross-selling/{seller_app_id}/analytics/insights/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"seller_app_id","description":"Id of the seller application which is serving the invetory/catalog of the company","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, seller_app_id=seller_app_id)
        query_string = await create_query_string(company_id=company_id, seller_app_id=seller_app_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/cross-selling/{seller_app_id}/analytics/insights/", company_id=company_id, seller_app_id=seller_app_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createMarketplaceOptin(self, company_id=None, marketplace=None, body=""):
        """Use this API to create/update opt-in information for given platform. If successful, returns data in the response body as specified in `OptInPostResponseSchema`
        :param company_id : The company id for which the detail needs to be retrieved. : type integer
        :param marketplace : The marketplace for which the detail needs to be retrieved. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if marketplace:
            payload["marketplace"] = marketplace
        

        # Parameter validation
        schema = CatalogValidator.createMarketplaceOptin()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.OptInPostRequest import OptInPostRequest
        schema = OptInPostRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/marketplaces/{marketplace}/optin/", """{"required":[{"in":"path","name":"company_id","description":"The company id for which the detail needs to be retrieved.","schema":{"type":"integer"},"required":true},{"in":"path","name":"marketplace","description":"The marketplace for which the detail needs to be retrieved.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, marketplace=marketplace)
        query_string = await create_query_string(company_id=company_id, marketplace=marketplace)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/marketplaces/{marketplace}/optin/", company_id=company_id, marketplace=marketplace), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getMarketplaceOptinDetail(self, company_id=None, body=""):
        """Use this API to fetch opt-in information for all the platforms. If successful, returns a logs in the response body as specified in `GetOptInPlatformSchema`
        :param company_id :  : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = CatalogValidator.getMarketplaceOptinDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/marketplaces/", """{"required":[{"in":"path","name":"company_id","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/marketplaces/", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getCompanyDetail(self, company_id=None, body=""):
        """Get the details of the company associated with the given company_id passed.
        :param company_id : The company id for which the detail needs to be retrieved. : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = CatalogValidator.getCompanyDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/marketplaces/company-details/", """{"required":[{"in":"path","name":"company_id","description":"The company id for which the detail needs to be retrieved.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/marketplaces/company-details/", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getCompanyBrandDetail(self, company_id=None, is_active=None, q=None, page_no=None, page_size=None, marketplace=None, body=""):
        """Get the details of the Brands associated with the given company_id passed.
        :param company_id : The company id for which the detail needs to be retrieved. : type integer
        :param is_active : The is_active status for the optin id. : type boolean
        :param q : The search value to filter the list. : type boolean
        :param page_no : The number of page for the company id. : type integer
        :param page_size : Number of records that can be seen on the page for the company id. : type integer
        :param marketplace : The marketplace platform associated with the company id. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if is_active:
            payload["is_active"] = is_active
        
        if q:
            payload["q"] = q
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if marketplace:
            payload["marketplace"] = marketplace
        

        # Parameter validation
        schema = CatalogValidator.getCompanyBrandDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/marketplaces/company-brand-details/", """{"required":[{"in":"path","name":"company_id","description":"The company id for which the detail needs to be retrieved.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"is_active","description":"The is_active status for the optin id.","schema":{"type":"boolean"},"required":false},{"in":"query","name":"q","description":"The search value to filter the list.","schema":{"type":"boolean"},"required":false},{"in":"query","name":"page_no","description":"The number of page for the company id.","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of records that can be seen on the page for the company id.","schema":{"type":"integer"},"required":false},{"in":"query","name":"marketplace","description":"The marketplace platform associated with the company id.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"is_active","description":"The is_active status for the optin id.","schema":{"type":"boolean"},"required":false},{"in":"query","name":"q","description":"The search value to filter the list.","schema":{"type":"boolean"},"required":false},{"in":"query","name":"page_no","description":"The number of page for the company id.","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of records that can be seen on the page for the company id.","schema":{"type":"integer"},"required":false},{"in":"query","name":"marketplace","description":"The marketplace platform associated with the company id.","schema":{"type":"string"},"required":false}],"headers":[]}""", company_id=company_id, is_active=is_active, q=q, page_no=page_no, page_size=page_size, marketplace=marketplace)
        query_string = await create_query_string(company_id=company_id, is_active=is_active, q=q, page_no=page_no, page_size=page_size, marketplace=marketplace)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/marketplaces/company-brand-details/", company_id=company_id, is_active=is_active, q=q, page_no=page_no, page_size=page_size, marketplace=marketplace), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getCompanyMetrics(self, company_id=None, body=""):
        """Get the Company metrics associated with the company ID passed.
        :param company_id : The company id for which the detail needs to be retrieved. : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = CatalogValidator.getCompanyMetrics()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/marketplaces/company-metrics/", """{"required":[{"in":"path","name":"company_id","description":"The company id for which the detail needs to be retrieved.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/marketplaces/company-metrics/", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getStoreDetail(self, company_id=None, q=None, page_no=None, page_size=None, body=""):
        """Get the details of the store associated with the company ID passed.
        :param company_id : The company id for which the detail needs to be retrieved. : type integer
        :param q : The search related the store for the company id. : type string
        :param page_no : The number of page for the company id. : type integer
        :param page_size : Number of records that can be seen on the page for the company id. : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if q:
            payload["q"] = q
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = CatalogValidator.getStoreDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/marketplaces/location-details/", """{"required":[{"in":"path","name":"company_id","description":"The company id for which the detail needs to be retrieved.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"q","description":"The search related the store for the company id.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"The number of page for the company id.","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of records that can be seen on the page for the company id.","schema":{"type":"integer"},"required":false}],"query":[{"in":"query","name":"q","description":"The search related the store for the company id.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"The number of page for the company id.","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of records that can be seen on the page for the company id.","schema":{"type":"integer"},"required":false}],"headers":[]}""", company_id=company_id, q=q, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(company_id=company_id, q=q, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/marketplaces/location-details/", company_id=company_id, q=q, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getGenderAttribute(self, company_id=None, attribute_slug=None, body=""):
        """This API allows to view the gender attribute details.
        :param company_id : company for which you want to view the genders : type integer
        :param attribute_slug : slug of the attribute for which you want to view the genders : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if attribute_slug:
            payload["attribute_slug"] = attribute_slug
        

        # Parameter validation
        schema = CatalogValidator.getGenderAttribute()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/product-attributes/{attribute_slug}", """{"required":[{"in":"path","name":"company_id","description":"company for which you want to view the genders","schema":{"type":"integer"},"required":true},{"in":"path","name":"attribute_slug","description":"slug of the attribute for which you want to view the genders","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, attribute_slug=attribute_slug)
        query_string = await create_query_string(company_id=company_id, attribute_slug=attribute_slug)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/product-attributes/{attribute_slug}", company_id=company_id, attribute_slug=attribute_slug), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def listProductTemplateCategories(self, company_id=None, departments=None, item_type=None, body=""):
        """Allows you to list all product categories values for the departments specified
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param departments : A `department` is name of a departments whose category needs to be listed. Can specify multiple departments. : type string
        :param item_type : An `item_type` is the type of item, it can be `set`, `standard`, `digital`, etc. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if departments:
            payload["departments"] = departments
        
        if item_type:
            payload["item_type"] = item_type
        

        # Parameter validation
        schema = CatalogValidator.listProductTemplateCategories()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/products/templates/categories/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"query","name":"departments","description":"A `department` is name of a departments whose category needs to be listed. Can specify multiple departments.","schema":{"type":"string"},"required":true},{"in":"query","name":"item_type","description":"An `item_type` is the type of item, it can be `set`, `standard`, `digital`, etc.","schema":{"type":"string"},"required":true}],"optional":[],"query":[{"in":"query","name":"departments","description":"A `department` is name of a departments whose category needs to be listed. Can specify multiple departments.","schema":{"type":"string"},"required":true},{"in":"query","name":"item_type","description":"An `item_type` is the type of item, it can be `set`, `standard`, `digital`, etc.","schema":{"type":"string"},"required":true}],"headers":[]}""", company_id=company_id, departments=departments, item_type=item_type)
        query_string = await create_query_string(company_id=company_id, departments=departments, item_type=item_type)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/products/templates/categories/", company_id=company_id, departments=departments, item_type=item_type), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def listDepartmentsData(self, company_id=None, page_no=None, page_size=None, name=None, search=None, is_active=None, body=""):
        """Allows you to list all departments, also can search using name and filter active and incative departments, and item type
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 10. : type integer
        :param name : Can search departments by passing name. : type string
        :param search : Can search departments by passing name of the department in search parameter. : type string
        :param is_active : Can query for departments based on whether they are active or inactive. : type boolean
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if name:
            payload["name"] = name
        
        if search:
            payload["search"] = search
        
        if is_active:
            payload["is_active"] = is_active
        

        # Parameter validation
        schema = CatalogValidator.listDepartmentsData()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/departments/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer"},"required":false},{"in":"query","name":"name","description":"Can search departments by passing name.","schema":{"type":"string"},"required":false},{"in":"query","name":"search","description":"Can search departments by passing name of the department in search parameter.","schema":{"type":"string"},"required":false},{"in":"query","name":"is_active","description":"Can query for departments based on whether they are active or inactive.","schema":{"type":"boolean"},"required":false}],"query":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer"},"required":false},{"in":"query","name":"name","description":"Can search departments by passing name.","schema":{"type":"string"},"required":false},{"in":"query","name":"search","description":"Can search departments by passing name of the department in search parameter.","schema":{"type":"string"},"required":false},{"in":"query","name":"is_active","description":"Can query for departments based on whether they are active or inactive.","schema":{"type":"boolean"},"required":false}],"headers":[]}""", company_id=company_id, page_no=page_no, page_size=page_size, name=name, search=search, is_active=is_active)
        query_string = await create_query_string(company_id=company_id, page_no=page_no, page_size=page_size, name=name, search=search, is_active=is_active)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/departments/", company_id=company_id, page_no=page_no, page_size=page_size, name=name, search=search, is_active=is_active), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getDepartmentData(self, company_id=None, uid=None, body=""):
        """Allows you to get department data, by uid
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param uid : A `uid` is a unique identifier of a department. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if uid:
            payload["uid"] = uid
        

        # Parameter validation
        schema = CatalogValidator.getDepartmentData()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/departments/{uid}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"uid","description":"A `uid` is a unique identifier of a department.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, uid=uid)
        query_string = await create_query_string(company_id=company_id, uid=uid)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/departments/{uid}/", company_id=company_id, uid=uid), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def listProductTemplate(self, company_id=None, department=None, body=""):
        """Allows you to list all product templates, also can filter by department
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param department : A `department` is the name of a particular department. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if department:
            payload["department"] = department
        

        # Parameter validation
        schema = CatalogValidator.listProductTemplate()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/products/templates/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"query","name":"department","description":"A `department` is the name of a particular department.","schema":{"type":"string"},"required":true}],"optional":[],"query":[{"in":"query","name":"department","description":"A `department` is the name of a particular department.","schema":{"type":"string"},"required":true}],"headers":[]}""", company_id=company_id, department=department)
        query_string = await create_query_string(company_id=company_id, department=department)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/products/templates/", company_id=company_id, department=department), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def validateProductTemplate(self, company_id=None, slug=None, body=""):
        """Allows you to list all product templates validation values for all the fields present in the database
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param slug : A `slug` is a unique identifier for a particular template. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if slug:
            payload["slug"] = slug
        

        # Parameter validation
        schema = CatalogValidator.validateProductTemplate()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/products/templates/{slug}/validation/schema/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"slug","description":"A `slug` is a unique identifier for a particular template.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, slug=slug)
        query_string = await create_query_string(company_id=company_id, slug=slug)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/products/templates/{slug}/validation/schema/", company_id=company_id, slug=slug), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def downloadProductTemplateViews(self, company_id=None, slug=None, body=""):
        """Allows you to download product template data
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param slug : A `slug` is a unique identifier for a particular template. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if slug:
            payload["slug"] = slug
        

        # Parameter validation
        schema = CatalogValidator.downloadProductTemplateViews()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/products/templates/{slug}/download/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"slug","description":"A `slug` is a unique identifier for a particular template.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, slug=slug)
        query_string = await create_query_string(company_id=company_id, slug=slug)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/products/templates/{slug}/download/", company_id=company_id, slug=slug), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def downloadProductTemplateView(self, company_id=None, item_type=None, body=""):
        """Allows you to download product template data
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param item_type : An `item_type` defines the type of item. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if item_type:
            payload["item_type"] = item_type
        

        # Parameter validation
        schema = CatalogValidator.downloadProductTemplateView()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/inventory/templates/download/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"query","name":"item_type","description":"An `item_type` defines the type of item.","schema":{"type":"string"},"required":true}],"optional":[],"query":[{"in":"query","name":"item_type","description":"An `item_type` defines the type of item.","schema":{"type":"string"},"required":true}],"headers":[]}""", company_id=company_id, item_type=item_type)
        query_string = await create_query_string(company_id=company_id, item_type=item_type)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/inventory/templates/download/", company_id=company_id, item_type=item_type), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def validateProductTemplateSchema(self, company_id=None, item_type=None, body=""):
        """Allows you to list all product templates validation values for all the fields present in the database
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param item_type : An `item_type` defines the type of item. The default value is standard. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if item_type:
            payload["item_type"] = item_type
        

        # Parameter validation
        schema = CatalogValidator.validateProductTemplateSchema()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/inventory/templates/validation/schema/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"query","name":"item_type","description":"An `item_type` defines the type of item. The default value is standard.","schema":{"type":"string"},"required":true}],"optional":[],"query":[{"in":"query","name":"item_type","description":"An `item_type` defines the type of item. The default value is standard.","schema":{"type":"string"},"required":true}],"headers":[]}""", company_id=company_id, item_type=item_type)
        query_string = await create_query_string(company_id=company_id, item_type=item_type)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/inventory/templates/validation/schema/", company_id=company_id, item_type=item_type), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def listHSNCodes(self, company_id=None, body=""):
        """Allows you to list all hsn Codes
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = CatalogValidator.listHSNCodes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/products/hsn/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/products/hsn/", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def listProductTemplateExportDetails(self, company_id=None, body=""):
        """Can view details including trigger data, task id , etc.
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = CatalogValidator.listProductTemplateExportDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/products/downloads/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/products/downloads/", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def listTemplateBrandTypeValues(self, company_id=None, filter=None, body=""):
        """The filter type query parameter defines what type of data to return. The type of query returns the valid values for the same
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param filter : A `filter` is the unique identifier of the type of value required. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if filter:
            payload["filter"] = filter
        

        # Parameter validation
        schema = CatalogValidator.listTemplateBrandTypeValues()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/downloads/configuration/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"query","name":"filter","description":"A `filter` is the unique identifier of the type of value required.","schema":{"type":"string"},"required":true}],"optional":[],"query":[{"in":"query","name":"filter","description":"A `filter` is the unique identifier of the type of value required.","schema":{"type":"string"},"required":true}],"headers":[]}""", company_id=company_id, filter=filter)
        query_string = await create_query_string(company_id=company_id, filter=filter)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/downloads/configuration/", company_id=company_id, filter=filter), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def listCategories(self, company_id=None, level=None, departments=None, q=None, page_no=None, page_size=None, body=""):
        """This API gets meta associated to product categories.
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param level : Get category for multiple levels : type string
        :param departments : Get category for multiple departments filtered : type string
        :param q : Get multiple categories filtered by search string : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 10. : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if level:
            payload["level"] = level
        
        if departments:
            payload["departments"] = departments
        
        if q:
            payload["q"] = q
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = CatalogValidator.listCategories()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/category/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"level","description":"Get category for multiple levels","schema":{"type":"string"},"required":false},{"in":"query","name":"departments","description":"Get category for multiple departments filtered","schema":{"type":"string"},"required":false},{"in":"query","name":"q","description":"Get multiple categories filtered by search string","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":12},"required":false}],"query":[{"in":"query","name":"level","description":"Get category for multiple levels","schema":{"type":"string"},"required":false},{"in":"query","name":"departments","description":"Get category for multiple departments filtered","schema":{"type":"string"},"required":false},{"in":"query","name":"q","description":"Get multiple categories filtered by search string","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":12},"required":false}],"headers":[]}""", company_id=company_id, level=level, departments=departments, q=q, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(company_id=company_id, level=level, departments=departments, q=q, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/category/", company_id=company_id, level=level, departments=departments, q=q, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createCategories(self, company_id=None, body=""):
        """This API lets user create product categories
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = CatalogValidator.createCategories()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.CategoryRequestBody import CategoryRequestBody
        schema = CategoryRequestBody()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/category/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/category/", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getCategoryData(self, company_id=None, uid=None, body=""):
        """This API gets meta associated to product categories.
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param uid : Category unique id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if uid:
            payload["uid"] = uid
        

        # Parameter validation
        schema = CatalogValidator.getCategoryData()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/category/{uid}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"uid","description":"Category unique id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, uid=uid)
        query_string = await create_query_string(company_id=company_id, uid=uid)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/category/{uid}/", company_id=company_id, uid=uid), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateCategory(self, company_id=None, uid=None, body=""):
        """Update a product category using this apu
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param uid : Category unique id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if uid:
            payload["uid"] = uid
        

        # Parameter validation
        schema = CatalogValidator.updateCategory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.CategoryRequestBody import CategoryRequestBody
        schema = CategoryRequestBody()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/category/{uid}/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"uid","description":"Category unique id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, uid=uid)
        query_string = await create_query_string(company_id=company_id, uid=uid)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/category/{uid}/", company_id=company_id, uid=uid), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getProducts(self, company_id=None, brand_ids=None, category_ids=None, item_ids=None, department_ids=None, item_code=None, q=None, tags=None, page_no=None, page_size=None, body=""):
        """This API gets meta associated to products.
        :param company_id : Get list of products filtered by company Id : type integer
        :param brand_ids : Get multiple products filtered by Brand Ids : type array
        :param category_ids : Get multiple products filtered by Category Ids : type array
        :param item_ids : Get multiple products filtered by Item Ids : type array
        :param department_ids : Get multiple products filtered by Department Ids : type array
        :param item_code : Get multiple products filtered by Item Code : type array
        :param q : Get multiple products filtered by q string : type string
        :param tags : Get multiple products filtered by tags : type array
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 10. : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if brand_ids:
            payload["brand_ids"] = brand_ids
        
        if category_ids:
            payload["category_ids"] = category_ids
        
        if item_ids:
            payload["item_ids"] = item_ids
        
        if department_ids:
            payload["department_ids"] = department_ids
        
        if item_code:
            payload["item_code"] = item_code
        
        if q:
            payload["q"] = q
        
        if tags:
            payload["tags"] = tags
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = CatalogValidator.getProducts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/products/", """{"required":[{"in":"path","name":"company_id","description":"Get list of products filtered by company Id","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"brand_ids","description":"Get multiple products filtered by Brand Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"category_ids","description":"Get multiple products filtered by Category Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"item_ids","description":"Get multiple products filtered by Item Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"department_ids","description":"Get multiple products filtered by Department Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"item_code","description":"Get multiple products filtered by Item Code","schema":{"type":"array","items":{"type":"number"}},"required":false},{"in":"query","name":"q","description":"Get multiple products filtered by q string","schema":{"type":"string"},"required":false},{"in":"query","name":"tags","description":"Get multiple products filtered by tags","schema":{"type":"array","items":{"type":"string"}},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":10},"required":false}],"query":[{"in":"query","name":"brand_ids","description":"Get multiple products filtered by Brand Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"category_ids","description":"Get multiple products filtered by Category Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"item_ids","description":"Get multiple products filtered by Item Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"department_ids","description":"Get multiple products filtered by Department Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"item_code","description":"Get multiple products filtered by Item Code","schema":{"type":"array","items":{"type":"number"}},"required":false},{"in":"query","name":"q","description":"Get multiple products filtered by q string","schema":{"type":"string"},"required":false},{"in":"query","name":"tags","description":"Get multiple products filtered by tags","schema":{"type":"array","items":{"type":"string"}},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":10},"required":false}],"headers":[]}""", company_id=company_id, brand_ids=brand_ids, category_ids=category_ids, item_ids=item_ids, department_ids=department_ids, item_code=item_code, q=q, tags=tags, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(company_id=company_id, brand_ids=brand_ids, category_ids=category_ids, item_ids=item_ids, department_ids=department_ids, item_code=item_code, q=q, tags=tags, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/products/", company_id=company_id, brand_ids=brand_ids, category_ids=category_ids, item_ids=item_ids, department_ids=department_ids, item_code=item_code, q=q, tags=tags, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createProduct(self, company_id=None, body=""):
        """This API allows to create product.
        :param company_id : Id of the company associated to product that is to be viewed. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = CatalogValidator.createProduct()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.ProductCreateUpdate import ProductCreateUpdate
        schema = ProductCreateUpdate()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/products/", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/products/", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def deleteProduct(self, company_id=None, item_id=None, body=""):
        """This API allows to delete product.
        :param company_id : Company Id of the company associated to product that is to be deleted. : type string
        :param item_id : Id of the product to be updated. : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if item_id:
            payload["item_id"] = item_id
        

        # Parameter validation
        schema = CatalogValidator.deleteProduct()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/products/{item_id}/", """{"required":[{"in":"path","name":"company_id","description":"Company Id of the company associated to product that is to be deleted.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Id of the product to be updated.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, item_id=item_id)
        query_string = await create_query_string(company_id=company_id, item_id=item_id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/products/{item_id}/", company_id=company_id, item_id=item_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getProduct(self, item_code=None, company_id=None, item_id=None, brand_uid=None, body=""):
        """This API helps to get data associated to a particular product.
        :param item_code : Item code of the product. : type string
        :param company_id : Company Id of the product. : type integer
        :param item_id : Item Id of the product. : type integer
        :param brand_uid : Brand Id of the product. : type integer
        """
        payload = {}
        
        if item_code:
            payload["item_code"] = item_code
        
        if company_id:
            payload["company_id"] = company_id
        
        if item_id:
            payload["item_id"] = item_id
        
        if brand_uid:
            payload["brand_uid"] = brand_uid
        

        # Parameter validation
        schema = CatalogValidator.getProduct()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/products/{item_id}/", """{"required":[{"in":"path","name":"company_id","description":"Company Id of the product.","schema":{"type":"integer"},"required":true},{"in":"path","name":"item_id","description":"Item Id of the product.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"item_code","description":"Item code of the product.","schema":{"type":"string"},"required":false},{"in":"query","name":"brand_uid","description":"Brand Id of the product.","schema":{"type":"integer"},"required":false}],"query":[{"in":"query","name":"item_code","description":"Item code of the product.","schema":{"type":"string"},"required":false},{"in":"query","name":"brand_uid","description":"Brand Id of the product.","schema":{"type":"integer"},"required":false}],"headers":[]}""", item_code=item_code, company_id=company_id, item_id=item_id, brand_uid=brand_uid)
        query_string = await create_query_string(item_code=item_code, company_id=company_id, item_id=item_id, brand_uid=brand_uid)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/products/{item_id}/", item_code=item_code, company_id=company_id, item_id=item_id, brand_uid=brand_uid), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def editProduct(self, company_id=None, item_id=None, body=""):
        """This API allows to edit product.
        :param company_id : Id of the company associated to product that is to be viewed. : type string
        :param item_id : Id of the product to be updated. : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if item_id:
            payload["item_id"] = item_id
        

        # Parameter validation
        schema = CatalogValidator.editProduct()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.ProductCreateUpdate import ProductCreateUpdate
        schema = ProductCreateUpdate()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/products/{item_id}/", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Id of the product to be updated.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, item_id=item_id)
        query_string = await create_query_string(company_id=company_id, item_id=item_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/products/{item_id}/", company_id=company_id, item_id=item_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getProductValidation(self, company_id=None, body=""):
        """This API validates product data.
        :param company_id : Validates data against given company : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = CatalogValidator.getProductValidation()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/products/validation/", """{"required":[{"in":"path","name":"company_id","description":"Validates data against given company","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/products/validation/", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getProductSize(self, item_code=None, company_id=None, item_id=None, brand_uid=None, uid=None, body=""):
        """This API helps to get data associated to a particular product size.
        :param item_code : Item code of the product size. : type string
        :param company_id : Company Id of the product size. : type integer
        :param item_id : Item Id of the product size. : type integer
        :param brand_uid : Brand Id of the product size. : type integer
        :param uid : Id of the product size. : type integer
        """
        payload = {}
        
        if item_code:
            payload["item_code"] = item_code
        
        if company_id:
            payload["company_id"] = company_id
        
        if item_id:
            payload["item_id"] = item_id
        
        if brand_uid:
            payload["brand_uid"] = brand_uid
        
        if uid:
            payload["uid"] = uid
        

        # Parameter validation
        schema = CatalogValidator.getProductSize()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/products/{item_id}/sizes/", """{"required":[{"in":"path","name":"company_id","description":"Company Id of the product size.","schema":{"type":"integer"},"required":true},{"in":"path","name":"item_id","description":"Item Id of the product size.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"item_code","description":"Item code of the product size.","schema":{"type":"string"},"required":false},{"in":"query","name":"brand_uid","description":"Brand Id of the product size.","schema":{"type":"integer"},"required":false},{"in":"query","name":"uid","description":"Id of the product size.","schema":{"type":"integer"},"required":false}],"query":[{"in":"query","name":"item_code","description":"Item code of the product size.","schema":{"type":"string"},"required":false},{"in":"query","name":"brand_uid","description":"Brand Id of the product size.","schema":{"type":"integer"},"required":false},{"in":"query","name":"uid","description":"Id of the product size.","schema":{"type":"integer"},"required":false}],"headers":[]}""", item_code=item_code, company_id=company_id, item_id=item_id, brand_uid=brand_uid, uid=uid)
        query_string = await create_query_string(item_code=item_code, company_id=company_id, item_id=item_id, brand_uid=brand_uid, uid=uid)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/products/{item_id}/sizes/", item_code=item_code, company_id=company_id, item_id=item_id, brand_uid=brand_uid, uid=uid), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getProductBulkUploadHistory(self, company_id=None, page_no=None, page_size=None, body=""):
        """This API helps to get bulk product upload jobs data.
        :param company_id : Company Id of of which Product Bulk Upload History to be obtained. : type integer
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = CatalogValidator.getProductBulkUploadHistory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/products/bulk", """{"required":[{"in":"path","name":"company_id","description":"Company Id of of which Product Bulk Upload History to be obtained.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false}],"query":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false}],"headers":[]}""", company_id=company_id, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(company_id=company_id, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/products/bulk", company_id=company_id, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateProductAssetsInBulk(self, company_id=None, body=""):
        """This API helps to create a bulk asset upload job.
        :param company_id : Company Id in which assets to be uploaded. : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = CatalogValidator.updateProductAssetsInBulk()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.BulkJob import BulkJob
        schema = BulkJob()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/products/bulk", """{"required":[{"in":"path","name":"company_id","description":"Company Id in which assets to be uploaded.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/products/bulk", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def deleteProductBulkJob(self, company_id=None, batch_id=None, body=""):
        """This API allows to delete bulk product job associated with company.
        :param company_id : Company Id of the company associated to size that is to be deleted. : type string
        :param batch_id : Batch Id of the bulk product job to be deleted. : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if batch_id:
            payload["batch_id"] = batch_id
        

        # Parameter validation
        schema = CatalogValidator.deleteProductBulkJob()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/products/bulk/{batch_id}", """{"required":[{"in":"path","name":"company_id","description":"Company Id of the company associated to size that is to be deleted.","schema":{"type":"string"},"required":true},{"in":"path","name":"batch_id","description":"Batch Id of the bulk product job to be deleted.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, batch_id=batch_id)
        query_string = await create_query_string(company_id=company_id, batch_id=batch_id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/products/bulk/{batch_id}", company_id=company_id, batch_id=batch_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createProductsInBulk(self, company_id=None, batch_id=None, body=""):
        """This API helps to create products in bulk push to kafka for approval/creation.
        :param company_id : Company Id in which assets to be uploaded. : type integer
        :param batch_id : Batch Id in which assets to be uploaded. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if batch_id:
            payload["batch_id"] = batch_id
        

        # Parameter validation
        schema = CatalogValidator.createProductsInBulk()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.BulkProductRequest import BulkProductRequest
        schema = BulkProductRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/products/bulk/{batch_id}", """{"required":[{"in":"path","name":"company_id","description":"Company Id in which assets to be uploaded.","schema":{"type":"integer"},"required":true},{"in":"path","name":"batch_id","description":"Batch Id in which assets to be uploaded.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, batch_id=batch_id)
        query_string = await create_query_string(company_id=company_id, batch_id=batch_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/products/bulk/{batch_id}", company_id=company_id, batch_id=batch_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getProductTags(self, company_id=None, body=""):
        """This API helps to get tags data associated to a particular company.
        :param company_id : Company Id for which tags to be fetched. : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = CatalogValidator.getProductTags()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/products/tags", """{"required":[{"in":"path","name":"company_id","description":"Company Id for which tags to be fetched.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/products/tags", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getProductAssetsInBulk(self, company_id=None, page_no=None, page_size=None, body=""):
        """This API helps to get bulk asset jobs data associated to a particular company.
        :param company_id : Company Id of the product size. : type integer
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = CatalogValidator.getProductAssetsInBulk()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/products/assets/bulk/", """{"required":[{"in":"path","name":"company_id","description":"Company Id of the product size.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false}],"query":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false}],"headers":[]}""", company_id=company_id, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(company_id=company_id, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/products/assets/bulk/", company_id=company_id, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createProductAssetsInBulk(self, company_id=None, body=""):
        """This API helps to create a bulk asset upload job.
        :param company_id : Company Id in which assets to be uploaded. : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = CatalogValidator.createProductAssetsInBulk()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.ProductBulkAssets import ProductBulkAssets
        schema = ProductBulkAssets()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/products/assets/bulk/", """{"required":[{"in":"path","name":"company_id","description":"Company Id in which assets to be uploaded.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/products/assets/bulk/", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def deleteSize(self, company_id=None, item_id=None, size=None, body=""):
        """This API allows to delete size associated with product.
        :param company_id : Company Id of the company associated to size that is to be deleted. : type string
        :param item_id : Item Id of the product associated with size to be deleted. : type integer
        :param size : size to be deleted. : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if item_id:
            payload["item_id"] = item_id
        
        if size:
            payload["size"] = size
        

        # Parameter validation
        schema = CatalogValidator.deleteSize()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/products/{item_id}/sizes/{size}", """{"required":[{"in":"path","name":"company_id","description":"Company Id of the company associated to size that is to be deleted.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Item Id of the product associated with size to be deleted.","schema":{"type":"integer"},"required":true},{"in":"path","name":"size","description":"size to be deleted.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, item_id=item_id, size=size)
        query_string = await create_query_string(company_id=company_id, item_id=item_id, size=size)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/products/{item_id}/sizes/{size}", company_id=company_id, item_id=item_id, size=size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getInventoryBySize(self, company_id=None, item_id=None, size=None, page_no=None, page_size=None, q=None, sellable=None, body=""):
        """This API allows get Inventory data for particular company grouped by size and store.
        :param company_id : Id of the company associated to product that is to be viewed. : type string
        :param item_id : Item code of the product of which size is to be get. : type string
        :param size : Size of which inventory is to get. : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param q : Search with help of store code. : type string
        :param sellable : Filter on whether product is in stock or not. : type boolean
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if item_id:
            payload["item_id"] = item_id
        
        if size:
            payload["size"] = size
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if q:
            payload["q"] = q
        
        if sellable:
            payload["sellable"] = sellable
        

        # Parameter validation
        schema = CatalogValidator.getInventoryBySize()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/products/{item_id}/sizes/{size}", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Item code of the product of which size is to be get.","schema":{"type":"string"},"required":true},{"in":"path","name":"size","description":"Size of which inventory is to get.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search with help of store code.","schema":{"type":"string"},"required":false},{"in":"query","name":"sellable","description":"Filter on whether product is in stock or not.","schema":{"type":"boolean","default":false},"required":false}],"query":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search with help of store code.","schema":{"type":"string"},"required":false},{"in":"query","name":"sellable","description":"Filter on whether product is in stock or not.","schema":{"type":"boolean","default":false},"required":false}],"headers":[]}""", company_id=company_id, item_id=item_id, size=size, page_no=page_no, page_size=page_size, q=q, sellable=sellable)
        query_string = await create_query_string(company_id=company_id, item_id=item_id, size=size, page_no=page_no, page_size=page_size, q=q, sellable=sellable)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/products/{item_id}/sizes/{size}", company_id=company_id, item_id=item_id, size=size, page_no=page_no, page_size=page_size, q=q, sellable=sellable), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def addInventory(self, company_id=None, item_id=None, size=None, body=""):
        """This API allows add Inventory for particular size and store.
        :param company_id : Id of the company associated to product that is to be viewed. : type string
        :param item_id : Item code of the product of which size is to be get. : type number
        :param size : Size in which inventory is to be added. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if item_id:
            payload["item_id"] = item_id
        
        if size:
            payload["size"] = size
        

        # Parameter validation
        schema = CatalogValidator.addInventory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.InventoryRequest import InventoryRequest
        schema = InventoryRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/products/{item_id}/sizes/{size}", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Item code of the product of which size is to be get.","schema":{"type":"number"},"required":true},{"in":"path","name":"size","description":"Size in which inventory is to be added.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, item_id=item_id, size=size)
        query_string = await create_query_string(company_id=company_id, item_id=item_id, size=size)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/products/{item_id}/sizes/{size}", company_id=company_id, item_id=item_id, size=size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getInventoryBySizeIdentifier(self, company_id=None, item_id=None, size_identifier=None, page_no=None, page_size=None, q=None, location_ids=None, body=""):
        """This API allows get Inventory data for particular company grouped by size and store.
        :param company_id : Id of the company associated to product that is to be viewed. : type string
        :param item_id : Item code of the product of which size is to be get. : type string
        :param size_identifier : Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get. : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param q : Search with help of store code. : type string
        :param location_ids : Search by store ids. : type array
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if item_id:
            payload["item_id"] = item_id
        
        if size_identifier:
            payload["size_identifier"] = size_identifier
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if q:
            payload["q"] = q
        
        if location_ids:
            payload["location_ids"] = location_ids
        

        # Parameter validation
        schema = CatalogValidator.getInventoryBySizeIdentifier()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/products/{item_id}/inventory/{size_identifier}", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Item code of the product of which size is to be get.","schema":{"type":"string"},"required":true},{"in":"path","name":"size_identifier","description":"Size Identifier (Seller Identifier or Primary Identifier) of which inventory is to get.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search with help of store code.","schema":{"type":"string"},"required":false},{"in":"query","name":"location_ids","description":"Search by store ids.","schema":{"type":"array","items":{"type":"integer"}},"required":false}],"query":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search with help of store code.","schema":{"type":"string"},"required":false},{"in":"query","name":"location_ids","description":"Search by store ids.","schema":{"type":"array","items":{"type":"integer"}},"required":false}],"headers":[]}""", company_id=company_id, item_id=item_id, size_identifier=size_identifier, page_no=page_no, page_size=page_size, q=q, location_ids=location_ids)
        query_string = await create_query_string(company_id=company_id, item_id=item_id, size_identifier=size_identifier, page_no=page_no, page_size=page_size, q=q, location_ids=location_ids)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/products/{item_id}/inventory/{size_identifier}", company_id=company_id, item_id=item_id, size_identifier=size_identifier, page_no=page_no, page_size=page_size, q=q, location_ids=location_ids), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def deleteInventory(self, company_id=None, size=None, item_id=None, location_id=None, body=""):
        """This API allows to delete inventory of a particular product for particular company.
        :param company_id : Company Id of the company associated with Inventory that is to be deleted. : type string
        :param size : size that is to be deleted. : type string
        :param item_id : Id of the product associated with Inventory to be deleted. : type integer
        :param location_id : Location ID of store of which inventory is to be deleted. : type number
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if size:
            payload["size"] = size
        
        if item_id:
            payload["item_id"] = item_id
        
        if location_id:
            payload["location_id"] = location_id
        

        # Parameter validation
        schema = CatalogValidator.deleteInventory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/products/{item_id}/sizes/{size}/location/{location_id}/", """{"required":[{"in":"path","name":"company_id","description":"Company Id of the company associated with Inventory that is to be deleted.","schema":{"type":"string"},"required":true},{"in":"path","name":"size","description":"size that is to be deleted.","schema":{"type":"string"},"required":true},{"in":"path","name":"item_id","description":"Id of the product associated with Inventory to be deleted.","schema":{"type":"integer"},"required":true},{"in":"path","name":"location_id","description":"Location ID of store of which inventory is to be deleted.","schema":{"type":"number"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, size=size, item_id=item_id, location_id=location_id)
        query_string = await create_query_string(company_id=company_id, size=size, item_id=item_id, location_id=location_id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/products/{item_id}/sizes/{size}/location/{location_id}/", company_id=company_id, size=size, item_id=item_id, location_id=location_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getInventoryBulkUploadHistory(self, company_id=None, page_no=None, page_size=None, body=""):
        """This API helps to get bulk Inventory upload jobs data.
        :param company_id : Company Id of of which Inventory Bulk Upload History to be obtained. : type integer
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = CatalogValidator.getInventoryBulkUploadHistory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/inventory/bulk/", """{"required":[{"in":"path","name":"company_id","description":"Company Id of of which Inventory Bulk Upload History to be obtained.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false}],"query":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false}],"headers":[]}""", company_id=company_id, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(company_id=company_id, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/inventory/bulk/", company_id=company_id, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createBulkInventoryJob(self, company_id=None, body=""):
        """This API helps to create a bulk Inventory upload job.
        :param company_id : Company Id in which Inventory to be uploaded. : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = CatalogValidator.createBulkInventoryJob()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.BulkJob import BulkJob
        schema = BulkJob()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/inventory/bulk/", """{"required":[{"in":"path","name":"company_id","description":"Company Id in which Inventory to be uploaded.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/inventory/bulk/", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def deleteBulkInventoryJob(self, company_id=None, batch_id=None, body=""):
        """This API allows to delete bulk Inventory job associated with company.
        :param company_id : Company Id of the company of which bulk Inventory job is to be deleted. : type string
        :param batch_id : Batch Id of the bulk delete job. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if batch_id:
            payload["batch_id"] = batch_id
        

        # Parameter validation
        schema = CatalogValidator.deleteBulkInventoryJob()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/inventory/bulk/{batch_id}/", """{"required":[{"in":"path","name":"company_id","description":"Company Id of the company of which bulk Inventory job is to be deleted.","schema":{"type":"string"},"required":true},{"in":"path","name":"batch_id","description":"Batch Id of the bulk delete job.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, batch_id=batch_id)
        query_string = await create_query_string(company_id=company_id, batch_id=batch_id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/inventory/bulk/{batch_id}/", company_id=company_id, batch_id=batch_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createBulkInventory(self, company_id=None, batch_id=None, body=""):
        """This API helps to create products in bulk push to kafka for approval/creation.
        :param company_id : Company Id in which Inventory is to be uploaded. : type integer
        :param batch_id : Batch Id of the bulk create job. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if batch_id:
            payload["batch_id"] = batch_id
        

        # Parameter validation
        schema = CatalogValidator.createBulkInventory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.InventoryBulkRequest import InventoryBulkRequest
        schema = InventoryBulkRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/inventory/bulk/{batch_id}/", """{"required":[{"in":"path","name":"company_id","description":"Company Id in which Inventory is to be uploaded.","schema":{"type":"integer"},"required":true},{"in":"path","name":"batch_id","description":"Batch Id of the bulk create job.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, batch_id=batch_id)
        query_string = await create_query_string(company_id=company_id, batch_id=batch_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/inventory/bulk/{batch_id}/", company_id=company_id, batch_id=batch_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getInventoryExport(self, company_id=None, body=""):
        """This API helps to get Inventory export history.
        :param company_id : Company Id in which assets to be uploaded. : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = CatalogValidator.getInventoryExport()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/inventory/download/", """{"required":[{"in":"path","name":"company_id","description":"Company Id in which assets to be uploaded.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/inventory/download/", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createInventoryExportJob(self, company_id=None, body=""):
        """This API helps to create a Inventory export job.
        :param company_id : Company Id in which assets to be uploaded. : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = CatalogValidator.createInventoryExportJob()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.InventoryExportRequest import InventoryExportRequest
        schema = InventoryExportRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/inventory/download/", """{"required":[{"in":"path","name":"company_id","description":"Company Id in which assets to be uploaded.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/inventory/download/", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def exportInventoryConfig(self, company_id=None, filter_type=None, body=""):
        """This API allows get List of different filters like brand, store, and type for inventory export.
        :param company_id : Id of the company associated to product that is to be viewed. : type string
        :param filter_type : filter type from any one of ['brand', 'store', 'type'] : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if filter_type:
            payload["filter_type"] = filter_type
        

        # Parameter validation
        schema = CatalogValidator.exportInventoryConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/inventory/download/configuration/", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to product that is to be viewed.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"filter_type","description":"filter type from any one of ['brand', 'store', 'type']","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"filter_type","description":"filter type from any one of ['brand', 'store', 'type']","schema":{"type":"string"},"required":false}],"headers":[]}""", company_id=company_id, filter_type=filter_type)
        query_string = await create_query_string(company_id=company_id, filter_type=filter_type)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/inventory/download/configuration/", company_id=company_id, filter_type=filter_type), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getAllHsnCodes(self, company_id=None, page_no=None, page_size=None, q=None, body=""):
        """Hsn Code List.
        :param company_id : company id : type string
        :param page_no : page no : type integer
        :param page_size : page size : type integer
        :param q : search using hsn code. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if q:
            payload["q"] = q
        

        # Parameter validation
        schema = CatalogValidator.getAllHsnCodes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/hsn/", """{"required":[{"in":"path","name":"company_id","description":"company id","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"page no","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"page size","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"search using hsn code.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"page_no","description":"page no","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"page size","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"search using hsn code.","schema":{"type":"string"},"required":false}],"headers":[]}""", company_id=company_id, page_no=page_no, page_size=page_size, q=q)
        query_string = await create_query_string(company_id=company_id, page_no=page_no, page_size=page_size, q=q)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/hsn/", company_id=company_id, page_no=page_no, page_size=page_size, q=q), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createHsnCode(self, company_id=None, body=""):
        """Create Hsn Code.
        :param company_id : company id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = CatalogValidator.createHsnCode()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.HsnUpsert import HsnUpsert
        schema = HsnUpsert()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/hsn/", """{"required":[{"in":"path","name":"company_id","description":"company id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/hsn/", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getHsnCode(self, company_id=None, id=None, body=""):
        """Fetch Hsn Code.
        :param company_id : company id : type string
        :param id : Unique id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.getHsnCode()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/hsn/{id}/", """{"required":[{"in":"path","name":"company_id","description":"company id","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"Unique id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, id=id)
        query_string = await create_query_string(company_id=company_id, id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/hsn/{id}/", company_id=company_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateHsnCode(self, company_id=None, id=None, body=""):
        """Update Hsn Code.
        :param company_id : company id : type string
        :param id : Unique id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CatalogValidator.updateHsnCode()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.HsnUpsert import HsnUpsert
        schema = HsnUpsert()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/hsn/{id}/", """{"required":[{"in":"path","name":"company_id","description":"company id","schema":{"type":"string"},"required":true},{"in":"path","name":"id","description":"Unique id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, id=id)
        query_string = await create_query_string(company_id=company_id, id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/hsn/{id}/", company_id=company_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def bulkHsnCode(self, company_id=None, body=""):
        """Bulk Create or Update Hsn Code.
        :param company_id : company id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = CatalogValidator.bulkHsnCode()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.BulkHsnUpsert import BulkHsnUpsert
        schema = BulkHsnUpsert()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/hsn/bulk/", """{"required":[{"in":"path","name":"company_id","description":"company id","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/hsn/bulk/", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getApplicationBrands(self, company_id=None, application_id=None, department=None, page_no=None, page_size=None, body=""):
        """A brand is the name under which a product is being sold. Use this API to list all the brands. You can pass optionally filter the brands by the department. If successful, returns a paginated list of brands specified in `BrandListingResponse`
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param application_id : A `application_id` is a unique identifier for a particular sale channel. : type string
        :param department : The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the **v1.0/departments/** API : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if department:
            payload["department"] = department
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = CatalogValidator.getApplicationBrands()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/brands", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"department","description":"The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the **v1.0/departments/** API","schema":{"type":"string","enum":["baby-care-kids-essentials","beauty-personal-care","home-living","kids","men","others","toys","women"]},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false}],"query":[{"in":"query","name":"department","description":"The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the **v1.0/departments/** API","schema":{"type":"string","enum":["baby-care-kids-essentials","beauty-personal-care","home-living","kids","men","others","toys","women"]},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false}],"headers":[]}""", company_id=company_id, application_id=application_id, department=department, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, department=department, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/brands", company_id=company_id, application_id=application_id, department=department, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getDepartments(self, company_id=None, application_id=None, body=""):
        """Departments are a way to categorise similar products. A product can lie in multiple departments. For example, a skirt can below to the 'Women's Fashion' Department while a handbag can lie in 'Women's Accessories' Department. Use this API to list all the departments. If successful, returns the list of departments specified in `DepartmentResponse`
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param application_id : A `application_id` is a unique identifier for a particular sale channel. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = CatalogValidator.getDepartments()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/departments", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/departments", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getCategories(self, company_id=None, application_id=None, department=None, body=""):
        """List all the categories. You can optionally pass filter the brands by the department. If successful, returns a paginated list of brands specified in `CategoryListingResponse`
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param application_id : A `application_id` is a unique identifier for a particular sale channel. : type string
        :param department : The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the **v1.0/departments/** API : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if department:
            payload["department"] = department
        

        # Parameter validation
        schema = CatalogValidator.getCategories()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/categories", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"department","description":"The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the **v1.0/departments/** API","schema":{"type":"string","enum":["baby-care-kids-essentials","beauty-personal-care","home-living","kids","men","others","toys","women"]},"required":false}],"query":[{"in":"query","name":"department","description":"The name of the department. Use this parameter to filter products by a particular department. See below the list of available departments. You can retrieve available departments from the **v1.0/departments/** API","schema":{"type":"string","enum":["baby-care-kids-essentials","beauty-personal-care","home-living","kids","men","others","toys","women"]},"required":false}],"headers":[]}""", company_id=company_id, application_id=application_id, department=department)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, department=department)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/categories", company_id=company_id, application_id=application_id, department=department), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getAppicationProducts(self, company_id=None, application_id=None, q=None, f=None, filters=None, sort_on=None, page_id=None, page_size=None, page_no=None, page_type=None, item_ids=None, body=""):
        """List all the products associated with a brand, collection or category in a requested sort order. The API additionally supports arbitrary search queries that may refer the name of any product, brand, category or collection. If successful, returns a paginated list of products specified in `ApplicationProductListingResponse`
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param application_id : A `application_id` is a unique identifier for a particular sale channel. : type string
        :param q : The search query. This can be a partial or complete name of a either a product, brand or category : type string
        :param f : The search filter parameters. All the parameter filtered from filter parameters will be passed in **f** parameter in this format. **?f=brand:voi-jeans||and:::category:t-shirts||shirts** : type string
        :param filters : Pass `filters` parameter to fetch the filter details. This flag is used to fetch all filters : type boolean
        :param sort_on : The order to sort the list of products on. The supported sort parameters are popularity, price, redemption and discount in either ascending or descending order. See the supported values below. : type string
        :param page_id : Each response will contain **page_id** param, which should be sent back to make pagination work. : type string
        :param page_size : Number of items to retrieve in each page. Default is 12. : type integer
        :param page_no : If page_type is number then pass it to fetch page items. Default is 1. : type integer
        :param page_type : For pagination type should be cursor or number. Default is cursor. : type string
        :param item_ids : Item Ids of product : type array
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if q:
            payload["q"] = q
        
        if f:
            payload["f"] = f
        
        if filters:
            payload["filters"] = filters
        
        if sort_on:
            payload["sort_on"] = sort_on
        
        if page_id:
            payload["page_id"] = page_id
        
        if page_size:
            payload["page_size"] = page_size
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_type:
            payload["page_type"] = page_type
        
        if item_ids:
            payload["item_ids"] = item_ids
        

        # Parameter validation
        schema = CatalogValidator.getAppicationProducts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/products", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"q","description":"The search query. This can be a partial or complete name of a either a product, brand or category","schema":{"type":"string"},"required":false},{"in":"query","name":"f","description":"The search filter parameters. All the parameter filtered from filter parameters will be passed in **f** parameter in this format. **?f=brand:voi-jeans||and:::category:t-shirts||shirts**","schema":{"type":"string"},"required":false},{"in":"query","name":"filters","description":"Pass `filters` parameter to fetch the filter details. This flag is used to fetch all filters","schema":{"type":"boolean","default":true},"required":false},{"in":"query","name":"sort_on","description":"The order to sort the list of products on. The supported sort parameters are popularity, price, redemption and discount in either ascending or descending order. See the supported values below.","schema":{"type":"string","enum":["latest","popular","price_asc","price_dsc","discount_asc","discount_dsc"]},"required":false},{"in":"query","name":"page_id","description":"Each response will contain **page_id** param, which should be sent back to make pagination work.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"page_no","description":"If page_type is number then pass it to fetch page items. Default is 1.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_type","description":"For pagination type should be cursor or number. Default is cursor.","schema":{"type":"string","default":"cursor"},"required":false},{"in":"query","name":"item_ids","description":"Item Ids of product","schema":{"type":"array","items":{"type":"integer"}},"required":false}],"query":[{"in":"query","name":"q","description":"The search query. This can be a partial or complete name of a either a product, brand or category","schema":{"type":"string"},"required":false},{"in":"query","name":"f","description":"The search filter parameters. All the parameter filtered from filter parameters will be passed in **f** parameter in this format. **?f=brand:voi-jeans||and:::category:t-shirts||shirts**","schema":{"type":"string"},"required":false},{"in":"query","name":"filters","description":"Pass `filters` parameter to fetch the filter details. This flag is used to fetch all filters","schema":{"type":"boolean","default":true},"required":false},{"in":"query","name":"sort_on","description":"The order to sort the list of products on. The supported sort parameters are popularity, price, redemption and discount in either ascending or descending order. See the supported values below.","schema":{"type":"string","enum":["latest","popular","price_asc","price_dsc","discount_asc","discount_dsc"]},"required":false},{"in":"query","name":"page_id","description":"Each response will contain **page_id** param, which should be sent back to make pagination work.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 12.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"page_no","description":"If page_type is number then pass it to fetch page items. Default is 1.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_type","description":"For pagination type should be cursor or number. Default is cursor.","schema":{"type":"string","default":"cursor"},"required":false},{"in":"query","name":"item_ids","description":"Item Ids of product","schema":{"type":"array","items":{"type":"integer"}},"required":false}],"headers":[]}""", company_id=company_id, application_id=application_id, q=q, f=f, filters=filters, sort_on=sort_on, page_id=page_id, page_size=page_size, page_no=page_no, page_type=page_type, item_ids=item_ids)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, q=q, f=f, filters=filters, sort_on=sort_on, page_id=page_id, page_size=page_size, page_no=page_no, page_type=page_type, item_ids=item_ids)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/products", company_id=company_id, application_id=application_id, q=q, f=f, filters=filters, sort_on=sort_on, page_id=page_id, page_size=page_size, page_no=page_no, page_type=page_type, item_ids=item_ids), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getProductDetailBySlug(self, company_id=None, application_id=None, slug=None, body=""):
        """Products are the core resource of an application. Products can be associated by categories, collections, brands and more. This API retrieves the product specified by the given **slug**. If successful, returns a Product resource in the response body specified in `ProductDetail`
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param application_id : A `application_id` is a unique identifier for a particular sale channel. : type string
        :param slug : The unique identifier of a product. i.e; `slug` of a product. You can retrieve these from the APIs that list products like **v1.0/products/** : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if slug:
            payload["slug"] = slug
        

        # Parameter validation
        schema = CatalogValidator.getProductDetailBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/products/{slug}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"path","name":"slug","description":"The unique identifier of a product. i.e; `slug` of a product. You can retrieve these from the APIs that list products like **v1.0/products/**","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, slug=slug)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, slug=slug)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/products/{slug}", company_id=company_id, application_id=application_id, slug=slug), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getAppProducts(self, company_id=None, application_id=None, brand_ids=None, category_ids=None, department_ids=None, tags=None, page_no=None, page_size=None, q=None, body=""):
        """Products are the core resource of an application. Products can be associated by categories, collections, brands and more. If successful, returns a Product resource in the response body specified in `ApplicationProductListingResponseDatabasePowered`
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        :param application_id : A `application_id` is a unique identifier for a particular sale channel. : type string
        :param brand_ids : Get multiple products filtered by Brand Ids : type array
        :param category_ids : Get multiple products filtered by Category Ids : type array
        :param department_ids : Get multiple products filtered by Department Ids : type array
        :param tags : Get multiple products filtered by tags : type array
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 10. : type integer
        :param q : Search with Item Code, Name, Slug or Identifier. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if brand_ids:
            payload["brand_ids"] = brand_ids
        
        if category_ids:
            payload["category_ids"] = category_ids
        
        if department_ids:
            payload["department_ids"] = department_ids
        
        if tags:
            payload["tags"] = tags
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if q:
            payload["q"] = q
        

        # Parameter validation
        schema = CatalogValidator.getAppProducts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/raw-products/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"brand_ids","description":"Get multiple products filtered by Brand Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"category_ids","description":"Get multiple products filtered by Category Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"department_ids","description":"Get multiple products filtered by Department Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"tags","description":"Get multiple products filtered by tags","schema":{"type":"array","items":{"type":"string"}},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":10},"required":false},{"in":"query","name":"q","description":"Search with Item Code, Name, Slug or Identifier.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"brand_ids","description":"Get multiple products filtered by Brand Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"category_ids","description":"Get multiple products filtered by Category Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"department_ids","description":"Get multiple products filtered by Department Ids","schema":{"type":"array","items":{"type":"integer"}},"required":false},{"in":"query","name":"tags","description":"Get multiple products filtered by tags","schema":{"type":"array","items":{"type":"string"}},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":10},"required":false},{"in":"query","name":"q","description":"Search with Item Code, Name, Slug or Identifier.","schema":{"type":"string"},"required":false}],"headers":[]}""", company_id=company_id, application_id=application_id, brand_ids=brand_ids, category_ids=category_ids, department_ids=department_ids, tags=tags, page_no=page_no, page_size=page_size, q=q)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, brand_ids=brand_ids, category_ids=category_ids, department_ids=department_ids, tags=tags, page_no=page_no, page_size=page_size, q=q)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/application/{application_id}/raw-products/", company_id=company_id, application_id=application_id, brand_ids=brand_ids, category_ids=category_ids, department_ids=department_ids, tags=tags, page_no=page_no, page_size=page_size, q=q), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getOptimalLocations(self, company_id=None, body=""):
        """
        :param company_id : Id of the company inside which the location is to be created. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = CatalogValidator.getOptimalLocations()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.AssignStore import AssignStore
        schema = AssignStore()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/catalog/v1.0/company/{company_id}/location/reassign/", """{"required":[{"in":"path","name":"company_id","description":"Id of the company inside which the location is to be created.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/catalog/v1.0/company/{company_id}/location/reassign/", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    

class CompanyProfile:
    def __init__(self, config):
        self._conf = config
    # async def ():
    
    async def updateCompany(self, company_id=None, body=""):
        """This API allows to edit the company profile of the seller account.
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = CompanyProfileValidator.updateCompany()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.UpdateCompany import UpdateCompany
        schema = UpdateCompany()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/company-profile/v1.0/company/{company_id}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain("/service/platform/company-profile/v1.0/company/{company_id}", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def cbsOnboardGet(self, company_id=None, body=""):
        """This API allows to view the company profile of the seller account.
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = CompanyProfileValidator.cbsOnboardGet()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/company-profile/v1.0/company/{company_id}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/company-profile/v1.0/company/{company_id}", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getCompanyMetrics(self, company_id=None, body=""):
        """This API allows to view the company metrics, i.e. the status of its brand and stores. Also its allows to view the number of products, company documents & store documents which are verified and unverified.
        :param company_id : A `company_id` is a unique identifier for a particular seller account. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = CompanyProfileValidator.getCompanyMetrics()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/company-profile/v1.0/company/{company_id}/metrics", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/company-profile/v1.0/company/{company_id}/metrics", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getBrand(self, company_id=None, brand_id=None, body=""):
        """This API helps to get data associated to a particular brand.
        :param company_id : Id of the company associated to brand that is to be viewed. : type string
        :param brand_id : Id of the brand to be viewed. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if brand_id:
            payload["brand_id"] = brand_id
        

        # Parameter validation
        schema = CompanyProfileValidator.getBrand()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/company-profile/v1.0/company/{company_id}/brand/{brand_id}", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to brand that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"brand_id","description":"Id of the brand to be viewed.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, brand_id=brand_id)
        query_string = await create_query_string(company_id=company_id, brand_id=brand_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/company-profile/v1.0/company/{company_id}/brand/{brand_id}", company_id=company_id, brand_id=brand_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def editBrand(self, company_id=None, brand_id=None, body=""):
        """This API allows to edit meta of a brand.
        :param company_id : Id of the company associated to brand that is to be viewed. : type string
        :param brand_id : Id of the brand to be viewed. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if brand_id:
            payload["brand_id"] = brand_id
        

        # Parameter validation
        schema = CompanyProfileValidator.editBrand()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.CreateUpdateBrandRequestSerializer import CreateUpdateBrandRequestSerializer
        schema = CreateUpdateBrandRequestSerializer()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/company-profile/v1.0/company/{company_id}/brand/{brand_id}", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to brand that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"brand_id","description":"Id of the brand to be viewed.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, brand_id=brand_id)
        query_string = await create_query_string(company_id=company_id, brand_id=brand_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/company-profile/v1.0/company/{company_id}/brand/{brand_id}", company_id=company_id, brand_id=brand_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createBrand(self, company_id=None, body=""):
        """This API allows to create a brand associated to a company.
        :param company_id : Id of the company. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = CompanyProfileValidator.createBrand()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.CreateUpdateBrandRequestSerializer import CreateUpdateBrandRequestSerializer
        schema = CreateUpdateBrandRequestSerializer()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/company-profile/v1.0/company/{company_id}/brand", """{"required":[{"in":"path","name":"company_id","description":"Id of the company.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/company-profile/v1.0/company/{company_id}/brand", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createCompanyBrandMapping(self, company_id=None, body=""):
        """This API allows to create a company brand mapping, for a already existing brand in the system.
        :param company_id : Id of the company inside which the brand is to be mapped. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = CompanyProfileValidator.createCompanyBrandMapping()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.CompanyBrandPostRequestSerializer import CompanyBrandPostRequestSerializer
        schema = CompanyBrandPostRequestSerializer()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/company-profile/v1.0/company/{company_id}/company-brand", """{"required":[{"in":"path","name":"company_id","description":"Id of the company inside which the brand is to be mapped.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/company-profile/v1.0/company/{company_id}/company-brand", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getBrands(self, company_id=None, page_no=None, page_size=None, q=None, body=""):
        """This API helps to get view brands associated to a particular company.
        :param company_id : Id of the company. : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 10. : type integer
        :param q : Search term for name. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if q:
            payload["q"] = q
        

        # Parameter validation
        schema = CompanyProfileValidator.getBrands()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/company-profile/v1.0/company/{company_id}/company-brand", """{"required":[{"in":"path","name":"company_id","description":"Id of the company.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":20},"required":false},{"in":"query","name":"q","description":"Search term for name.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":20},"required":false},{"in":"query","name":"q","description":"Search term for name.","schema":{"type":"string"},"required":false}],"headers":[]}""", company_id=company_id, page_no=page_no, page_size=page_size, q=q)
        query_string = await create_query_string(company_id=company_id, page_no=page_no, page_size=page_size, q=q)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/company-profile/v1.0/company/{company_id}/company-brand", company_id=company_id, page_no=page_no, page_size=page_size, q=q), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createLocation(self, company_id=None, body=""):
        """This API allows to create a location associated to a company.
        :param company_id : Id of the company inside which the location is to be created. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = CompanyProfileValidator.createLocation()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.LocationSerializer import LocationSerializer
        schema = LocationSerializer()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/company-profile/v1.0/company/{company_id}/location", """{"required":[{"in":"path","name":"company_id","description":"Id of the company inside which the location is to be created.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/company-profile/v1.0/company/{company_id}/location", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getLocations(self, company_id=None, store_type=None, q=None, stage=None, page_no=None, page_size=None, body=""):
        """This API allows to view all the locations asscoiated to a company.
        :param company_id : Id of the company whose locations are to fetched : type string
        :param store_type : Helps to sort the location list on the basis of location type. : type string
        :param q : Query that is to be searched. : type string
        :param stage : to filter companies on basis of verified or unverified companies. : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 10. : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if store_type:
            payload["store_type"] = store_type
        
        if q:
            payload["q"] = q
        
        if stage:
            payload["stage"] = stage
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = CompanyProfileValidator.getLocations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/company-profile/v1.0/company/{company_id}/location", """{"required":[{"in":"path","name":"company_id","description":"Id of the company whose locations are to fetched","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"store_type","description":"Helps to sort the location list on the basis of location type.","schema":{"type":"string"},"required":false},{"in":"query","name":"q","description":"Query that is to be searched.","schema":{"type":"string"},"required":false},{"in":"query","name":"stage","description":"to filter companies on basis of verified or unverified companies.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":20},"required":false}],"query":[{"in":"query","name":"store_type","description":"Helps to sort the location list on the basis of location type.","schema":{"type":"string"},"required":false},{"in":"query","name":"q","description":"Query that is to be searched.","schema":{"type":"string"},"required":false},{"in":"query","name":"stage","description":"to filter companies on basis of verified or unverified companies.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":20},"required":false}],"headers":[]}""", company_id=company_id, store_type=store_type, q=q, stage=stage, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(company_id=company_id, store_type=store_type, q=q, stage=stage, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/company-profile/v1.0/company/{company_id}/location", company_id=company_id, store_type=store_type, q=q, stage=stage, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getLocationDetail(self, company_id=None, location_id=None, body=""):
        """This API helps to get data associated to a specific location.
        :param company_id : Id of the company inside which the location lies. : type string
        :param location_id : Id of the location which you want to view. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if location_id:
            payload["location_id"] = location_id
        

        # Parameter validation
        schema = CompanyProfileValidator.getLocationDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/company-profile/v1.0/company/{company_id}/location/{location_id}", """{"required":[{"in":"path","name":"company_id","description":"Id of the company inside which the location lies.","schema":{"type":"string"},"required":true},{"in":"path","name":"location_id","description":"Id of the location which you want to view.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, location_id=location_id)
        query_string = await create_query_string(company_id=company_id, location_id=location_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/company-profile/v1.0/company/{company_id}/location/{location_id}", company_id=company_id, location_id=location_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateLocation(self, company_id=None, location_id=None, body=""):
        """This API allows to edit a location associated to a company.
        :param company_id : Id of the company inside which the location is to be created. : type string
        :param location_id : Id of the location which you want to edit. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if location_id:
            payload["location_id"] = location_id
        

        # Parameter validation
        schema = CompanyProfileValidator.updateLocation()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.LocationSerializer import LocationSerializer
        schema = LocationSerializer()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/company-profile/v1.0/company/{company_id}/location/{location_id}", """{"required":[{"in":"path","name":"company_id","description":"Id of the company inside which the location is to be created.","schema":{"type":"string"},"required":true},{"in":"path","name":"location_id","description":"Id of the location which you want to edit.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, location_id=location_id)
        query_string = await create_query_string(company_id=company_id, location_id=location_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/company-profile/v1.0/company/{company_id}/location/{location_id}", company_id=company_id, location_id=location_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createLocationBulk(self, company_id=None, body=""):
        """This API allows to create a location associated to a company.
        :param company_id : Id of the company inside which the location is to be created. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = CompanyProfileValidator.createLocationBulk()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.BulkLocationSerializer import BulkLocationSerializer
        schema = BulkLocationSerializer()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/company-profile/v1.0/company/{company_id}/location/bulk", """{"required":[{"in":"path","name":"company_id","description":"Id of the company inside which the location is to be created.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/company-profile/v1.0/company/{company_id}/location/bulk", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    

class FileStorage:
    def __init__(self, config):
        self._conf = config
    # async def ():
    
    async def startUpload(self, namespace=None, company_id=None, body=""):
        """Uploads an arbitrarily sized buffer or blob.

It has three Major Steps:
* Start
* Upload
* Complete

### Start
Initiates the assets upload using `startUpload`.
It returns the storage link in response.

### Upload
Use the storage link to upload a file (Buffer or Blob) to the File Storage.
Make a `PUT` request on storage link received from `startUpload` api with file (Buffer or Blob) as a request body.

### Complete
After successfully upload, call `completeUpload` api to complete the upload process.
This operation will return the url for the uploaded file.

        :param namespace : bucket name : type string
        :param company_id : company_id : type integer
        """
        payload = {}
        
        if namespace:
            payload["namespace"] = namespace
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = FileStorageValidator.startUpload()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.StartRequest import StartRequest
        schema = StartRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/assets/v1.0/company/{company_id}/namespaces/{namespace}/upload/start/", """{"required":[{"name":"namespace","in":"path","description":"bucket name","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[]}""", namespace=namespace, company_id=company_id)
        query_string = await create_query_string(namespace=namespace, company_id=company_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/assets/v1.0/company/{company_id}/namespaces/{namespace}/upload/start/", namespace=namespace, company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def completeUpload(self, namespace=None, company_id=None, body=""):
        """Uploads an arbitrarily sized buffer or blob.

It has three Major Steps:
* Start
* Upload
* Complete

### Start
Initiates the assets upload using `startUpload`.
It returns the storage link in response.

### Upload
Use the storage link to upload a file (Buffer or Blob) to the File Storage.
Make a `PUT` request on storage link received from `startUpload` api with file (Buffer or Blob) as a request body.

### Complete
After successfully upload, call `completeUpload` api to complete the upload process.
This operation will return the url for the uploaded file.

        :param namespace : bucket name : type string
        :param company_id : company_id : type integer
        """
        payload = {}
        
        if namespace:
            payload["namespace"] = namespace
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = FileStorageValidator.completeUpload()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.StartResponse import StartResponse
        schema = StartResponse()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/assets/v1.0/company/{company_id}/namespaces/{namespace}/upload/complete/", """{"required":[{"name":"namespace","in":"path","description":"bucket name","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[]}""", namespace=namespace, company_id=company_id)
        query_string = await create_query_string(namespace=namespace, company_id=company_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/assets/v1.0/company/{company_id}/namespaces/{namespace}/upload/complete/", namespace=namespace, company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def appStartUpload(self, namespace=None, company_id=None, application_id=None, body=""):
        """Uploads an arbitrarily sized buffer or blob.

It has three Major Steps:
* Start
* Upload
* Complete

### Start
Initiates the assets upload using `appStartUpload`.
It returns the storage link in response.

### Upload
Use the storage link to upload a file (Buffer or Blob) to the File Storage.
Make a `PUT` request on storage link received from `appStartUpload` api with file (Buffer or Blob) as a request body.

### Complete
After successfully upload, call `appCompleteUpload` api to complete the upload process.
This operation will return the url for the uploaded file.

        :param namespace : bucket name : type string
        :param company_id : company_id : type integer
        :param application_id : application id : type string
        """
        payload = {}
        
        if namespace:
            payload["namespace"] = namespace
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = FileStorageValidator.appStartUpload()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.StartRequest import StartRequest
        schema = StartRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/assets/v1.0/company/{company_id}/application/{application_id}/namespaces/{namespace}/upload/start/", """{"required":[{"name":"namespace","in":"path","description":"bucket name","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", namespace=namespace, company_id=company_id, application_id=application_id)
        query_string = await create_query_string(namespace=namespace, company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/assets/v1.0/company/{company_id}/application/{application_id}/namespaces/{namespace}/upload/start/", namespace=namespace, company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def appCompleteUpload(self, namespace=None, company_id=None, application_id=None, body=""):
        """Uploads an arbitrarily sized buffer or blob.

It has three Major Steps:
* Start
* Upload
* Complete

### Start
Initiates the assets upload using `appStartUpload`.
It returns the storage link in response.

### Upload
Use the storage link to upload a file (Buffer or Blob) to the File Storage.
Make a `PUT` request on storage link received from `appStartUpload` api with file (Buffer or Blob) as a request body.

### Complete
After successfully upload, call `appCompleteUpload` api to complete the upload process.
This operation will return the url for the uploaded file.

        :param namespace : bucket name : type string
        :param company_id : company_id : type integer
        :param application_id : application id : type string
        """
        payload = {}
        
        if namespace:
            payload["namespace"] = namespace
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = FileStorageValidator.appCompleteUpload()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.StartResponse import StartResponse
        schema = StartResponse()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/assets/v1.0/company/{company_id}/application/{application_id}/namespaces/{namespace}/upload/complete/", """{"required":[{"name":"namespace","in":"path","description":"bucket name","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"application_id","in":"path","description":"application id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", namespace=namespace, company_id=company_id, application_id=application_id)
        query_string = await create_query_string(namespace=namespace, company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/assets/v1.0/company/{company_id}/application/{application_id}/namespaces/{namespace}/upload/complete/", namespace=namespace, company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getSignUrls(self, company_id=None, body=""):
        """Describe here
        :param company_id : company_id : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = FileStorageValidator.getSignUrls()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.SignUrlRequest import SignUrlRequest
        schema = SignUrlRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/assets/v1.0/company/{company_id}/sign-urls/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/assets/v1.0/company/{company_id}/sign-urls/", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def copyFiles(self, sync=None, company_id=None, body=""):
        """Copy Files
        :param sync : sync : type boolean
        :param company_id : company_id : type integer
        """
        payload = {}
        
        if sync:
            payload["sync"] = sync
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = FileStorageValidator.copyFiles()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.BulkRequest import BulkRequest
        schema = BulkRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/assets/v1.0/company/{company_id}/uploads/copy/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"name":"sync","in":"query","description":"sync","required":false,"schema":{"type":"boolean"}}],"query":[{"name":"sync","in":"query","description":"sync","required":false,"schema":{"type":"boolean"}}],"headers":[]}""", sync=sync, company_id=company_id)
        query_string = await create_query_string(sync=sync, company_id=company_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/assets/v1.0/company/{company_id}/uploads/copy/", sync=sync, company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def appCopyFiles(self, sync=None, company_id=None, application_id=None, body=""):
        """Copy Files
        :param sync : sync : type boolean
        :param company_id : company_id : type integer
        :param application_id : application_id : type integer
        """
        payload = {}
        
        if sync:
            payload["sync"] = sync
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = FileStorageValidator.appCopyFiles()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.BulkRequest import BulkRequest
        schema = BulkRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/assets/v1.0/company/{company_id}/application/{application_id}/uploads/copy/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"application_id","in":"path","description":"application_id","required":true,"schema":{"type":"integer"}}],"optional":[{"name":"sync","in":"query","description":"sync","required":false,"schema":{"type":"boolean"}}],"query":[{"name":"sync","in":"query","description":"sync","required":false,"schema":{"type":"boolean"}}],"headers":[]}""", sync=sync, company_id=company_id, application_id=application_id)
        query_string = await create_query_string(sync=sync, company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/assets/v1.0/company/{company_id}/application/{application_id}/uploads/copy/", sync=sync, company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def browse(self, namespace=None, company_id=None, page_no=None, body=""):
        """Browse Files
        :param namespace : bucket name : type string
        :param company_id : company_id : type integer
        :param page_no : page no : type integer
        """
        payload = {}
        
        if namespace:
            payload["namespace"] = namespace
        
        if company_id:
            payload["company_id"] = company_id
        
        if page_no:
            payload["page_no"] = page_no
        

        # Parameter validation
        schema = FileStorageValidator.browse()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/assets/v1.0/company/{company_id}/namespaces/{namespace}/browse/", """{"required":[{"name":"namespace","in":"path","description":"bucket name","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"name":"page_no","in":"query","description":"page no","required":false,"schema":{"type":"integer"}}],"query":[{"name":"page_no","in":"query","description":"page no","required":false,"schema":{"type":"integer"}}],"headers":[]}""", namespace=namespace, company_id=company_id, page_no=page_no)
        query_string = await create_query_string(namespace=namespace, company_id=company_id, page_no=page_no)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/assets/v1.0/company/{company_id}/namespaces/{namespace}/browse/", namespace=namespace, company_id=company_id, page_no=page_no), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def browse(self, namespace=None, company_id=None, application_id=None, page_no=None, body=""):
        """Browse Files
        :param namespace : bucket name : type string
        :param company_id : company_id : type integer
        :param application_id : application_id : type integer
        :param page_no : page no : type integer
        """
        payload = {}
        
        if namespace:
            payload["namespace"] = namespace
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if page_no:
            payload["page_no"] = page_no
        

        # Parameter validation
        schema = FileStorageValidator.browse()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/assets/v1.0/company/{company_id}/application/{application_id}/namespaces/{namespace}/browse/", """{"required":[{"name":"namespace","in":"path","description":"bucket name","required":true,"schema":{"type":"string"}},{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"application_id","in":"path","description":"application_id","required":true,"schema":{"type":"integer"}}],"optional":[{"name":"page_no","in":"query","description":"page no","required":false,"schema":{"type":"integer"}}],"query":[{"name":"page_no","in":"query","description":"page no","required":false,"schema":{"type":"integer"}}],"headers":[]}""", namespace=namespace, company_id=company_id, application_id=application_id, page_no=page_no)
        query_string = await create_query_string(namespace=namespace, company_id=company_id, application_id=application_id, page_no=page_no)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/assets/v1.0/company/{company_id}/application/{application_id}/namespaces/{namespace}/browse/", namespace=namespace, company_id=company_id, application_id=application_id, page_no=page_no), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def proxy(self, company_id=None, url=None, body=""):
        """Proxy
        :param company_id : company_id : type integer
        :param url : url : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if url:
            payload["url"] = url
        

        # Parameter validation
        schema = FileStorageValidator.proxy()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/assets/v1.0/company/{company_id}/proxy/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"url","in":"query","description":"url","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"url","in":"query","description":"url","required":true,"schema":{"type":"string"}}],"headers":[]}""", company_id=company_id, url=url)
        query_string = await create_query_string(company_id=company_id, url=url)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/assets/v1.0/company/{company_id}/proxy/", company_id=company_id, url=url), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    

class Share:
    def __init__(self, config):
        self._conf = config
    # async def ():
    
    async def createShortLink(self, company_id=None, application_id=None, body=""):
        """Create short link
        :param company_id : Company Id : type string
        :param application_id : Application Id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ShareValidator.createShortLink()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.ShortLinkReq import ShortLinkReq
        schema = ShortLinkReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/share/v1.0/company/{company_id}/application/{application_id}/links/short-link/", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/share/v1.0/company/{company_id}/application/{application_id}/links/short-link/", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getShortLinks(self, company_id=None, application_id=None, page_no=None, page_size=None, created_by=None, active=None, q=None, body=""):
        """Get short links
        :param company_id : Company Id : type string
        :param application_id : Application Id : type string
        :param page_no : Current page number : type integer
        :param page_size : Current page size : type integer
        :param created_by : Short link creator : type string
        :param active : Short link active status : type string
        :param q : Search text for original and short url : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if created_by:
            payload["created_by"] = created_by
        
        if active:
            payload["active"] = active
        
        if q:
            payload["q"] = q
        

        # Parameter validation
        schema = ShareValidator.getShortLinks()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/share/v1.0/company/{company_id}/application/{application_id}/links/short-link/", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"default":1,"type":"integer"}},{"name":"page_size","in":"query","description":"Current page size","required":false,"schema":{"default":10,"type":"integer"}},{"name":"created_by","in":"query","description":"Short link creator","required":false,"schema":{"type":"string","enum":["team"]}},{"name":"active","in":"query","description":"Short link active status","required":false,"schema":{"type":"string","enum":[true,false]}},{"name":"q","in":"query","description":"Search text for original and short url","required":false,"schema":{"type":"string"}}],"query":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"default":1,"type":"integer"}},{"name":"page_size","in":"query","description":"Current page size","required":false,"schema":{"default":10,"type":"integer"}},{"name":"created_by","in":"query","description":"Short link creator","required":false,"schema":{"type":"string","enum":["team"]}},{"name":"active","in":"query","description":"Short link active status","required":false,"schema":{"type":"string","enum":[true,false]}},{"name":"q","in":"query","description":"Search text for original and short url","required":false,"schema":{"type":"string"}}],"headers":[]}""", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, created_by=created_by, active=active, q=q)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, created_by=created_by, active=active, q=q)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/share/v1.0/company/{company_id}/application/{application_id}/links/short-link/", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, created_by=created_by, active=active, q=q), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getShortLinkByHash(self, company_id=None, application_id=None, hash=None, body=""):
        """Get short link by hash
        :param company_id : Company Id : type string
        :param application_id : Application Id : type string
        :param hash : Hash of short url : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if hash:
            payload["hash"] = hash
        

        # Parameter validation
        schema = ShareValidator.getShortLinkByHash()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/share/v1.0/company/{company_id}/application/{application_id}/links/short-link/{hash}/", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"hash","in":"path","description":"Hash of short url","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, hash=hash)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, hash=hash)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/share/v1.0/company/{company_id}/application/{application_id}/links/short-link/{hash}/", company_id=company_id, application_id=application_id, hash=hash), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateShortLinkById(self, company_id=None, application_id=None, id=None, body=""):
        """Update short link by id
        :param company_id : Company Id : type string
        :param application_id : Application Id : type string
        :param id : Short link document identifier : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ShareValidator.updateShortLinkById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.ShortLinkReq import ShortLinkReq
        schema = ShortLinkReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/share/v1.0/company/{company_id}/application/{application_id}/links/short-link/{id}/", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"id","in":"path","description":"Short link document identifier","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain("/service/platform/share/v1.0/company/{company_id}/application/{application_id}/links/short-link/{id}/", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    

class Inventory:
    def __init__(self, config):
        self._conf = config
    # async def ():
    
    async def getJobsByCompany(self, company_id=None, page_no=None, page_size=None, body=""):
        """REST Endpoint that returns all job configs for a company
        :param company_id : Company Id : type integer
        :param page_no : Page Number : type integer
        :param page_size : Page Size : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = InventoryValidator.getJobsByCompany()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/inventory/v1.0/company/{company_id}/jobs", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}}],"optional":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer","format":"int32","default":1}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32","default":10}}],"query":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer","format":"int32","default":1}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32","default":10}}],"headers":[]}""", company_id=company_id, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(company_id=company_id, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/inventory/v1.0/company/{company_id}/jobs", company_id=company_id, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateJob(self, company_id=None, body=""):
        """REST Endpoint that updates a job config
        :param company_id : Company Id : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = InventoryValidator.updateJob()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.JobConfigDTO import JobConfigDTO
        schema = JobConfigDTO()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/inventory/v1.0/company/{company_id}/jobs", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/inventory/v1.0/company/{company_id}/jobs", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createJob(self, company_id=None, body=""):
        """REST Endpoint that creates a new job config
        :param company_id : Company Id : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = InventoryValidator.createJob()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.JobConfigDTO import JobConfigDTO
        schema = JobConfigDTO()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/inventory/v1.0/company/{company_id}/jobs", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/inventory/v1.0/company/{company_id}/jobs", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getJobSteps(self, company_id=None, job_id=None, body=""):
        """REST Endpoint that returns Inventory Job Steps
        :param company_id : Company Id : type integer
        :param job_id : Job Id : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if job_id:
            payload["job_id"] = job_id
        

        # Parameter validation
        schema = InventoryValidator.getJobSteps()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/inventory/v1.0/company/{company_id}/jobs/steps/{job_id}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"job_id","in":"path","description":"Job Id","required":true,"schema":{"type":"integer","format":"int32"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, job_id=job_id)
        query_string = await create_query_string(company_id=company_id, job_id=job_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/inventory/v1.0/company/{company_id}/jobs/steps/{job_id}", company_id=company_id, job_id=job_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getJobByCompanyAndIntegration(self, company_id=None, integration_id=None, page_no=None, page_size=None, body=""):
        """REST Endpoint that returns all job configs by company And integration
        :param company_id : Company Id : type integer
        :param integration_id : Integration Id : type string
        :param page_no : Page Number : type integer
        :param page_size : Page Size : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if integration_id:
            payload["integration_id"] = integration_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = InventoryValidator.getJobByCompanyAndIntegration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/inventory/v1.0/company/{company_id}/jobs/integration/{integration_id}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"integration_id","in":"path","description":"Integration Id","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer","format":"int32","default":1}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32","default":10}}],"query":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer","format":"int32","default":1}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32","default":10}}],"headers":[]}""", company_id=company_id, integration_id=integration_id, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(company_id=company_id, integration_id=integration_id, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/inventory/v1.0/company/{company_id}/jobs/integration/{integration_id}", company_id=company_id, integration_id=integration_id, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def disable(self, company_id=None, integration_id=None, body=""):
        """REST Endpoint that disables Inventory Job Config
        :param company_id : Company Id : type integer
        :param integration_id : IntegrationId : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if integration_id:
            payload["integration_id"] = integration_id
        

        # Parameter validation
        schema = InventoryValidator.disable()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/inventory/v1.0/company/{company_id}/jobs/disable/integration/{integration_id}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"integration_id","in":"path","description":"IntegrationId","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, integration_id=integration_id)
        query_string = await create_query_string(company_id=company_id, integration_id=integration_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/inventory/v1.0/company/{company_id}/jobs/disable/integration/{integration_id}", company_id=company_id, integration_id=integration_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getJobConfigDefaults(self, company_id=None, body=""):
        """REST Endpoint that returns default fields job configs by company And integration
        :param company_id : Company Id : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = InventoryValidator.getJobConfigDefaults()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/inventory/v1.0/company/{company_id}/jobs/defaults", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/inventory/v1.0/company/{company_id}/jobs/defaults", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getJobByCode(self, company_id=None, code=None, body=""):
        """REST Endpoint that returns job config by code
        :param company_id : Company Id : type integer
        :param code : Job Code : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if code:
            payload["code"] = code
        

        # Parameter validation
        schema = InventoryValidator.getJobByCode()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/inventory/v1.0/company/{company_id}/jobs/code/{code}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"code","in":"path","description":"Job Code","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, code=code)
        query_string = await create_query_string(company_id=company_id, code=code)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/inventory/v1.0/company/{company_id}/jobs/code/{code}", company_id=company_id, code=code), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getJobCodeMetrics(self, company_id=None, code=None, page_no=None, page_size=None, status=None, date=None, body=""):
        """REST Endpoint that returns Inventory Run History For A Job Code
        :param company_id : Company Id : type integer
        :param code : Code : type string
        :param page_no : Page Number : type integer
        :param page_size : Page Size : type integer
        :param status : Status : type string
        :param date : From Date : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if code:
            payload["code"] = code
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if status:
            payload["status"] = status
        
        if date:
            payload["date"] = date
        

        # Parameter validation
        schema = InventoryValidator.getJobCodeMetrics()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/inventory/v1.0/company/{company_id}/jobs/code/{code}/metrics", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"code","in":"path","description":"Code","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer","format":"int32","default":1}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32","default":10}},{"name":"status","in":"query","description":"Status","required":false,"schema":{"type":"string"}},{"name":"date","in":"query","description":"From Date","required":false,"schema":{"type":"string","format":"date-time"}}],"query":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer","format":"int32","default":1}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32","default":10}},{"name":"status","in":"query","description":"Status","required":false,"schema":{"type":"string"}},{"name":"date","in":"query","description":"From Date","required":false,"schema":{"type":"string","format":"date-time"}}],"headers":[]}""", company_id=company_id, code=code, page_no=page_no, page_size=page_size, status=status, date=date)
        query_string = await create_query_string(company_id=company_id, code=code, page_no=page_no, page_size=page_size, status=status, date=date)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/inventory/v1.0/company/{company_id}/jobs/code/{code}/metrics", company_id=company_id, code=code, page_no=page_no, page_size=page_size, status=status, date=date), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getJobCodesByCompanyAndIntegration(self, company_id=None, integration_id=None, page_no=None, page_size=None, body=""):
        """REST Endpoint that returns all job codes by company And integration
        :param company_id : Company Id : type integer
        :param integration_id : Integration Id : type string
        :param page_no : Page Number : type integer
        :param page_size : Page Size : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if integration_id:
            payload["integration_id"] = integration_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = InventoryValidator.getJobCodesByCompanyAndIntegration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/inventory/v1.0/company/{company_id}/jobs/code/integration/{integration_id}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"integration_id","in":"path","description":"Integration Id","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer","format":"int32","default":1}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32","default":10}}],"query":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer","format":"int32","default":1}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32","default":10}}],"headers":[]}""", company_id=company_id, integration_id=integration_id, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(company_id=company_id, integration_id=integration_id, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/inventory/v1.0/company/{company_id}/jobs/code/integration/{integration_id}", company_id=company_id, integration_id=integration_id, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    

class Configuration:
    def __init__(self, config):
        self._conf = config
    # async def ():
    
    async def getBuildConfig(self, company_id=None, application_id=None, platform_type=None, body=""):
        """Get latest build config
        :param company_id : Current company id : type string
        :param application_id : Current application id : type string
        :param platform_type : Current platform name : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if platform_type:
            payload["platform_type"] = platform_type
        

        # Parameter validation
        schema = ConfigurationValidator.getBuildConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/build/{platform_type}/configuration", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"},{"schema":{"type":"string","enum":["android","ios"]},"description":"Current platform name","in":"path","required":true,"name":"platform_type"}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, platform_type=platform_type)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, platform_type=platform_type)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/build/{platform_type}/configuration", company_id=company_id, application_id=application_id, platform_type=platform_type), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateBuildConfig(self, company_id=None, application_id=None, platform_type=None, body=""):
        """Update build config for next build
        :param company_id : Current company id : type string
        :param application_id : Current application id : type string
        :param platform_type : Current platform name : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if platform_type:
            payload["platform_type"] = platform_type
        

        # Parameter validation
        schema = ConfigurationValidator.updateBuildConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.MobileAppConfigRequest import MobileAppConfigRequest
        schema = MobileAppConfigRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/build/{platform_type}/configuration", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"},{"schema":{"type":"string","enum":["android","ios"]},"description":"Current platform name","in":"path","required":true,"name":"platform_type"}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, platform_type=platform_type)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, platform_type=platform_type)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/build/{platform_type}/configuration", company_id=company_id, application_id=application_id, platform_type=platform_type), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getPreviousVersions(self, company_id=None, application_id=None, platform_type=None, body=""):
        """Get previous build versions
        :param company_id : Current company id : type string
        :param application_id : Current application id : type string
        :param platform_type : Current platform name : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if platform_type:
            payload["platform_type"] = platform_type
        

        # Parameter validation
        schema = ConfigurationValidator.getPreviousVersions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/build/{platform_type}/versions", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"},{"schema":{"type":"string","enum":["android","ios"]},"description":"Current platform name","in":"path","required":true,"name":"platform_type"}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, platform_type=platform_type)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, platform_type=platform_type)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/build/{platform_type}/versions", company_id=company_id, application_id=application_id, platform_type=platform_type), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getAppFeatures(self, company_id=None, application_id=None, body=""):
        """Get features of application
        :param company_id : Current company id : type string
        :param application_id : Current application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ConfigurationValidator.getAppFeatures()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/feature", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/feature", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateAppFeatures(self, company_id=None, application_id=None, body=""):
        """Update features of application
        :param company_id : Current company id : type string
        :param application_id : Current application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ConfigurationValidator.updateAppFeatures()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.AppFeatureRequest import AppFeatureRequest
        schema = AppFeatureRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/feature", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/feature", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getAppBasicDetails(self, company_id=None, application_id=None, body=""):
        """Get basic application details like name
        :param company_id : Current company id : type string
        :param application_id : Current application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ConfigurationValidator.getAppBasicDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/detail", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/detail", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateAppBasicDetails(self, company_id=None, application_id=None, body=""):
        """Add or update application's basic details
        :param company_id : Current company id : type string
        :param application_id : Current application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ConfigurationValidator.updateAppBasicDetails()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.ApplicationDetail import ApplicationDetail
        schema = ApplicationDetail()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/detail", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/detail", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getAppContactInfo(self, company_id=None, application_id=None, body=""):
        """Get Application Current Information. This includes information about social links, address and contact information of company/seller/brand of the application.
        :param company_id : Current company id : type string
        :param application_id : Current application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ConfigurationValidator.getAppContactInfo()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/information", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/information", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateAppContactInfo(self, company_id=None, application_id=None, body=""):
        """Save Application Current Information. This includes information about social links, address and contact information of an application.
        :param company_id : Current company id : type string
        :param application_id : Current application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ConfigurationValidator.updateAppContactInfo()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.ApplicationInformation import ApplicationInformation
        schema = ApplicationInformation()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/information", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/information", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getAppApiTokens(self, company_id=None, application_id=None, body=""):
        """Get social tokens.
        :param company_id : Current company id : type string
        :param application_id : Current application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ConfigurationValidator.getAppApiTokens()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/token", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/token", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateAppApiTokens(self, company_id=None, application_id=None, body=""):
        """Add social tokens.
        :param company_id : Current company id : type string
        :param application_id : Current application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ConfigurationValidator.updateAppApiTokens()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.TokenResponse import TokenResponse
        schema = TokenResponse()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/token", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/token", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getAppCompanies(self, company_id=None, application_id=None, page_no=None, page_size=None, body=""):
        """Application inventory enabled companies.
        :param company_id : Current company id : type string
        :param application_id : Current application id : type string
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ConfigurationValidator.getAppCompanies()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/companies", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"headers":[]}""", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/companies", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getAppStores(self, company_id=None, application_id=None, page_no=None, page_size=None, body=""):
        """Application inventory enabled stores.
        :param company_id : Current company id : type string
        :param application_id : Current application id : type string
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ConfigurationValidator.getAppStores()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/stores", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"headers":[]}""", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/stores", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getInventoryConfig(self, company_id=None, application_id=None, body=""):
        """Get application configuration for various features and data
        :param company_id : Current company id : type string
        :param application_id : Current application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ConfigurationValidator.getInventoryConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/configuration", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/configuration", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateInventoryConfig(self, company_id=None, application_id=None, body=""):
        """Update application configuration for various features and data
        :param company_id : Current company id : type string
        :param application_id : Current application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ConfigurationValidator.updateInventoryConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.ApplicationInventory import ApplicationInventory
        schema = ApplicationInventory()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/configuration", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/configuration", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def partiallyUpdateInventoryConfig(self, company_id=None, application_id=None, body=""):
        """Partially update application configuration for various features and data
        :param company_id : Current company id : type string
        :param application_id : Current application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ConfigurationValidator.partiallyUpdateInventoryConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.AppInventoryPartialUpdate import AppInventoryPartialUpdate
        schema = AppInventoryPartialUpdate()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/configuration", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/configuration", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getAppCurrencyConfig(self, company_id=None, application_id=None, body=""):
        """Get application enabled currency list
        :param company_id : Current company id : type string
        :param application_id : Current application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ConfigurationValidator.getAppCurrencyConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/currency", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/currency", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateAppCurrencyConfig(self, company_id=None, application_id=None, body=""):
        """Add initial application supported currency for various features and data. Default INR will be enabled.
        :param company_id : Current company id : type string
        :param application_id : Current application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ConfigurationValidator.updateAppCurrencyConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.AppSupportedCurrency import AppSupportedCurrency
        schema = AppSupportedCurrency()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/currency", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/currency", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getAppSupportedCurrency(self, company_id=None, application_id=None, body=""):
        """Use this API to get a list of currencies allowed in the current application. Moreover, get the name, code, symbol, and the decimal digits of the currencies.
        :param company_id : Current company id : type string
        :param application_id : Current application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ConfigurationValidator.getAppSupportedCurrency()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/currency/supported", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/currency/supported", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getOrderingStoresByFilter(self, company_id=None, application_id=None, page_no=None, page_size=None, body=""):
        """Get ordering store by filter
        :param company_id : Current company id : type string
        :param application_id : Current application id : type string
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ConfigurationValidator.getOrderingStoresByFilter()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.FilterOrderingStoreRequest import FilterOrderingStoreRequest
        schema = FilterOrderingStoreRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/ordering-store/stores/filter", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"headers":[]}""", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/ordering-store/stores/filter", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateOrderingStoreConfig(self, company_id=None, application_id=None, body=""):
        """Add/Update ordering store config.
        :param company_id : Current company id : type string
        :param application_id : Current application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ConfigurationValidator.updateOrderingStoreConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.OrderingStoreConfig import OrderingStoreConfig
        schema = OrderingStoreConfig()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/ordering-store", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/ordering-store", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getStaffOrderingStores(self, company_id=None, application_id=None, page_no=None, page_size=None, q=None, body=""):
        """Use this API to retrieve the details of all stores access given to the staff member (the selling locations where the application will be utilized for placing orders).
        :param company_id : Current company id : type string
        :param application_id : Current application id : type string
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        :param q : Store code or name of the ordering store. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if q:
            payload["q"] = q
        

        # Parameter validation
        schema = ConfigurationValidator.getStaffOrderingStores()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/ordering-store/staff-stores", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."},{"name":"q","in":"query","schema":{"type":"string"},"description":"Store code or name of the ordering store."}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."},{"name":"q","in":"query","schema":{"type":"string"},"description":"Store code or name of the ordering store."}],"headers":[]}""", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, q=q)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, q=q)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/ordering-store/staff-stores", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, q=q), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getDomains(self, company_id=None, application_id=None, body=""):
        """Get attached domain list.
        :param company_id : Current company id : type string
        :param application_id : Current application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ConfigurationValidator.getDomains()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/domain", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/domain", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def addDomain(self, company_id=None, application_id=None, body=""):
        """Add new domain to application.
        :param company_id : Current company id : type string
        :param application_id : Current application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ConfigurationValidator.addDomain()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.DomainAddRequest import DomainAddRequest
        schema = DomainAddRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/domain", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/domain", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def removeDomainById(self, company_id=None, application_id=None, id=None, body=""):
        """Remove attached domain.
        :param company_id : Current company id : type string
        :param application_id : Current application id : type string
        :param id : Domain _id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ConfigurationValidator.removeDomainById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/domain/{id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","required":true,"description":"Domain _id","schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/domain/{id}", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def changeDomainType(self, company_id=None, application_id=None, body=""):
        """Change a domain to Primary or Shortlink domain
        :param company_id : Current company id : type string
        :param application_id : Current application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ConfigurationValidator.changeDomainType()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.UpdateDomainTypeRequest import UpdateDomainTypeRequest
        schema = UpdateDomainTypeRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/domain/set-domain", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/domain/set-domain", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getDomainStatus(self, company_id=None, application_id=None, body=""):
        """Get domain connected status. Check if domain is live and mapped to appropriate IP to fynd servers.
        :param company_id : Current company id : type string
        :param application_id : Current application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ConfigurationValidator.getDomainStatus()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.DomainStatusRequest import DomainStatusRequest
        schema = DomainStatusRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/domain/domain-status", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}/domain/domain-status", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createApplication(self, company_id=None, body=""):
        """Create new application
        :param company_id : Current company id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = ConfigurationValidator.createApplication()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.CreateApplicationRequest import CreateApplicationRequest
        schema = CreateApplicationRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/application", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/application", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getApplications(self, company_id=None, page_no=None, page_size=None, q=None, body=""):
        """Get list of application under company
        :param company_id : Current company id : type string
        :param page_no :  : type integer
        :param page_size :  : type integer
        :param q : Url encoded object used as mongodb query : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if q:
            payload["q"] = q
        

        # Parameter validation
        schema = ConfigurationValidator.getApplications()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/application", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}],"optional":[{"in":"query","name":"page_no","schema":{"type":"integer"}},{"name":"page_size","schema":{"type":"integer"},"in":"query"},{"name":"q","schema":{"type":"string"},"in":"query","description":"Url encoded object used as mongodb query"}],"query":[{"in":"query","name":"page_no","schema":{"type":"integer"}},{"name":"page_size","schema":{"type":"integer"},"in":"query"},{"name":"q","schema":{"type":"string"},"in":"query","description":"Url encoded object used as mongodb query"}],"headers":[]}""", company_id=company_id, page_no=page_no, page_size=page_size, q=q)
        query_string = await create_query_string(company_id=company_id, page_no=page_no, page_size=page_size, q=q)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/application", company_id=company_id, page_no=page_no, page_size=page_size, q=q), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getApplicationById(self, company_id=None, application_id=None, body=""):
        """Get application data from id
        :param company_id : Current company id : type string
        :param application_id : Current application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = ConfigurationValidator.getApplicationById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/application/{application_id}", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getCurrencies(self, company_id=None, body=""):
        """Get all currencies
        :param company_id : Current company id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = ConfigurationValidator.getCurrencies()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/currencies", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/currencies", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getDomainAvailibility(self, company_id=None, body=""):
        """Check domain availibility before linking to application. Also sends domain suggestions with similar to queried domain. \ Custom domain search is currently powered by GoDaddy provider.
        :param company_id : Current company id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = ConfigurationValidator.getDomainAvailibility()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.DomainSuggestionsRequest import DomainSuggestionsRequest
        schema = DomainSuggestionsRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/domain/suggestions", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/domain/suggestions", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getIntegrationById(self, company_id=None, id=None, body=""):
        """Get integration data
        :param company_id : Current company id : type string
        :param id : Integration id : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ConfigurationValidator.getIntegrationById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/integration/{id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"integer"},"description":"Integration id","required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, id=id)
        query_string = await create_query_string(company_id=company_id, id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/integration/{id}", company_id=company_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getAvailableOptIns(self, company_id=None, page_no=None, page_size=None, body=""):
        """Get all available integration opt-ins
        :param company_id : Current company id : type string
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ConfigurationValidator.getAvailableOptIns()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/integration-opt-in/available", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"headers":[]}""", company_id=company_id, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(company_id=company_id, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/integration-opt-in/available", company_id=company_id, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getSelectedOptIns(self, company_id=None, level=None, uid=None, page_no=None, page_size=None, body=""):
        """Get company/store level integration opt-ins
        :param company_id : Current company id : type string
        :param level : Integration level : type string
        :param uid : Integration level uid : type integer
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if level:
            payload["level"] = level
        
        if uid:
            payload["uid"] = uid
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ConfigurationValidator.getSelectedOptIns()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/integration-opt-in/selected/{level}/{uid}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"level","in":"path","schema":{"type":"string"},"description":"Integration level","required":true},{"name":"uid","in":"path","schema":{"type":"integer"},"description":"Integration level uid","required":true}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"headers":[]}""", company_id=company_id, level=level, uid=uid, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(company_id=company_id, level=level, uid=uid, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/integration-opt-in/selected/{level}/{uid}", company_id=company_id, level=level, uid=uid, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getIntegrationLevelConfig(self, company_id=None, id=None, level=None, opted=None, check_permission=None, body=""):
        """Get integration/integration-opt-in level config
        :param company_id : Current company id : type string
        :param id : Integration id : type string
        :param level : Integration level : type string
        :param opted : Filter on opted stores : type boolean
        :param check_permission : Filter on if permissions are present : type boolean
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if id:
            payload["id"] = id
        
        if level:
            payload["level"] = level
        
        if opted:
            payload["opted"] = opted
        
        if check_permission:
            payload["check_permission"] = check_permission
        

        # Parameter validation
        schema = ConfigurationValidator.getIntegrationLevelConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/integration-opt-in/configuration/new/{id}/{level}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration id","required":true},{"name":"level","in":"path","schema":{"type":"string"},"description":"Integration level","required":true}],"optional":[{"name":"opted","in":"query","schema":{"type":"boolean"},"description":"Filter on opted stores","required":false},{"name":"check_permission","in":"query","schema":{"type":"boolean"},"description":"Filter on if permissions are present","required":false}],"query":[{"name":"opted","in":"query","schema":{"type":"boolean"},"description":"Filter on opted stores","required":false},{"name":"check_permission","in":"query","schema":{"type":"boolean"},"description":"Filter on if permissions are present","required":false}],"headers":[]}""", company_id=company_id, id=id, level=level, opted=opted, check_permission=check_permission)
        query_string = await create_query_string(company_id=company_id, id=id, level=level, opted=opted, check_permission=check_permission)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/integration-opt-in/configuration/new/{id}/{level}", company_id=company_id, id=id, level=level, opted=opted, check_permission=check_permission), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getIntegrationByLevelId(self, company_id=None, id=None, level=None, uid=None, body=""):
        """Get level data for integration
        :param company_id : Current company id : type string
        :param id : Integration id : type string
        :param level : Integration level : type string
        :param uid : Integration level uid : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if id:
            payload["id"] = id
        
        if level:
            payload["level"] = level
        
        if uid:
            payload["uid"] = uid
        

        # Parameter validation
        schema = ConfigurationValidator.getIntegrationByLevelId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/integration-opt-in/configuration/{id}/{level}/{uid}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration id","required":true},{"name":"level","in":"path","schema":{"type":"string"},"description":"Integration level","required":true},{"name":"uid","in":"path","schema":{"type":"integer"},"description":"Integration level uid","required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, id=id, level=level, uid=uid)
        query_string = await create_query_string(company_id=company_id, id=id, level=level, uid=uid)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/integration-opt-in/configuration/{id}/{level}/{uid}", company_id=company_id, id=id, level=level, uid=uid), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateLevelUidIntegration(self, company_id=None, id=None, level=None, uid=None, body=""):
        """Update a store level opt-in for integration
        :param company_id : Current company id : type string
        :param id : Integration id : type string
        :param level : Integration level : type string
        :param uid : Integration level uid : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if id:
            payload["id"] = id
        
        if level:
            payload["level"] = level
        
        if uid:
            payload["uid"] = uid
        

        # Parameter validation
        schema = ConfigurationValidator.updateLevelUidIntegration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.IntegrationLevel import IntegrationLevel
        schema = IntegrationLevel()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/integration-opt-in/configuration/{id}/{level}/{uid}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration id","required":true},{"name":"level","in":"path","schema":{"type":"string"},"description":"Integration level","required":true},{"name":"uid","in":"path","schema":{"type":"integer"},"description":"Integration level uid","required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, id=id, level=level, uid=uid)
        query_string = await create_query_string(company_id=company_id, id=id, level=level, uid=uid)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/integration-opt-in/configuration/{id}/{level}/{uid}", company_id=company_id, id=id, level=level, uid=uid), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getLevelActiveIntegrations(self, company_id=None, id=None, level=None, uid=None, body=""):
        """API checks if a store is already opted in any other integrations
        :param company_id : Current company id : type string
        :param id : Integration id : type string
        :param level : Integration level : type string
        :param uid : Integration level uid : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if id:
            payload["id"] = id
        
        if level:
            payload["level"] = level
        
        if uid:
            payload["uid"] = uid
        

        # Parameter validation
        schema = ConfigurationValidator.getLevelActiveIntegrations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/integration-opt-in/check/configuration/{id}/{level}/{uid}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration id","required":true},{"name":"level","in":"path","schema":{"type":"string"},"description":"Integration level","required":true},{"name":"uid","in":"path","schema":{"type":"integer"},"description":"Integration level uid","required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, id=id, level=level, uid=uid)
        query_string = await create_query_string(company_id=company_id, id=id, level=level, uid=uid)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/integration-opt-in/check/configuration/{id}/{level}/{uid}", company_id=company_id, id=id, level=level, uid=uid), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateLevelIntegration(self, company_id=None, id=None, level=None, body=""):
        """Update a store level opt-in for integration
        :param company_id : Current company id : type string
        :param id : Integration id : type string
        :param level : Integration level : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if id:
            payload["id"] = id
        
        if level:
            payload["level"] = level
        

        # Parameter validation
        schema = ConfigurationValidator.updateLevelIntegration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.UpdateIntegrationLevelRequest import UpdateIntegrationLevelRequest
        schema = UpdateIntegrationLevelRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/integration-opt-in/configuration/{id}/{level}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Integration id","required":true},{"name":"level","in":"path","schema":{"type":"string"},"description":"Integration level","required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, id=id, level=level)
        query_string = await create_query_string(company_id=company_id, id=id, level=level)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/integration-opt-in/configuration/{id}/{level}", company_id=company_id, id=id, level=level), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getBrandsByCompany(self, company_id=None, q=None, body=""):
        """Get brands by company
        :param company_id : Current company id : type string
        :param q : Search text for brand name : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if q:
            payload["q"] = q
        

        # Parameter validation
        schema = ConfigurationValidator.getBrandsByCompany()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/inventory/brands-by-companies", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}],"optional":[{"name":"q","in":"query","schema":{"type":"string"},"description":"Search text for brand name"}],"query":[{"name":"q","in":"query","schema":{"type":"string"},"description":"Search text for brand name"}],"headers":[]}""", company_id=company_id, q=q)
        query_string = await create_query_string(company_id=company_id, q=q)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/inventory/brands-by-companies", company_id=company_id, q=q), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getCompanyByBrands(self, company_id=None, page_no=None, page_size=None, body=""):
        """Get company by brand uids
        :param company_id : Current company id : type string
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ConfigurationValidator.getCompanyByBrands()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.CompanyByBrandsRequest import CompanyByBrandsRequest
        schema = CompanyByBrandsRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/inventory/companies-by-brands", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"headers":[]}""", company_id=company_id, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(company_id=company_id, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/inventory/companies-by-brands", company_id=company_id, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getStoreByBrands(self, company_id=None, page_no=None, page_size=None, body=""):
        """Get stores by brand uids
        :param company_id : Current company id : type string
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ConfigurationValidator.getStoreByBrands()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.StoreByBrandsRequest import StoreByBrandsRequest
        schema = StoreByBrandsRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/inventory/stores-by-brands", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"headers":[]}""", company_id=company_id, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(company_id=company_id, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/inventory/stores-by-brands", company_id=company_id, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getOtherSellerApplications(self, company_id=None, page_no=None, page_size=None, body=""):
        """Get other seller applications who has opted current company as inventory
        :param company_id : Current company id : type string
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ConfigurationValidator.getOtherSellerApplications()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/other-seller-applications/", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"}],"headers":[]}""", company_id=company_id, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(company_id=company_id, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/other-seller-applications/", company_id=company_id, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getOtherSellerApplicationById(self, company_id=None, id=None, body=""):
        """Get other seller application
        :param company_id : Current company id : type string
        :param id : Application Id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ConfigurationValidator.getOtherSellerApplicationById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/other-seller-applications/{id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Application Id","required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, id=id)
        query_string = await create_query_string(company_id=company_id, id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/other-seller-applications/{id}", company_id=company_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def optOutFromApplication(self, company_id=None, id=None, body=""):
        """Opt out company or store from other seller application
        :param company_id : Current company id : type string
        :param id : Application Id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = ConfigurationValidator.optOutFromApplication()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.OptOutInventory import OptOutInventory
        schema = OptOutInventory()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/configuration/v1.0/company/{company_id}/other-seller-applications/{id}/opt_out", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Application Id","required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, id=id)
        query_string = await create_query_string(company_id=company_id, id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/configuration/v1.0/company/{company_id}/other-seller-applications/{id}/opt_out", company_id=company_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    

class Cart:
    def __init__(self, config):
        self._conf = config
    # async def ():
    
    async def getCoupons(self, company_id=None, application_id=None, page_no=None, page_size=None, is_archived=None, title=None, is_public=None, is_display=None, type_slug=None, code=None, body=""):
        """Get coupon list with pagination
        :param company_id : Current company id : type string
        :param application_id : Current Application _id : type string
        :param page_no :  : type integer
        :param page_size :  : type integer
        :param is_archived :  : type boolean
        :param title :  : type string
        :param is_public :  : type boolean
        :param is_display :  : type boolean
        :param type_slug :  : type string
        :param code :  : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if is_archived:
            payload["is_archived"] = is_archived
        
        if title:
            payload["title"] = title
        
        if is_public:
            payload["is_public"] = is_public
        
        if is_display:
            payload["is_display"] = is_display
        
        if type_slug:
            payload["type_slug"] = type_slug
        
        if code:
            payload["code"] = code
        

        # Parameter validation
        schema = CartValidator.getCoupons()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/cart/v1.0/company/{company_id}/application/{application_id}/coupon", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer","default":0,"description":"current page no as per pagination"}},{"name":"page_size","in":"query","schema":{"type":"integer","default":10,"description":"Coupon max records fetched in single request"}},{"name":"is_archived","in":"query","schema":{"type":"boolean","description":"Filter by active or inactive coupon","default":false}},{"name":"title","in":"query","schema":{"type":"string","description":"Filter by `title`"}},{"name":"is_public","in":"query","schema":{"type":"boolean","description":"Filter by `is_public`"}},{"name":"is_display","in":"query","schema":{"type":"boolean","description":"Filter by `is_display`"}},{"name":"type_slug","in":"query","schema":{"type":"string","description":"Filter by coupon type"}},{"name":"code","in":"query","schema":{"type":"string","description":"Filter by `code`"}}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer","default":0,"description":"current page no as per pagination"}},{"name":"page_size","in":"query","schema":{"type":"integer","default":10,"description":"Coupon max records fetched in single request"}},{"name":"is_archived","in":"query","schema":{"type":"boolean","description":"Filter by active or inactive coupon","default":false}},{"name":"title","in":"query","schema":{"type":"string","description":"Filter by `title`"}},{"name":"is_public","in":"query","schema":{"type":"boolean","description":"Filter by `is_public`"}},{"name":"is_display","in":"query","schema":{"type":"boolean","description":"Filter by `is_display`"}},{"name":"type_slug","in":"query","schema":{"type":"string","description":"Filter by coupon type"}},{"name":"code","in":"query","schema":{"type":"string","description":"Filter by `code`"}}],"headers":[]}""", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, is_archived=is_archived, title=title, is_public=is_public, is_display=is_display, type_slug=type_slug, code=code)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, is_archived=is_archived, title=title, is_public=is_public, is_display=is_display, type_slug=type_slug, code=code)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/cart/v1.0/company/{company_id}/application/{application_id}/coupon", company_id=company_id, application_id=application_id, page_no=page_no, page_size=page_size, is_archived=is_archived, title=title, is_public=is_public, is_display=is_display, type_slug=type_slug, code=code), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createCoupon(self, company_id=None, application_id=None, body=""):
        """Create new coupon
        :param company_id : Current company id : type string
        :param application_id : Current Application _id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = CartValidator.createCoupon()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.CouponAdd import CouponAdd
        schema = CouponAdd()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/cart/v1.0/company/{company_id}/application/{application_id}/coupon", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/cart/v1.0/company/{company_id}/application/{application_id}/coupon", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getCouponById(self, company_id=None, application_id=None, id=None, body=""):
        """Get single coupon details with `id` in path param
        :param company_id : Current company id : type string
        :param application_id : Current Application _id : type string
        :param id :  : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CartValidator.getCouponById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/cart/v1.0/company/{company_id}/application/{application_id}/coupon/{id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","required":true,"schema":{"type":"string","description":"Coupon mongo _id for fetching single coupon data for editing"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/cart/v1.0/company/{company_id}/application/{application_id}/coupon/{id}", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateCoupon(self, company_id=None, application_id=None, id=None, body=""):
        """Update coupon with id sent in `id`
        :param company_id : Current company id : type string
        :param application_id : Current Application _id : type string
        :param id :  : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CartValidator.updateCoupon()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.CouponUpdate import CouponUpdate
        schema = CouponUpdate()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/cart/v1.0/company/{company_id}/application/{application_id}/coupon/{id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","schema":{"type":"string","description":"Coupon mongo _id for fetching single coupon data for editing"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/cart/v1.0/company/{company_id}/application/{application_id}/coupon/{id}", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateCouponPartially(self, company_id=None, application_id=None, id=None, body=""):
        """Update archive/unarchive and change schedule for coupon
        :param company_id : Current company id : type string
        :param application_id : Current Application _id : type string
        :param id :  : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CartValidator.updateCouponPartially()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.CouponPartialUpdate import CouponPartialUpdate
        schema = CouponPartialUpdate()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/cart/v1.0/company/{company_id}/application/{application_id}/coupon/{id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","schema":{"type":"string","description":"Coupon mongo _id for fetching single coupon data for editing"},"required":true}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain("/service/platform/cart/v1.0/company/{company_id}/application/{application_id}/coupon/{id}", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def fetchAndvalidateCartItems(self, company_id=None, application_id=None, body=""):
        """Get all the details of cart for a list of provided `cart_items`
        :param company_id : Current company id : type string
        :param application_id : Current Application _id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = CartValidator.fetchAndvalidateCartItems()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.OpenapiCartDetailsRequest import OpenapiCartDetailsRequest
        schema = OpenapiCartDetailsRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/cart/v1.0/company/{company_id}/application/{application_id}/cart/validate", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/cart/v1.0/company/{company_id}/application/{application_id}/cart/validate", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def checkCartServiceability(self, company_id=None, application_id=None, body=""):
        """Check Pincode serviceability for cart items provided in `cart_items` and address pincode in `shipping_address`
        :param company_id : Current company id : type string
        :param application_id : Current Application _id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = CartValidator.checkCartServiceability()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.OpenApiCartServiceabilityRequest import OpenApiCartServiceabilityRequest
        schema = OpenApiCartServiceabilityRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/cart/v1.0/company/{company_id}/application/{application_id}/cart/serviceability", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/cart/v1.0/company/{company_id}/application/{application_id}/cart/serviceability", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def checkoutCart(self, company_id=None, application_id=None, body=""):
        """Generate Fynd order for cart details send with provided `cart_items`
        :param company_id : Current company id : type string
        :param application_id : Current Application _id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = CartValidator.checkoutCart()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.OpenApiPlatformCheckoutReq import OpenApiPlatformCheckoutReq
        schema = OpenApiPlatformCheckoutReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/cart/v1.0/company/{company_id}/application/{application_id}/cart/checkout", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/cart/v1.0/company/{company_id}/application/{application_id}/cart/checkout", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    

class Rewards:
    def __init__(self, config):
        self._conf = config
    # async def ():
    
    async def getGiveaways(self, company_id=None, application_id=None, page_id=None, page_size=None, body=""):
        """List of giveaways of the current application.
        :param company_id : company id : type string
        :param application_id : application id : type string
        :param page_id : pagination page id : type string
        :param page_size : pagination page size : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if page_id:
            payload["page_id"] = page_id
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = RewardsValidator.getGiveaways()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/rewards/v1.0/company/{company_id}/application/{application_id}/giveaways/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"pagination page id","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"pagination page size","in":"query","name":"page_size","schema":{"type":"integer"}}],"query":[{"description":"pagination page id","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"pagination page size","in":"query","name":"page_size","schema":{"type":"integer"}}],"headers":[]}""", company_id=company_id, application_id=application_id, page_id=page_id, page_size=page_size)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, page_id=page_id, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/rewards/v1.0/company/{company_id}/application/{application_id}/giveaways/", company_id=company_id, application_id=application_id, page_id=page_id, page_size=page_size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createGiveaway(self, company_id=None, application_id=None, body=""):
        """Adds a new giveaway.
        :param company_id : company id : type string
        :param application_id : application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = RewardsValidator.createGiveaway()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.Giveaway import Giveaway
        schema = Giveaway()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/rewards/v1.0/company/{company_id}/application/{application_id}/giveaways/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/rewards/v1.0/company/{company_id}/application/{application_id}/giveaways/", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getGiveawayByID(self, company_id=None, application_id=None, id=None, body=""):
        """Get giveaway by ID.
        :param company_id : company id : type string
        :param application_id : application id : type string
        :param id : Giveaway ID : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = RewardsValidator.getGiveawayByID()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/rewards/v1.0/company/{company_id}/application/{application_id}/giveaways/{id}/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Giveaway ID","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/rewards/v1.0/company/{company_id}/application/{application_id}/giveaways/{id}/", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateGiveaway(self, company_id=None, application_id=None, id=None, body=""):
        """Updates the giveaway by it's ID.
        :param company_id : company id : type string
        :param application_id : application id : type string
        :param id : Giveaway ID : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = RewardsValidator.updateGiveaway()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.Giveaway import Giveaway
        schema = Giveaway()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/rewards/v1.0/company/{company_id}/application/{application_id}/giveaways/{id}/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Giveaway ID","in":"path","name":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, id=id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/rewards/v1.0/company/{company_id}/application/{application_id}/giveaways/{id}/", company_id=company_id, application_id=application_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getOffers(self, company_id=None, application_id=None, body=""):
        """List of offer of the current application.
        :param company_id : company id : type string
        :param application_id : application id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = RewardsValidator.getOffers()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/rewards/v1.0/company/{company_id}/application/{application_id}/offers/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/rewards/v1.0/company/{company_id}/application/{application_id}/offers/", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getOfferByName(self, company_id=None, application_id=None, cookie=None, name=None, body=""):
        """Get offer by name.
        :param company_id : company id : type string
        :param application_id : application id : type string
        :param cookie : User's session cookie. This cookie is set in browser cookie when logged-in to fynd's authentication system i.e. `Grimlock` or by using grimlock-backend SDK for backend implementation. : type string
        :param name : Offer name : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if cookie:
            payload["cookie"] = cookie
        
        if name:
            payload["name"] = name
        

        # Parameter validation
        schema = RewardsValidator.getOfferByName()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/rewards/v1.0/company/{company_id}/application/{application_id}/offers/{name}/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"User's session cookie. This cookie is set in browser cookie when logged-in to fynd's authentication system i.e. `Grimlock` or by using grimlock-backend SDK for backend implementation.","in":"header","name":"cookie","required":true,"schema":{"type":"string"}},{"description":"Offer name","in":"path","name":"name","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[{"description":"User's session cookie. This cookie is set in browser cookie when logged-in to fynd's authentication system i.e. `Grimlock` or by using grimlock-backend SDK for backend implementation.","in":"header","name":"cookie","required":true,"schema":{"type":"string"}}]}""", company_id=company_id, application_id=application_id, cookie=cookie, name=name)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, cookie=cookie, name=name)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/rewards/v1.0/company/{company_id}/application/{application_id}/offers/{name}/", company_id=company_id, application_id=application_id, cookie=cookie, name=name), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateOfferByName(self, company_id=None, application_id=None, name=None, body=""):
        """Updates the offer by name.
        :param company_id : company id : type string
        :param application_id : application id : type string
        :param name : Offer name : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if name:
            payload["name"] = name
        

        # Parameter validation
        schema = RewardsValidator.updateOfferByName()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.Offer import Offer
        schema = Offer()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/rewards/v1.0/company/{company_id}/application/{application_id}/offers/{name}/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"Offer name","in":"path","name":"name","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, name=name)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, name=name)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/rewards/v1.0/company/{company_id}/application/{application_id}/offers/{name}/", company_id=company_id, application_id=application_id, name=name), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getUserAvailablePoints(self, company_id=None, application_id=None, user_id=None, body=""):
        """User's reward details.
        :param company_id : company id : type string
        :param application_id : application id : type string
        :param user_id : user id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if user_id:
            payload["user_id"] = user_id
        

        # Parameter validation
        schema = RewardsValidator.getUserAvailablePoints()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/rewards/v1.0/company/{company_id}/application/{application_id}/users/{user_id}/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"user id","in":"path","name":"user_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, user_id=user_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, user_id=user_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/rewards/v1.0/company/{company_id}/application/{application_id}/users/{user_id}/", company_id=company_id, application_id=application_id, user_id=user_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateUserStatus(self, company_id=None, application_id=None, user_id=None, body=""):
        """Update user status, active/archive
        :param company_id : company id : type string
        :param application_id : application id : type string
        :param user_id : user id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if user_id:
            payload["user_id"] = user_id
        

        # Parameter validation
        schema = RewardsValidator.updateUserStatus()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.AppUser import AppUser
        schema = AppUser()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/rewards/v1.0/company/{company_id}/application/{application_id}/users/{user_id}/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"user id","in":"path","name":"user_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, user_id=user_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, user_id=user_id)
        return await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain("/service/platform/rewards/v1.0/company/{company_id}/application/{application_id}/users/{user_id}/", company_id=company_id, application_id=application_id, user_id=user_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getUserPointsHistory(self, company_id=None, application_id=None, user_id=None, page_id=None, page_limit=None, page_size=None, body=""):
        """Get list of points transactions.
The list of points history is paginated.
        :param company_id : company id : type string
        :param application_id : application id : type string
        :param user_id : user id : type string
        :param page_id : PageID is the ID of the requested page. For first request it should be kept empty. : type string
        :param page_limit : PageLimit is the number of requested items in response. : type integer
        :param page_size : PageSize is the number of requested items in response. : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if user_id:
            payload["user_id"] = user_id
        
        if page_id:
            payload["page_id"] = page_id
        
        if page_limit:
            payload["page_limit"] = page_limit
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = RewardsValidator.getUserPointsHistory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/rewards/v1.0/company/{company_id}/application/{application_id}/users/{user_id}/points/history/", """{"required":[{"description":"company id","in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"description":"application id","in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"description":"user id","in":"path","name":"user_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"PageID is the ID of the requested page. For first request it should be kept empty.","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"PageLimit is the number of requested items in response.","in":"query","name":"page_limit","schema":{"type":"integer"}},{"description":"PageSize is the number of requested items in response.","in":"query","name":"page_size","schema":{"type":"integer"}}],"query":[{"description":"PageID is the ID of the requested page. For first request it should be kept empty.","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"PageLimit is the number of requested items in response.","in":"query","name":"page_limit","schema":{"type":"integer"}},{"description":"PageSize is the number of requested items in response.","in":"query","name":"page_size","schema":{"type":"integer"}}],"headers":[]}""", company_id=company_id, application_id=application_id, user_id=user_id, page_id=page_id, page_limit=page_limit, page_size=page_size)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, user_id=user_id, page_id=page_id, page_limit=page_limit, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/rewards/v1.0/company/{company_id}/application/{application_id}/users/{user_id}/points/history/", company_id=company_id, application_id=application_id, user_id=user_id, page_id=page_id, page_limit=page_limit, page_size=page_size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    

class Analytics:
    def __init__(self, config):
        self._conf = config
    # async def ():
    
    async def getStatiscticsGroups(self, company_id=None, application_id=None, body=""):
        """Get statistics groups
        :param company_id : Company Id : type string
        :param application_id : Application Id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        

        # Parameter validation
        schema = AnalyticsValidator.getStatiscticsGroups()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/analytics/v1.0/company/{company_id}/application/{application_id}/stats/group", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/analytics/v1.0/company/{company_id}/application/{application_id}/stats/group", company_id=company_id, application_id=application_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getStatiscticsGroupComponents(self, company_id=None, application_id=None, group_name=None, body=""):
        """Get statistics group components
        :param company_id : Company Id : type string
        :param application_id : Application Id : type string
        :param group_name : Group name : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if group_name:
            payload["group_name"] = group_name
        

        # Parameter validation
        schema = AnalyticsValidator.getStatiscticsGroupComponents()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/analytics/v1.0/company/{company_id}/application/{application_id}/stats/group/{group_name}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"group_name","in":"path","description":"Group name","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, group_name=group_name)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, group_name=group_name)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/analytics/v1.0/company/{company_id}/application/{application_id}/stats/group/{group_name}", company_id=company_id, application_id=application_id, group_name=group_name), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getComponentStatsCSV(self, company_id=None, application_id=None, component_name=None, body=""):
        """Get component statistics csv
        :param company_id : Company Id : type string
        :param application_id : Application Id : type string
        :param component_name : Component name : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if component_name:
            payload["component_name"] = component_name
        

        # Parameter validation
        schema = AnalyticsValidator.getComponentStatsCSV()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/analytics/v1.0/company/{company_id}/application/{application_id}/stats/component/{component_name}.csv", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"component_name","in":"path","description":"Component name","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, component_name=component_name)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, component_name=component_name)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/analytics/v1.0/company/{company_id}/application/{application_id}/stats/component/{component_name}.csv", company_id=company_id, application_id=application_id, component_name=component_name), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getComponentStatsPDF(self, company_id=None, application_id=None, component_name=None, body=""):
        """Get component statistics pdf
        :param company_id : Company Id : type string
        :param application_id : Application Id : type string
        :param component_name : Component name : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if component_name:
            payload["component_name"] = component_name
        

        # Parameter validation
        schema = AnalyticsValidator.getComponentStatsPDF()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/analytics/v1.0/company/{company_id}/application/{application_id}/stats/component/{component_name}.pdf", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"component_name","in":"path","description":"Component name","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, component_name=component_name)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, component_name=component_name)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/analytics/v1.0/company/{company_id}/application/{application_id}/stats/component/{component_name}.pdf", company_id=company_id, application_id=application_id, component_name=component_name), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getComponentStats(self, company_id=None, application_id=None, component_name=None, body=""):
        """Get component statistics
        :param company_id : Company Id : type string
        :param application_id : Application Id : type string
        :param component_name : Component name : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if component_name:
            payload["component_name"] = component_name
        

        # Parameter validation
        schema = AnalyticsValidator.getComponentStats()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/analytics/v1.0/company/{company_id}/application/{application_id}/stats/component/{component_name}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"component_name","in":"path","description":"Component name","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, component_name=component_name)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, component_name=component_name)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/analytics/v1.0/company/{company_id}/application/{application_id}/stats/component/{component_name}", company_id=company_id, application_id=application_id, component_name=component_name), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getAbandonCartList(self, company_id=None, application_id=None, from_date=None, to_date=None, page_no=None, page_size=None, body=""):
        """Get abandon carts list
        :param company_id : Company Id : type string
        :param application_id : Application Id : type string
        :param from_date : From date : type string
        :param to_date : To date : type string
        :param page_no : Current page number : type integer
        :param page_size : Current page size : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if from_date:
            payload["from_date"] = from_date
        
        if to_date:
            payload["to_date"] = to_date
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = AnalyticsValidator.getAbandonCartList()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/analytics/v1.0/company/{company_id}/application/{application_id}/cart/from/{from_date}/to/{to_date}/abandon-cart/", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"from_date","in":"path","description":"From date","required":true,"schema":{"type":"string"}},{"name":"to_date","in":"path","description":"To date","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"integer","default":0}},{"name":"page_size","in":"query","description":"Current page size","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"integer","default":0}},{"name":"page_size","in":"query","description":"Current page size","required":false,"schema":{"type":"integer","default":10}}],"headers":[]}""", company_id=company_id, application_id=application_id, from_date=from_date, to_date=to_date, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, from_date=from_date, to_date=to_date, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/analytics/v1.0/company/{company_id}/application/{application_id}/cart/from/{from_date}/to/{to_date}/abandon-cart/", company_id=company_id, application_id=application_id, from_date=from_date, to_date=to_date, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getAbandonCartsCSV(self, company_id=None, application_id=None, from_date=None, to_date=None, body=""):
        """Get abandon carts csv
        :param company_id : Company Id : type string
        :param application_id : Application Id : type string
        :param from_date : From date : type string
        :param to_date : To date : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if from_date:
            payload["from_date"] = from_date
        
        if to_date:
            payload["to_date"] = to_date
        

        # Parameter validation
        schema = AnalyticsValidator.getAbandonCartsCSV()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/analytics/v1.0/company/{company_id}/application/{application_id}/cart/{from_date}/to/{to_date}/abandon-cart.csv", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"from_date","in":"path","description":"From date","required":true,"schema":{"type":"string"}},{"name":"to_date","in":"path","description":"To date","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, from_date=from_date, to_date=to_date)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, from_date=from_date, to_date=to_date)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/analytics/v1.0/company/{company_id}/application/{application_id}/cart/{from_date}/to/{to_date}/abandon-cart.csv", company_id=company_id, application_id=application_id, from_date=from_date, to_date=to_date), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getAbandonCartDetail(self, company_id=None, application_id=None, cart_id=None, body=""):
        """Get abandon cart details
        :param company_id : Company Id : type string
        :param application_id : Application Id : type string
        :param cart_id : Cart Id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if cart_id:
            payload["cart_id"] = cart_id
        

        # Parameter validation
        schema = AnalyticsValidator.getAbandonCartDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/analytics/v1.0/company/{company_id}/application/{application_id}/cart/abandon-cart/{cart_id}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"cart_id","in":"path","description":"Cart Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, cart_id=cart_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, cart_id=cart_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/analytics/v1.0/company/{company_id}/application/{application_id}/cart/abandon-cart/{cart_id}", company_id=company_id, application_id=application_id, cart_id=cart_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createExportJob(self, company_id=None, export_type=None, body=""):
        """Create data export job in required format
        :param company_id : Company Id : type string
        :param export_type : Export type / format : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if export_type:
            payload["export_type"] = export_type
        

        # Parameter validation
        schema = AnalyticsValidator.createExportJob()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.ExportJobReq import ExportJobReq
        schema = ExportJobReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/analytics/v1.0/company/{company_id}/export/{export_type}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"export_type","in":"path","description":"Export type / format","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, export_type=export_type)
        query_string = await create_query_string(company_id=company_id, export_type=export_type)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/analytics/v1.0/company/{company_id}/export/{export_type}", company_id=company_id, export_type=export_type), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getExportJobStatus(self, company_id=None, export_type=None, job_id=None, body=""):
        """Get data export job status
        :param company_id : Company Id : type string
        :param export_type : Export type / format : type string
        :param job_id : Export job id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if export_type:
            payload["export_type"] = export_type
        
        if job_id:
            payload["job_id"] = job_id
        

        # Parameter validation
        schema = AnalyticsValidator.getExportJobStatus()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/analytics/v1.0/company/{company_id}/export/{export_type}/job/{job_id}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"export_type","in":"path","description":"Export type / format","required":true,"schema":{"type":"string"}},{"name":"job_id","in":"path","description":"Export job id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, export_type=export_type, job_id=job_id)
        query_string = await create_query_string(company_id=company_id, export_type=export_type, job_id=job_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/analytics/v1.0/company/{company_id}/export/{export_type}/job/{job_id}", company_id=company_id, export_type=export_type, job_id=job_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getLogsList(self, company_id=None, log_type=None, page_no=None, page_size=None, body=""):
        """Get logs list
        :param company_id : Company Id : type string
        :param log_type : Log type : type string
        :param page_no : Current page number : type integer
        :param page_size : Current page size : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if log_type:
            payload["log_type"] = log_type
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = AnalyticsValidator.getLogsList()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.GetLogsListReq import GetLogsListReq
        schema = GetLogsListReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/analytics/v1.0/company/{company_id}/logs/{log_type}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"log_type","in":"path","description":"Log type","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"integer","default":0}},{"name":"page_size","in":"query","description":"Current page size","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"integer","default":0}},{"name":"page_size","in":"query","description":"Current page size","required":false,"schema":{"type":"integer","default":10}}],"headers":[]}""", company_id=company_id, log_type=log_type, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(company_id=company_id, log_type=log_type, page_no=page_no, page_size=page_size)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/analytics/v1.0/company/{company_id}/logs/{log_type}", company_id=company_id, log_type=log_type, page_no=page_no, page_size=page_size), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def searchLogs(self, company_id=None, page_no=None, page_size=None, log_type=None, body=""):
        """Search logs
        :param company_id : Company Id : type string
        :param page_no : Current page number : type integer
        :param page_size : Current page size : type integer
        :param log_type : Log type : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if log_type:
            payload["log_type"] = log_type
        

        # Parameter validation
        schema = AnalyticsValidator.searchLogs()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.SearchLogReq import SearchLogReq
        schema = SearchLogReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/analytics/v1.0/company/{company_id}/logs/{log_type}/search", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"log_type","in":"path","description":"Log type","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"integer","default":0}},{"name":"page_size","in":"query","description":"Current page size","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"integer","default":0}},{"name":"page_size","in":"query","description":"Current page size","required":false,"schema":{"type":"integer","default":10}}],"headers":[]}""", company_id=company_id, page_no=page_no, page_size=page_size, log_type=log_type)
        query_string = await create_query_string(company_id=company_id, page_no=page_no, page_size=page_size, log_type=log_type)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/analytics/v1.0/company/{company_id}/logs/{log_type}/search", company_id=company_id, page_no=page_no, page_size=page_size, log_type=log_type), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    

class Discount:
    def __init__(self, config):
        self._conf = config
    # async def ():
    
    async def getDiscounts(self, company_id=None, view=None, q=None, page_no=None, page_size=None, archived=None, month=None, year=None, type=None, app_ids=None, body=""):
        """Fetch discount list.
        :param company_id : company_id : type integer
        :param view : listing or calender.  Default is listing. : type string
        :param q : The search query. This can be a partial or complete name of a discount. : type string
        :param page_no : page number. Default is 1. : type integer
        :param page_size : page size. Default is 12. : type integer
        :param archived : archived. Default is false. : type boolean
        :param month : month. Default is current month. : type integer
        :param year : year. Default is current year. : type integer
        :param type : basic or custom. : type string
        :param app_ids : application ids. : type array
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if view:
            payload["view"] = view
        
        if q:
            payload["q"] = q
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if archived:
            payload["archived"] = archived
        
        if month:
            payload["month"] = month
        
        if year:
            payload["year"] = year
        
        if type:
            payload["type"] = type
        
        if app_ids:
            payload["app_ids"] = app_ids
        

        # Parameter validation
        schema = DiscountValidator.getDiscounts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/discount/v1.0/company/{company_id}/job/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"name":"view","in":"query","description":"listing or calender.  Default is listing.","required":false,"schema":{"type":"string","enum":["listing","calender"]}},{"name":"q","in":"query","description":"The search query. This can be a partial or complete name of a discount.","required":false,"schema":{"type":"string"}},{"name":"page_no","in":"query","description":"page number. Default is 1.","required":false,"schema":{"type":"integer"}},{"name":"page_size","in":"query","description":"page size. Default is 12.","required":false,"schema":{"type":"integer"}},{"name":"archived","in":"query","description":"archived. Default is false.","required":false,"schema":{"type":"boolean","enum":[true,false]}},{"name":"month","in":"query","description":"month. Default is current month.","required":false,"schema":{"type":"integer"}},{"name":"year","in":"query","description":"year. Default is current year.","required":false,"schema":{"type":"integer"}},{"name":"type","in":"query","description":"basic or custom.","required":false,"schema":{"type":"string"}},{"name":"app_ids","in":"query","description":"application ids.","required":false,"schema":{"type":"array","items":{"type":"string"}}}],"query":[{"name":"view","in":"query","description":"listing or calender.  Default is listing.","required":false,"schema":{"type":"string","enum":["listing","calender"]}},{"name":"q","in":"query","description":"The search query. This can be a partial or complete name of a discount.","required":false,"schema":{"type":"string"}},{"name":"page_no","in":"query","description":"page number. Default is 1.","required":false,"schema":{"type":"integer"}},{"name":"page_size","in":"query","description":"page size. Default is 12.","required":false,"schema":{"type":"integer"}},{"name":"archived","in":"query","description":"archived. Default is false.","required":false,"schema":{"type":"boolean","enum":[true,false]}},{"name":"month","in":"query","description":"month. Default is current month.","required":false,"schema":{"type":"integer"}},{"name":"year","in":"query","description":"year. Default is current year.","required":false,"schema":{"type":"integer"}},{"name":"type","in":"query","description":"basic or custom.","required":false,"schema":{"type":"string"}},{"name":"app_ids","in":"query","description":"application ids.","required":false,"schema":{"type":"array","items":{"type":"string"}}}],"headers":[]}""", company_id=company_id, view=view, q=q, page_no=page_no, page_size=page_size, archived=archived, month=month, year=year, type=type, app_ids=app_ids)
        query_string = await create_query_string(company_id=company_id, view=view, q=q, page_no=page_no, page_size=page_size, archived=archived, month=month, year=year, type=type, app_ids=app_ids)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/discount/v1.0/company/{company_id}/job/", company_id=company_id, view=view, q=q, page_no=page_no, page_size=page_size, archived=archived, month=month, year=year, type=type, app_ids=app_ids), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def createDiscount(self, company_id=None, body=""):
        """Create Discount.
        :param company_id : company_id : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = DiscountValidator.createDiscount()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.CreateUpdateDiscount import CreateUpdateDiscount
        schema = CreateUpdateDiscount()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/discount/v1.0/company/{company_id}/job/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/discount/v1.0/company/{company_id}/job/", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getDiscount(self, company_id=None, id=None, body=""):
        """Fetch discount.
        :param company_id : company_id : type integer
        :param id : unique id. : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = DiscountValidator.getDiscount()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/discount/v1.0/company/{company_id}/job/{id}/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"unique id.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, id=id)
        query_string = await create_query_string(company_id=company_id, id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/discount/v1.0/company/{company_id}/job/{id}/", company_id=company_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateDiscount(self, company_id=None, id=None, body=""):
        """Create Discount.
        :param company_id : company_id : type integer
        :param id : id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = DiscountValidator.updateDiscount()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.CreateUpdateDiscount import CreateUpdateDiscount
        schema = CreateUpdateDiscount()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/discount/v1.0/company/{company_id}/job/{id}/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, id=id)
        query_string = await create_query_string(company_id=company_id, id=id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/discount/v1.0/company/{company_id}/job/{id}/", company_id=company_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def validateDiscountFile(self, company_id=None, discount=None, body=""):
        """Validate File.
        :param company_id : company_id : type integer
        :param discount : discount : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if discount:
            payload["discount"] = discount
        

        # Parameter validation
        schema = DiscountValidator.validateDiscountFile()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.DiscountJob import DiscountJob
        schema = DiscountJob()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/discount/v1.0/company/{company_id}/file/validation/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"name":"discount","in":"query","description":"discount","required":false,"schema":{"type":"string"}}],"query":[{"name":"discount","in":"query","description":"discount","required":false,"schema":{"type":"string"}}],"headers":[]}""", company_id=company_id, discount=discount)
        query_string = await create_query_string(company_id=company_id, discount=discount)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/discount/v1.0/company/{company_id}/file/validation/", company_id=company_id, discount=discount), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def downloadDiscountFile(self, company_id=None, type=None, body=""):
        """Validate File.
        :param company_id : company_id : type integer
        :param type : type : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if type:
            payload["type"] = type
        

        # Parameter validation
        schema = DiscountValidator.downloadDiscountFile()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.DownloadFileJob import DownloadFileJob
        schema = DownloadFileJob()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/discount/v1.0/company/{company_id}/file/{type}/download/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"type","in":"path","description":"type","required":true,"schema":{"type":"string","enum":["product","inventory"]}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, type=type)
        query_string = await create_query_string(company_id=company_id, type=type)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/discount/v1.0/company/{company_id}/file/{type}/download/", company_id=company_id, type=type), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getValidationJob(self, company_id=None, id=None, body=""):
        """Validate File Job.
        :param company_id : company_id : type integer
        :param id : id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = DiscountValidator.getValidationJob()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/discount/v1.0/company/{company_id}/file/validation/{id}/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, id=id)
        query_string = await create_query_string(company_id=company_id, id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/discount/v1.0/company/{company_id}/file/validation/{id}/", company_id=company_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def cancelValidationJob(self, company_id=None, id=None, body=""):
        """Cancel Validation Job.
        :param company_id : company_id : type integer
        :param id : id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = DiscountValidator.cancelValidationJob()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/discount/v1.0/company/{company_id}/file/validation/{id}/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, id=id)
        query_string = await create_query_string(company_id=company_id, id=id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain("/service/platform/discount/v1.0/company/{company_id}/file/validation/{id}/", company_id=company_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getDownloadJob(self, company_id=None, id=None, body=""):
        """Download File Job.
        :param company_id : company_id : type integer
        :param id : id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = DiscountValidator.getDownloadJob()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/discount/v1.0/company/{company_id}/file/download/{id}/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, id=id)
        query_string = await create_query_string(company_id=company_id, id=id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/discount/v1.0/company/{company_id}/file/download/{id}/", company_id=company_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def cancelDownloadJob(self, company_id=None, id=None, body=""):
        """Cancel Download Job.
        :param company_id : company_id : type integer
        :param id : id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = DiscountValidator.cancelDownloadJob()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/discount/v1.0/company/{company_id}/file/download/{id}/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, id=id)
        query_string = await create_query_string(company_id=company_id, id=id)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain("/service/platform/discount/v1.0/company/{company_id}/file/download/{id}/", company_id=company_id, id=id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    

class Partner:
    def __init__(self, config):
        self._conf = config
    # async def ():
    
    async def addProxyPath(self, company_id=None, application_id=None, extension_id=None, body=""):
        """Add proxy path for external url
        :param company_id : Current company id : type string
        :param application_id : Current application id : type string
        :param extension_id : Extension id : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if extension_id:
            payload["extension_id"] = extension_id
        

        # Parameter validation
        schema = PartnerValidator.addProxyPath()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.AddProxyReq import AddProxyReq
        schema = AddProxyReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/partners/v1.0/company/{company_id}/application/{application_id}/proxy/{extension_id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"},{"name":"extension_id","in":"path","description":"Extension id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, extension_id=extension_id)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, extension_id=extension_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/partners/v1.0/company/{company_id}/application/{application_id}/proxy/{extension_id}", company_id=company_id, application_id=application_id, extension_id=extension_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def removeProxyPath(self, company_id=None, application_id=None, extension_id=None, attached_path=None, body=""):
        """Remove proxy path for external url
        :param company_id : Current company id : type string
        :param application_id : Current application id : type string
        :param extension_id : Extension id : type string
        :param attached_path : Attachaed path slug : type string
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if application_id:
            payload["application_id"] = application_id
        
        if extension_id:
            payload["extension_id"] = extension_id
        
        if attached_path:
            payload["attached_path"] = attached_path
        

        # Parameter validation
        schema = PartnerValidator.removeProxyPath()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/partners/v1.0/company/{company_id}/application/{application_id}/proxy/{extension_id}/{attached_path}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current application id","in":"path","required":true,"name":"application_id"},{"name":"extension_id","in":"path","description":"Extension id","required":true,"schema":{"type":"string"}},{"name":"attached_path","in":"path","description":"Attachaed path slug","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, application_id=application_id, extension_id=extension_id, attached_path=attached_path)
        query_string = await create_query_string(company_id=company_id, application_id=application_id, extension_id=extension_id, attached_path=attached_path)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain("/service/platform/partners/v1.0/company/{company_id}/application/{application_id}/proxy/{extension_id}/{attached_path}", company_id=company_id, application_id=application_id, extension_id=extension_id, attached_path=attached_path), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    

class Webhook:
    def __init__(self, config):
        self._conf = config
    # async def ():
    
    async def getSubscribersByCompany(self, page_no=None, page_size=None, company_id=None, extension_id=None, body=""):
        """Get Subscribers By CompanyId
        :param page_no : Page Number : type integer
        :param page_size : Page Size : type integer
        :param company_id : Company ID of the application : type integer
        :param extension_id : Extension ID : type string
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if company_id:
            payload["company_id"] = company_id
        
        if extension_id:
            payload["extension_id"] = extension_id
        

        # Parameter validation
        schema = WebhookValidator.getSubscribersByCompany()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/webhook/v1.0/company/{company_id}/subscriber", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"integer","format":"int32"}}],"optional":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer","format":"int32","default":1}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32","default":10}},{"name":"extension_id","in":"query","description":"Extension ID","required":false,"schema":{"type":"string"}}],"query":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer","format":"int32","default":1}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32","default":10}},{"name":"extension_id","in":"query","description":"Extension ID","required":false,"schema":{"type":"string"}}],"headers":[]}""", page_no=page_no, page_size=page_size, company_id=company_id, extension_id=extension_id)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, company_id=company_id, extension_id=extension_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/webhook/v1.0/company/{company_id}/subscriber", page_no=page_no, page_size=page_size, company_id=company_id, extension_id=extension_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def registerSubscriberToEvent(self, company_id=None, body=""):
        """Register Subscriber
        :param company_id : Company Id of the application : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = WebhookValidator.registerSubscriberToEvent()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.SubscriberConfig import SubscriberConfig
        schema = SubscriberConfig()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/webhook/v1.0/company/{company_id}/subscriber", """{"required":[{"name":"company_id","in":"path","description":"Company Id of the application","required":true,"schema":{"type":"integer","format":"int32"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain("/service/platform/webhook/v1.0/company/{company_id}/subscriber", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def updateSubscriberConfig(self, company_id=None, body=""):
        """Update Subscriber
        :param company_id : Company ID of the application : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = WebhookValidator.updateSubscriberConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .platform_models.SubscriberConfig import SubscriberConfig
        schema = SubscriberConfig()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/webhook/v1.0/company/{company_id}/subscriber", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"integer","format":"int32"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain("/service/platform/webhook/v1.0/company/{company_id}/subscriber", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getSubscribersByExtensionId(self, page_no=None, page_size=None, company_id=None, extension_id=None, body=""):
        """Get Subscribers By ExtensionID
        :param page_no : Page Number : type integer
        :param page_size : Page Size : type integer
        :param company_id : Company ID of the application : type integer
        :param extension_id : Extension ID : type string
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if company_id:
            payload["company_id"] = company_id
        
        if extension_id:
            payload["extension_id"] = extension_id
        

        # Parameter validation
        schema = WebhookValidator.getSubscribersByExtensionId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/webhook/v1.0/company/{company_id}/extension/{extension_id}/subscriber", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"extension_id","in":"path","description":"Extension ID","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer","format":"int32","default":1}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32","default":10}}],"query":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer","format":"int32","default":1}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32","default":10}}],"headers":[]}""", page_no=page_no, page_size=page_size, company_id=company_id, extension_id=extension_id)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, company_id=company_id, extension_id=extension_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/webhook/v1.0/company/{company_id}/extension/{extension_id}/subscriber", page_no=page_no, page_size=page_size, company_id=company_id, extension_id=extension_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def getSubscriberById(self, company_id=None, subscriber_id=None, body=""):
        """Get Subscriber By Subscriber ID
        :param company_id : Company ID of the application : type integer
        :param subscriber_id : Subscriber ID : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        
        if subscriber_id:
            payload["subscriber_id"] = subscriber_id
        

        # Parameter validation
        schema = WebhookValidator.getSubscriberById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/webhook/v1.0/company/{company_id}/subscriber/{subscriber_id}", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"integer","format":"int32"}},{"name":"subscriber_id","in":"path","description":"Subscriber ID","required":true,"schema":{"type":"integer","format":"int32"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id, subscriber_id=subscriber_id)
        query_string = await create_query_string(company_id=company_id, subscriber_id=subscriber_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/webhook/v1.0/company/{company_id}/subscriber/{subscriber_id}", company_id=company_id, subscriber_id=subscriber_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    
    async def fetchAllEventConfigurations(self, company_id=None, body=""):
        """Get All Webhook Events
        :param company_id : Company ID of the application : type integer
        """
        payload = {}
        
        if company_id:
            payload["company_id"] = company_id
        

        # Parameter validation
        schema = WebhookValidator.fetchAllEventConfigurations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, "/service/platform/webhook/v1.0/company/{company_id}/events", """{"required":[{"name":"company_id","in":"path","description":"Company ID of the application","required":true,"schema":{"type":"integer","format":"int32"}}],"optional":[],"query":[],"headers":[]}""", company_id=company_id)
        query_string = await create_query_string(company_id=company_id)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain("/service/platform/webhook/v1.0/company/{company_id}/events", company_id=company_id), query_string, {"Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.apiKey, self._conf.apiSecret).encode()).decode()}, body), data=body)
    



class PlatformClient:
    def __init__(self, config):
        self._conf = config
        self.common = Common(config)
        self.lead = Lead(config)
        self.feedback = Feedback(config)
        self.theme = Theme(config)
        self.user = User(config)
        self.content = Content(config)
        self.billing = Billing(config)
        self.communication = Communication(config)
        self.payment = Payment(config)
        self.order = Order(config)
        self.catalog = Catalog(config)
        self.companyProfile = CompanyProfile(config)
        self.fileStorage = FileStorage(config)
        self.share = Share(config)
        self.inventory = Inventory(config)
        self.configuration = Configuration(config)
        self.cart = Cart(config)
        self.rewards = Rewards(config)
        self.analytics = Analytics(config)
        self.discount = Discount(config)
        self.partner = Partner(config)
        self.webhook = Webhook(config)
        

    def application(self, applicationId):
        return PlatformApplicationClient(applicationId, self._conf)
