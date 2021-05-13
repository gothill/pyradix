import fire
from collections import partial

from pyradix.connection import Connection


radix_spec = [
    dict(
        method_name='network_id',
        api_name='newtorkID',
    )
]


class Client(Connection):
    # def _inject_api_methods(self, radix_spec):
    #     for operation_id, kwargs in radix_spec.items():
    #         use_schema_validation = not operation_id.endswith(
    #             ('_patch', '_put')
    #         )
    #         setattr(
    #             self,
    #             operation_id,
    #             partial(
    #                 self._call,
    #                 operation_id=operation_id,
    #             ),
    #         )
    @property
    def network_id(self):
        return self._request('networkId')

    @property
    def network_throughput(self):
        return self._request('networkTransactionThroughput')

    @property
    def network_throughput_demand(self):
        return self._request('networkTransactionDemand')

    @property
    def native_token(self):
        return self._request('nativeToken')

    def get_token_info(self, token_id):
        return self._request('tokenInfo', [token_id])

    def get_token_balances(self, address):
        return self._request('tokenBalances', [address])

    def get_transaction(self, transaction_id):
        return self._request('lookupTransaction', [transaction_id])

    def get_transaction_history(self, address, n=100, cursor=1):
        return self._request('transactionHistory', [address, n, cursor])

    def get_stake_positions(self, address):
        return self._request('stakePositions', [address])

    def get_unstaked_positions(self, address):
        return self._request('unstakePositions', [address])

    def get_transaction_status(self, transaction_id):
        return self._request('statusOfTransaction', [transaction_id])

    def get_validators(self, n=100, cursor=1):
        cursor = 1
        return self._request('validators', [n, cursor])

    def get_validator(self, validator_id):
        return self._request('lookupValidator', [validator_id])

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
        return self._request('submitTransaction', [signature])

    def finalize_transaction(self, signature):
        return self._request('finalizeTransaction', [signature])

    def _build_transaction(self, params):
        return self._request('buildTransaction', [params])


if __name__ == '__main__':
    fire.Fire(Client)
