# Web SDK

<img src="resources/brand.svg" width="100%" alt="Brand image" />

<p align="center">

<a href="https://github.com/extralait-web/web-sdk/actions?query=event%3Apush+branch%3Amaster+workflow%3ACI" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/extralait-web/web-sdk/ci.yml?branch=master&logo=github&label=CI" alt="CI">
</a>
<a href="https://coverage-badge.samuelcolvin.workers.dev/redirect/extralait-web/web-sdk" target="_blank">
    <img src="https://coverage-badge.samuelcolvin.workers.dev/extralait-web/web-sdk.svg" alt="Coverage">
</a>
<a href="https://pypi.python.org/pypi/web-sdk" target="_blank">
    <img src="https://img.shields.io/pypi/v/web-sdk.svg" alt="pypi">
</a>
<a href="https://pepy.tech/project/web-sdk" target="_blank">
    <img src="https://static.pepy.tech/badge/web-sdk/month" alt="downloads">
</a>
<a href="https://github.com/extralait-web/web-sdk" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/web-sdk.svg" alt="versions">
</a>
<a href="https://github.com/extralait-web/web-sdk" target="_blank">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/extralait-web/web-sdk/master/docs/badge/alfa.json" alt="Web SDK alfa">
</a>

</p>

WebSDK is a library for quickly and easily creating SDKs for integration with third-party APIs.

## Minimal example

Let's imagine that we have the following data schemas
```py linenums="1" title="dtos.py""
--8<-- "home/minimal/dtos.py"
```

To make the example simpler, we'll write the server part using [fastapi](https://fastapi.tiangolo.com/).
```py linenums="1" title="server.py""
--8<-- "home/minimal/server.py"
```


To link with the routes declare in server code, you only need the following client code
```py linenums="1" title="client.py""
--8<-- "home/minimal/client.py"
```

All you have to do next is init the client and call methods you need.
```py linenums="1" title="usage.py""
--8<-- "home/minimal/usage.py"
```

## Features
- [x] Annotation like request parts mapper
- [x] All requests methods support
- [x] Pydantic validation output and input data
- [x] File sending
- [x] Custom extra and context data during request
- [x] Errors logging
- [x] Custom client settings
- [x] Custom and token auth
- [x] Test mode settings support
- [x] Requests REST support
    * [x] Service declaration base request configuring
    * [x] Method declaration base request configuring
    * [x] Method call base request configuring
    * [x] Request call base request configuring
    * [ ] Path part mapping without field annotation
- [x] Requests SOAP support
    * [x] Custom transport for file sending
    * [ ] Service declaration base request configuring
    * [ ] Method declaration base request configuring
    * [ ] Method call base request configuring
    * [ ] Request call base request configuring
- [ ] HTTPX REST support
- [ ] HTTPX SOAP support
- [ ] MkDocs documentation
