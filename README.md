# FDK Python

![GitHub requirements.txt version](https://img.shields.io/github/package-json/v/gofynd/fdk-client-python?style=plastic)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/gofynd/fdk-client-python?style=plastic)
![GitHub](https://img.shields.io/github/license/gofynd/fdk-client-python?style=plastic)
[![Coverage Status](https://coveralls.io/repos/github/gofynd/fdk-client-python/badge.svg)](https://coveralls.io/github/gofynd/fdk-client-python)

FDK client for python

## Getting Started

Get started with the python Development SDK for Fynd Platform

### Usage

```
pip install fdk-client-python
```

Using this method, you can `import` fdk-client-python like so:

```python
from fdk-client-python.application.ApplicationClient import ApplicationClient
from fdk-client-python.application.ApplicationConfig import ApplicationConfig
```

### Sample Usage - ApplicationClient

```python
config = ApplicationConfig({
    "applicationID": "YOUR_APPLICATION_ID",
    "applicationToken": "YOUR_APPLICATION_TOKEN",
    "domain": "YOUR_DOMAIN"
})

applicationClient = ApplicationClient(config)

async def getProductDetails():
    try:
        product = await applicationClient.catalog.getProductDetailBySlug(slug="product-slug")
        print(product)
    except Exception as e:
        print(e)

getProductDetails()
```