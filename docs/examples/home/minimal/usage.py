# init client settings
settings = Settings(protocol="http", host="127.0.0.1", api_path="api/v1", port=8000)

# init client instance
client = FooClient(settings=settings)

# make get_data request
data_response = client.service.get_data(pk=1, q=True)
# extract data from response
data = get_res(data_response)
# Data(pk=1, q=True, nested=ShortData(pk=1, q=True))

# make get_short_data request
short_data_response = client.service.get_short_data(pk=1, q=True)
# extract data from response
short_data = get_res(short_data_response)
# ShortData(pk=1, q=True)
