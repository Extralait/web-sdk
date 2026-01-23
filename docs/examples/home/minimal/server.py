from fastapi import FastAPI

# Create FastAPI app
app = FastAPI(root_path="/api/v1")


@app.get("/data/{pk}/info")
async def get_data_info(pk: int, q: bool | None = None) -> Data:
    """Return full data info."""
    return Data(pk=pk, q=q, nested=ShortData(pk=pk, q=q))


# route with short data return
@app.get("/data/{pk}/info/short")
async def get_short_data_info(pk: int, q: bool | None = None) -> ShortData:
    """Return short data info."""
    return ShortData(pk=pk, q=q)
