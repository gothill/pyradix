#!/usr/bin/env python

'''Tests for `pyradix` package.'''

import pytest

from pyradix import Client

DUMMY_RESPONSE = {
    'result': {'key': 'value'},
    'id': 1,
    'jsonrpc': '2.0',
}


@pytest.fixture
def dummy_response():
    return DUMMY_RESPONSE


class TestClient:
    @pytest.fixture(autouse=True)
    def setup_case(self):
        self.endpoint = 'http://fake-radix/rpc'
        self.client = Client(node_url=self.endpoint)

    def test_network_id(self, requests_mock, dummy_response):
        requests_mock.post(self.endpoint, json=dummy_response)
        assert self.client.network_id == dummy_response['result']

    def test_network_throughput(self, requests_mock, dummy_response):
        requests_mock.post(self.endpoint, json=dummy_response)
        assert self.client.network_throughput == dummy_response['result']

    def test_network_throughput_demand(self, requests_mock, dummy_response):
        requests_mock.post(self.endpoint, json=dummy_response)
        assert (
            self.client.network_throughput_demand == dummy_response['result']
        )

    def test_native_token(self, requests_mock, dummy_response):
        requests_mock.post(self.endpoint, json=dummy_response)
        assert self.client.native_token == dummy_response['result']

    def test_token_balances(self, requests_mock, dummy_response):
        requests_mock.post(self.endpoint, json=dummy_response)
        assert (
            self.client.get_token_balances('address')
            == dummy_response['result']
        )

    def test_transaction_history(self, requests_mock, dummy_response):
        requests_mock.post(self.endpoint, json=dummy_response)
        assert (
            self.client.get_transaction_history('address')
            == dummy_response['result']
        )

    def test_get_stake_positions(self, requests_mock, dummy_response):
        requests_mock.post(self.endpoint, json=dummy_response)
        assert (
            self.client.get_stake_positions('address')
            == dummy_response['result']
        )

    def test_get_unstaked_positions(self, requests_mock, dummy_response):
        requests_mock.post(self.endpoint, json=dummy_response)
        assert (
            self.client.get_unstaked_positions('address')
            == dummy_response['result']
        )

    def test_get_transaction_status(self, requests_mock, dummy_response):
        requests_mock.post(self.endpoint, json=dummy_response)
        assert (
            self.client.get_transaction_status('transaction-id')
            == dummy_response['result']
        )

    def test_get_validators(self, requests_mock, dummy_response):
        requests_mock.post(self.endpoint, json=dummy_response)
        assert self.client.get_validators() == dummy_response['result']

    def test_get_validator(self, requests_mock, dummy_response):
        requests_mock.post(self.endpoint, json=dummy_response)
        assert (
            self.client.get_validator('validator-id')
            == dummy_response['result']
        )

    def test_transfer_tokens(self, requests_mock, dummy_response):
        requests_mock.post(self.endpoint, json=dummy_response)
        assert (
            self.client.transfer_tokens(
                from_='address',
                to='another-address',
                amount=12,
                token_id='token-id',
            )
            == dummy_response['result']
        )

    def test_stake_tokens(self, requests_mock, dummy_response):
        requests_mock.post(self.endpoint, json=dummy_response)
        assert (
            self.client.stake_tokens(
                from_='address', validator_id='validator-id', amount=1000
            )
            == dummy_response['result']
        )

    def test_unstake_tokens(self, requests_mock, dummy_response):
        requests_mock.post(self.endpoint, json=dummy_response)
        assert (
            self.client.unstake_tokens(
                from_='address', validator_id='validator-id', amount=1000
            )
            == dummy_response['result']
        )

    def test_finalize_transaction(self, requests_mock, dummy_response):
        requests_mock.post(self.endpoint, json=dummy_response)
        result = self.client.finalize_transaction(signature='signature')
        assert result == dummy_response['result']

    def test_submit_transaction(self, requests_mock, dummy_response):
        requests_mock.post(self.endpoint, json=dummy_response)
        assert (
            self.client.submit_transaction(signature='signature')
            == dummy_response['result']
        )

    def test_get_transaction(self, requests_mock, dummy_response):
        requests_mock.post(self.endpoint, json=dummy_response)
        assert (
            self.client.submit_transaction(signature='signature')
            == dummy_response['result']
        )
