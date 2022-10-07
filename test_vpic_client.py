import pytest
import vpic_client

def test_get_vin_record():
    assert vpic_client.get_vin_record("1FUJGLDR3HLHG7532") == 'FREIGHTLINER'

