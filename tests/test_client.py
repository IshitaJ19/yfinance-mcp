from fastmcp import Client
import pytest

@pytest.mark.asyncio
async def test_client_connection():
    async with Client("http://127.0.0.1:8000/mcp") as client:
        assert client.is_connected()