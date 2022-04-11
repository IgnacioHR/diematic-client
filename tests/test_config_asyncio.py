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

@pytest.mark.asyncio
async def test_set_value():
	client = DiematicBoilerClient("polo.chiton")
	config = await client.update_boiler_register('temp_dia_b', 16)
	assert isinstance(config, str)

@pytest.mark.asyncio
async def test_set_value():
	client = DiematicBoilerClient("polo.chiton")
	config = await client.read_boiler_register('temp_dia_b')
	assert isinstance(config, dict)
