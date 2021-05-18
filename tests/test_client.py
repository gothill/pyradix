#!/usr/bin/env python

from unittest.mock import patch

import pytest
from tinyrpc.client import RPCProxy

from pyradix import Client
from pyradix.constants import RPC_METHOD_PREFIX


class TestClient:
    @pytest.fixture(autouse=True)
    def setup_case(self):
        self.endpoint = 'http://fake-radix/rpc'
        self.client = Client(node_url=self.endpoint)

    def test_rpc_proxy(self):
        rpc_proxy = self.client._rpc_proxy
        assert isinstance(rpc_proxy, RPCProxy)
        assert rpc_proxy.prefix == RPC_METHOD_PREFIX
        assert rpc_proxy.client.transport.endpoint == self.endpoint

    def test_network_id(self):
        with patch.object(
            self.client._rpc_proxy,
            'networkId',
            return_value=dict(networkId=3),
        ) as mock:
            assert self.client.network_id == 3
            assert mock.called

    def test_network_tps(self):
        with patch.object(
            self.client._rpc_proxy,
            'networkTransactionThroughput',
            return_value=dict(tps=15000),
        ) as mock:
            assert self.client.network_tps == 15000
            assert mock.called

    def test_network_tps_demand(self):
        with patch.object(
            self.client._rpc_proxy,
            'networkTransactionDemand',
            return_value=dict(tps=20000),
        ) as mock:
            assert self.client.network_tps_demand == 20000
            assert mock.called

    def test_native_token(self):
        with patch.object(
            self.client._rpc_proxy,
            'nativeToken',
            return_value=dict(rri='xrd'),
        ) as mock:
            assert self.client.native_token == dict(rri='xrd')
            assert mock.called

    def test_token_balances(self):
        with patch.object(
            self.client._rpc_proxy,
            'tokenBalances',
            return_value=dict(tokenBalances=dict(rri='xrd', amount='200')),
        ) as mock:
            assert self.client.get_token_balances('address') == dict(
                rri='xrd', amount='200'
            )
            mock.assert_called_once_with('address')

    def test_get_transaction(self):
        with patch.object(
            self.client._rpc_proxy,
            'lookupTransaction',
            return_value=dict(txID='tx-id', sentAt='1995-12-17T03:24:00'),
        ) as mock:
            assert self.client.get_transaction('tx-id') == dict(
                txID='tx-id', sentAt='1995-12-17T03:24:00'
            )
            mock.assert_called_once_with('tx-id')

    def test_transaction_history(self):
        with patch.object(
            self.client._rpc_proxy,
            'transactionHistory',
            return_value=dict(cursor='1', transactions=[1, 2, 3]),
        ) as mock:
            assert self.client.get_transaction_history(
                'address', n=10, cursor='cursor'
            ) == dict(cursor='1', transactions=[1, 2, 3])
            mock.assert_called_once_with('address', 10, 'cursor')

    def test_get_stake_positions(self):
        with patch.object(
            self.client._rpc_proxy,
            'stakePositions',
            return_value=dict(
                fee='10',
                transaction=dict(blob='b', hashOfBlobToSign='h'),
            ),
        ) as mock:
            assert self.client.get_stake_positions('address') == dict(
                fee='10',
                transaction=dict(blob='b', hashOfBlobToSign='h'),
            )
            mock.assert_called_once_with('address')

    def test_get_unstaked_positions(self):
        with patch.object(
            self.client._rpc_proxy,
            'unstakePositions',
            return_value=dict(
                fee='10',
                transaction=dict(blob='b', hashOfBlobToSign='h'),
            ),
        ) as mock:
            assert self.client.get_unstaked_positions('address') == dict(
                fee='10',
                transaction=dict(blob='b', hashOfBlobToSign='h'),
            )
            mock.assert_called_once_with('address')

    def test_get_transaction_status(self):
        with patch.object(
            self.client._rpc_proxy,
            'statusOfTransaction',
            return_value=dict(status='CONFIRMED'),
        ) as mock:
            assert self.client.get_transaction_status('tx-id') == 'CONFIRMED'
            mock.assert_called_once_with('tx-id')

    def test_get_validator(self):
        with patch.object(
            self.client._rpc_proxy,
            'lookupValidator',
            return_value=dict(address='address', totalDelegatedStake=30000),
        ) as mock:
            assert self.client.get_validator('address') == dict(
                address='address', totalDelegatedStake=30000
            )
            mock.assert_called_once_with('address')

    def test_get_validators(self):
        with patch.object(
            self.client._rpc_proxy,
            'validators',
            return_value=[1, 2, 3],
        ) as mock:
            assert self.client.get_validators() == [1, 2, 3]
            assert mock.called

    def test_transfer_tokens(self):
        with patch.object(
            self.client._rpc_proxy,
            'buildTransaction',
            return_value=dict(txID='tx-id'),
        ) as mock:
            assert (
                self.client.transfer_tokens(
                    from_='from-address',
                    to='to-address',
                    amount=99,
                    token_id='xrd',
                )
                == dict(txID='tx-id')
            )
            mock.assert_called_once_with(
                [
                    {
                        'type': 'TokenTransfer',
                        'from': 'from-address',
                        'to': 'to-address',
                        'amount': 99,
                        'tokenIdentifier': 'xrd',
                    }
                ]
            )

    def test_stake_tokens(self):
        with patch.object(
            self.client._rpc_proxy,
            'buildTransaction',
            return_value=dict(txID='tx-id'),
        ) as mock:
            assert self.client.stake_tokens(
                from_='from-address', validator_id='to-address', amount=99
            ) == dict(txID='tx-id')
            mock.assert_called_once_with(
                [
                    {
                        'type': 'StakeTokens',
                        'from': 'from-address',
                        'validator': 'to-address',
                        'amount': 99,
                    }
                ]
            )

    def test_unstake_tokens(self):
        with patch.object(
            self.client._rpc_proxy,
            'buildTransaction',
            return_value=dict(txID='tx-id'),
        ) as mock:
            assert self.client.unstake_tokens(
                from_='from-address', validator_id='to-address', amount=99
            ) == dict(txID='tx-id')
            mock.assert_called_once_with(
                [
                    {
                        'type': 'UnstakeTokens',
                        'from': 'from-address',
                        'validator': 'to-address',
                        'amount': 99,
                    }
                ]
            )

    def test_submit_transaction(self):
        with patch.object(
            self.client._rpc_proxy,
            'submitTransaction',
            return_value=dict(txID='tx-id'),
        ) as mock:
            assert self.client.submit_transaction(
                public_key='pk', blob='b', signature='s'
            ) == dict(txID='tx-id')
            mock.assert_called_once_with(dict(blob='b'), 'pk', 's')

    def test_finalize_transaction(self):
        with patch.object(
            self.client._rpc_proxy,
            'finalizeTransaction',
            return_value=dict(txID='tx-id'),
        ) as mock:
            assert self.client.finalize_transaction(
                public_key='pk', blob='b', signature='s'
            ) == dict(txID='tx-id')
            mock.assert_called_once_with(dict(blob='b'), 'pk', 's')
