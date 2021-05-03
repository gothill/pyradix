import fire

from .connection import Connection


class Client(Connection):
    @property
    def network_id(self):
        return self._request("networkId")["networkId"]

    @property
    def network_tps(self):
        return self._request("networkTransactionThroughput")["tps"]

    @property
    def network_tps_demand(self):
        return self._request("networkTransactionDemand")["tps"]

    @property
    def native_token(self):
        return self._request("nativeToken")

    def get_token_info(self, token_id):
        return self._request("tokenInfo", [token_id])

    def get_token_balances(self, address):
        return self._request("tokenBalances", [address])["tokenBalances"]

    def get_transaction_history(self, address, n=100):
        # TODO: Pagination broken here.
        cursor = 1
        return self._request("transactionHistory", [address, n, cursor])

    def get_stake_positions(self, address):
        result = self._request("stakePositions", [address])
        if "stakePositions" in result:
            return result["stakePositions"]
        return []

    def get_unstaked_positions(self, address):
        result = self._request("unstakePositions", [address])
        if "unstakePositions" in result:
            return result["unstakePositions"]
        return []

    def get_transaction_status(self, transaction_id):
        return self._request("statusOfTransaction", [transaction_id])["status"]

    def get_validators(self, n=100):
        cursor = 1
        while cursor:
            result = self._request("validators", [n, cursor])
            cursor = result["cursor"]
            yield from iter(result["validators"])

    def get_validator(self, validator_id):
        return self._request("lookupValidator", [validator_id])

    def transfer_tokens(self, from_, to, amount, token_id):
        """In the wallet, this could return a transaction object
        in a pending state and a confirmation method which signs it.
        """
        return self._build_transaction(
            [
                {
                    "type": "TokenTransfer",
                    "from": from_,
                    "to": to,
                    "amount": amount,
                    "tokenIdentifier": token_id,
                }
            ]
        )

    def stake_tokens(self, from_, validator_id, amount):
        return self._build_transaction(
            [
                {
                    "type": "StakeTokens",
                    "from": from_,
                    "validator": validator_id,
                    "amount": amount,
                }
            ]
        )

    def unstake_tokens(self, from_, validator_id, amount):
        return self._build_transaction(
            [
                {
                    "type": "UnstakeTokens",
                    "from": from_,
                    "validator": validator_id,
                    "amount": amount,
                }
            ]
        )

    def finalize_transaction(self, signature):
        return self._request("finalizeTransaction", [signature])

    def submit_transaction(self, signature):
        return self._request("submitTransaction", [signature])

    def get_transaction(self, transaction_id):
        return self._request("lookupTransaction", [transaction_id])

    def _build_transaction(self, params):
        return self._request("buildTransaction", [params])


if __name__ == "__main__":
    fire.Fire(Client)
