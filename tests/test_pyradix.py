#!/usr/bin/env python

"""Tests for `pyradix` package."""

import pytest

from pyradix import Client

from .dummy_responses import (
    NETWORK_ID_RESPONSE,
    NATIVE_TOKEN_RESPONSE,
    NETWORK_TPS_RESPONSE,
    NETWORK_TPS_DEMAND_RESPONSE,
    TOKEN_BALANCES_RESPONSE,
)


class TestClient:
    @pytest.fixture(autouse=True)
    def setup_case(self):
        self.endpoint = "http://fake-radix/rpc"
        self.client = Client(node_url=self.endpoint)

    def test_network_id(self, requests_mock):
        requests_mock.post(self.endpoint, json=NETWORK_ID_RESPONSE)
        assert self.client.network_id == 17

    def test_network_tps(self, requests_mock):
        requests_mock.post(self.endpoint, json=NETWORK_TPS_RESPONSE)
        assert self.client.network_tps == 10000

    def test_network_tps_demand(self, requests_mock):
        requests_mock.post(self.endpoint, json=NETWORK_TPS_DEMAND_RESPONSE)
        assert self.client.network_tps_demand == 100000

    def test_native_token(self, requests_mock):
        requests_mock.post(self.endpoint, json=NATIVE_TOKEN_RESPONSE)
        assert self.client.native_token == {
            "tokenInfoURL": "https://tokens.radixdlt.com/",
            "symbol": "xrd",
            "isSupplyMutable": True,
            "granularity": "1",
            "name": "Rads",
            "rri": "xrd_rb1qya85pwq",
            "description": "Radix Betanet Tokens",
            "currentSupply": "999999999999999999999998479700000000000000000",
            "iconURL": "https://assets.radixdlt.com/icons/icon-xrd-32x32.png",
        }

    def test_token_balances(self, requests_mock):
        requests_mock.post(self.endpoint, json=TOKEN_BALANCES_RESPONSE)
        assert self.client.get_token_balances("fake-address") == [
            {
                "amount": "70000000000000000000",
                "rri": "cerb_rb1qvvm3mx58augl027sfv229f6qmsqq6xc7nqkncacxe0sp6faqs",
            },
            {
                "amount": "105000000000000000000",
                "rri": "emunie_rb1q0wsjfurhlus3dz9qgxd84an53cseqcjvl08sv3gr2qqmzkd2c",
            },
            {
                "amount": "97111111200000000000",
                "rri": "gum_rb1qduv0q8xtvgz5jqt4cmedyvaen88hu3pxrchhvp8xx9s5yjeh5",
            },
            {"amount": "139706666666666670000", "rri": "xrd_rb1qya85pwq"},
        ]
