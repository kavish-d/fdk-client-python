"""Python utils."""

import hashlib
import hmac
import json
from typing import Dict, Text
from urllib import parse
from datetime import datetime
from .exceptions import RequiredParametersError


async def validate_required_query_params(proccessed_params: Dict, params: Dict):
    """Checks if required params are present or not."""
    for r_param in proccessed_params["required"]:
        if r_param["name"] not in params:
            raise RequiredParametersError(message="{} missing".format(r_param["name"]))


async def create_url_with_params(domain: Text, url: Text, proccessed_params: Text, **kwargs):
    """Creates url with params"""
    params = {}
    final_url = domain + url
    for key, value in kwargs.items():
        new_key = key.replace("_", "-")
        params[new_key] = value
        if new_key in final_url:
            final_url.replace(new_key, key)
    await validate_required_query_params(json.loads(proccessed_params), params)
    final_url = final_url.format(**params)
    query_string = parse.urlencode(params)
    if query_string:
        final_url += "?" + query_string
    return final_url


async def create_url_without_domain(url: Text, **kwargs):
    """Returns url without domain replacing variables."""
    params = {}
    for key, value in kwargs.items():
        new_key = key.replace("_", "-")
        params[new_key] = value
        if new_key in url:
            url.replace(new_key, key)
    final_url = url.format(**params)
    return final_url


async def create_query_string(**kwargs):
    """Return query string."""
    params = {}
    for key, value in kwargs.items():
        new_key = key.replace("_", "-")
        params[new_key] = value
    query_string = parse.urlencode(params)
    return query_string


async def get_headers_with_signature(domain: Text, method: Text, url: Text, query_string: Text, headers: Dict, body=""):
    """Returns headers with signature."""
    fp_date = datetime.now().strftime("%Y%m%dT%H%M%SZ")
    headers_str = ""
    host = domain.replace("https://", "").replace("http://", "")
    headers["host"] = host
    headers["x-fp-date"] = fp_date
    authorization = headers.pop("Authorization")
    for key, val in headers.items():
        headers_str += f"{key}:{val}\n"
    request_list = [
        method.upper(),
        url,
        query_string,
        headers_str,
        "host;x-fp-date",
        hashlib.sha256(str(body).encode()).hexdigest()
    ]
    request_str = "\n".join(request_list)
    request_str = "\n".join([fp_date, hashlib.sha256(request_str.encode()).hexdigest()])
    signature = "v1.1:" + hmac.new("1234567".encode(), request_str.encode(), hashlib.sha256).hexdigest()
    headers["x-fp-signature"] = signature
    headers["Authorization"] = authorization
    return headers
