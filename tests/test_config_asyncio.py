import pytest
from diematic_client import DiematicBoilerClient
from diematic_client import Boiler

@pytest.mark.asyncio
async def test_get_config():
	client = DiematicBoilerClient("polo.chiton")
	config = await client.config()
	assert isinstance(config, list)


@pytest.mark.asyncio
async def test_get_boiler():
	client = DiematicBoilerClient("polo.chiton")
	boiler = await client.boiler()
	assert isinstance(boiler, Boiler)

@pytest.mark.asyncio
async def test_get_config():
	client = DiematicBoilerClient("polo.chiton")
	config = await client.config()
	assert isinstance(config, list)
