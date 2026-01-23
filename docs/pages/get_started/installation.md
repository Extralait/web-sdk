## Common installation

### REST installation

=== "pip"
    ```sh
    pip install web-sdk[rest]
    # or if you want use 'web_sdk.sdks.rest.XmlResponse'
    pip install web-sdk[rest,xml]
    ```
=== "uv"
    ```sh
    uv add web-sdk[rest]
    # or if you want use 'web_sdk.sdks.rest.XmlResponse'
    uv add web-sdk[rest,xml]
    ```
=== "poetry"
    ```sh
    poetry add web-sdk[rest]
    # or if you want use 'web_sdk.sdks.rest.XmlResponse'
    poetry add web-sdk[rest,xml]
    ```
=== "pdm"
    ```sh
    pdm add web-sdk[rest]
    # or if you want use 'web_sdk.sdks.rest.XmlResponse'
    pdm add web-sdk[rest,xml]
    ```

### SOAP installation

=== "pip"
    ```sh
    pip install web-sdk[soap]
    ```
=== "uv"
    ```sh
    uv add web-sdk[soap]
    ```
=== "poetry"
    ```sh
    poetry add web-sdk[soap]
    ```
=== "pdm"
    ```sh
    pdm add web-sdk[soap]
    ```

## Install from repository

### REST installation

=== "pip"
    ```sh
    pip install 'git+https://github.com/extralait-web/web-sdk@master#egg=web-sdk[rest]'
    # or if you want use 'web_sdk.sdks.rest.XmlResponse'
    pip install 'git+https://github.com/extralait-web/web-sdk@master#egg=web-sdk[rest,xml]'
    ```
=== "uv"
    ```sh
    uv add 'git+https://github.com/extralait-web/web-sdk@master#egg=web-sdk[rest]'
    # or if you want use 'web_sdk.sdks.rest.XmlResponse'
    uv add 'git+https://github.com/extralait-web/web-sdk@master#egg=web-sdk[rest,xml]'
    ```
=== "poetry"
    ```sh
    poetry add 'git+https://github.com/extralait-web/web-sdk@master#egg=web-sdk[rest]'
    # or if you want use 'web_sdk.sdks.rest.XmlResponse'
    poetry add 'git+https://github.com/extralait-web/web-sdk@master#egg=web-sdk[rest,xml]'
    ```
=== "pdm"
    ```sh
    pdm add 'git+https://github.com/extralait-web/web-sdk@master#egg=web-sdk[rest]'
    # or if you want use 'web_sdk.sdks.rest.XmlResponse'
    pdm add 'git+https://github.com/extralait-web/web-sdk@master#egg=web-sdk[rest,xml]'
    ```

### SOAP installation

=== "pip"
    ```sh
    pip install 'git+https://github.com/extralait-web/web-sdk@master#egg=pydantic[soap]'
    ```
=== "uv"
    ```sh
    uv add 'git+https://github.com/extralait-web/web-sdk@master#egg=pydantic[soap]'
    ```
=== "poetry"
    ```sh
    poetry add 'git+https://github.com/extralait-web/web-sdk@master#egg=pydantic[soap]'
    ```
=== "pdm"
    ```sh
    pdm add 'git+https://github.com/extralait-web/web-sdk@master#egg=pydantic[soap]'
    ```
