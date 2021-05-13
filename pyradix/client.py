import os
import fire
from functools import partial

from tinyrpc import RPCClient
from tinyrpc.protocols.jsonrpc import JSONRPCProtocol
from tinyrpc.transports.http import HttpPostClientTransport

RADIX_PREFIX = 'radix.'


class Client:
    def __init__(self, node_url=None):
        rpc_client = RPCClient(
            JSONRPCProtocol(),
            HttpPostClientTransport(node_url or os.getenv("RADIX_NODE_URL")),
        )
        self._rpc_client = rpc_client.get_proxy(prefix=RADIX_PREFIX)

    @property
    def network_id(self):
        return self._rpc_client.networkId()['networkId']

    @property
    def network_tps(self):
        return self._rpc_client.networkTransactionThroughput()['tps']

    @property
    def network_tps_demand(self):
        return self._rpc_client.networkTransactionDemand()['tps']

    @property
    def network_native_token(self):
        return self._rpc_client.nativeToken()

    def get_token_info(self, token_id):
        return self._rpc_client.nativeToken(token_id)

    def get_token_balances(self, address):
        return self._rpc_client.tokenBalances(address)['tokenBalances']

    def get_transaction(self, transaction_id):
        return self._rpc_client.lookupTransaction(transaction_id)

    def get_transaction_history(self, address, n=100, cursor=1):
        return self._rpc_client.transactionHistory(address, n, cursor)

    def get_stake_positions(self, address):
        return self._rpc_client.stakePositions(address)

    def get_unstaked_positions(self, address):
        return self._rpc_client.unstakePositions(address)

    def get_transaction_status(self, transaction_id):
        return self._rpc_client.statusOfTransaction(transaction_id)['status']

    def get_validator(self, validator_id):
        return self._rpc_client.lookupValidator(validator_id)

    def get_validators(self, n=100, cursor=1):
        return self._rpc_client.validators(n, cursor)

    def transfer_tokens(self, from_, to, amount, token_id):
        return self._build_transaction(
            [
                {
                    'type': 'TokenTransfer',
                    'from': from_,
                    'to': to,
                    'amount': amount,
                    'tokenIdentifier': token_id,
                }
            ]
        )

    def stake_tokens(self, from_, validator_id, amount):
        return self._build_transaction(
            [
                {
                    'type': 'StakeTokens',
                    'from': from_,
                    'validator': validator_id,
                    'amount': amount,
                }
            ]
        )

    def unstake_tokens(self, from_, validator_id, amount):
        return self._build_transaction(
            [
                {
                    'type': 'UnstakeTokens',
                    'from': from_,
                    'validator': validator_id,
                    'amount': amount,
                }
            ]
        )

    def submit_transaction(self, signature):
        return self._rpc_client.submitTransaction(signature)

    def finalize_transaction(self, signature):
        return self._rpc_client.finalizeTransaction(signature)

    def _build_transaction(self, params):
        return self._rpc_client.buildTransaction(params)
