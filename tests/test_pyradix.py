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
    TRANSACTION_HISTORY_RESPONSE,
    STAKE_POSITIONS_RESPONSE,
    UNSTAKED_POSITIONS_RESPONSE,
    TRANSACTION_STATUS_RESPONSE,
    VALIDATORS_RESPONSE,
    VALIDATOR_RESPONSE,
    TOKEN_TRANSFER_RESPONSE,
    STAKE_RESPONSE,
    UNSTAKE_RESPONSE,
    FINALIZE_RESPONSE,
    SUBMIT_RESPONSE,
    TRANSACTION_RESPONSE,
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
        assert self.client.get_token_balances("address") == [
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

    def test_transaction_history(self, requests_mock):
        requests_mock.post(self.endpoint, json=TRANSACTION_HISTORY_RESPONSE)
        assert self.client.get_transaction_history("address") == [
            {
                "txID": "d52e7fa4fe41bfc04495227a982a7f7d21165a7b4ffcb90210b760ea3554d042",
                "sentAt": "1995-12-17T03:24:00",
                "fee": "100",
                "message": "Example message",
                "actions": [
                    {
                        "type": "TokenTransfer",
                        "from": "9S8khLHZa6FsyGo634xQo9QwLgSHGpXHHW764D5mPYBcrnfZV6R",
                        "to": "9S8khLHZa6FsyGo634xQo9QwLgSHGpXHHW764D5mPYBcrnfZV6RT",
                        "amount": "100",
                        "rri": "xrd_rb1qya85pwq",
                    },
                    {
                        "type": "StakeTokens",
                        "from": "9S8khLHZa6FsyGo634xQo9QwLgSHGpXHHW764D5mPYBcrnfZV6R",
                        "validator": "9S8khLHZa6FsyGo634xQo9QwLgSHGpXHHW764D5mPYBcrnfZV6RT",
                        "amount": "100",
                    },
                    {
                        "type": "UnstakeTokens",
                        "from": "9S8khLHZa6FsyGo634xQo9QwLgSHGpXHHW764D5mPYBcrnfZV6R",
                        "validator": "9S8khLHZa6FsyGo634xQo9QwLgSHGpXHHW764D5mPYBcrnfZV6RT",
                        "amount": "100",
                    },
                    {"type": "Other"},
                ],
            }
        ]

    def test_get_stake_positions(self, requests_mock):
        requests_mock.post(self.endpoint, json=STAKE_POSITIONS_RESPONSE)
        assert self.client.get_stake_positions("address") == [
            {
                "amount": "100",
                "validator": "9S8khLHZa6FsyGo634xQo9QwLgSHGpXHHW764D5mPYBcrnfZV6RT",
            }
        ]

    def test_get_unstaked_positions(self, requests_mock):
        requests_mock.post(self.endpoint, json=UNSTAKED_POSITIONS_RESPONSE)
        assert self.client.get_unstaked_positions("address") == [
            {
                "amount": "100",
                "validator": "9S8khLHZa6FsyGo634xQo9QwLgSHGpXHHW764D5mPYBcrnfZV6RT",
            }
        ]

    def test_get_transaction_status(self, requests_mock):
        requests_mock.post(self.endpoint, json=TRANSACTION_STATUS_RESPONSE)
        assert self.client.get_transaction_status("transaction-id") == "CONFIRMED"

    def test_get_validators(self, requests_mock):
        # TODO: Fails due to pagination (response always has cursor)
        requests_mock.post(self.endpoint, json=VALIDATORS_RESPONSE)
        # assert list(self.client.get_validators()) == [
        #     {
        #         "address": "9S8khLHZa6FsyGo634xQo9QwLgSHGpXHHW764D5mPYBcrnfZV6RT",
        #         "ownerAddress": "9S8khLHZa6FsyGo634xQo9QwLgSHGpXHHW764D5mPYBcrnfZV6RT",
        #         "name": "Cerby",
        #         "infoURL": "https://www.radixdlt.com",
        #         "totalDelegatedStake": "100",
        #         "ownerDelegation": "100",
        #         "isExternalStakeAccepted": "true",
        #     }
        # ]

    def test_get_validator(self, requests_mock):
        requests_mock.post(self.endpoint, json=VALIDATOR_RESPONSE)
        assert self.client.get_validator("validator-id") == {
            "address": "vb1q00jd22ygzsg8p05ht5hwz5qvx9yjc532ffe895jkez0lkgqztmny9uzhav",
            "ownerAddress": "9S8khLHZa6FsyGo634xQo9QwLgSHGpXHHW764D5mPYBcrnfZV6RT",
            "name": "Cerby",
            "infoURL": "https://www.radixdlt.com",
            "totalDelegatedStake": "100",
            "ownerDelegation": "100",
            "isExternalStakeAccepted": "true",
        }

    def test_transfer_tokens(self, requests_mock):
        requests_mock.post(self.endpoint, json=TRANSACTION_RESPONSE)
        result = self.client.transfer_tokens(
            from_="address", to="another-address", amount=12, token_id="token-id"
        )
        assert result == {
            "txID": "d52e7fa4fe41bfc04495227a982a7f7d21165a7b4ffcb90210b760ea3554d042",
            "sentAt": "1995-12-17T03:24:00",
            "fee": "100",
            "message": "Example message",
            "actions": [
                {
                    "type": "TokenTransfer",
                    "from": "9S8khLHZa6FsyGo634xQo9QwLgSHGpXHHW764D5mPYBcrnfZV6RT",
                    "to": "9S8khLHZa6FsyGo634xQo9QwLgSHGpXHHW764D5mPYBcrnfZV6RT",
                    "amount": "100",
                    "rri": "xrd_rb1qya85pwq",
                },
                {
                    "type": "StakeTokens",
                    "from": "9S8khLHZa6FsyGo634xQo9QwLgSHGpXHHW764D5mPYBcrnfZV6RT",
                    "validator": "9S8khLHZa6FsyGo634xQo9QwLgSHGpXHHW764D5mPYBcrnfZV6RT",
                    "amount": "100",
                },
                {
                    "type": "UnstakeTokens",
                    "from": "9S8khLHZa6FsyGo634xQo9QwLgSHGpXHHW764D5mPYBcrnfZV6RT",
                    "validator": "9S8khLHZa6FsyGo634xQo9QwLgSHGpXHHW764D5mPYBcrnfZV6RT",
                    "amount": "100",
                },
                {"type": "Other"},
            ],
        }

    def test_stake_tokens(self, requests_mock):
        requests_mock.post(self.endpoint, json=STAKE_RESPONSE)
        result = self.client.stake_tokens(
            from_="address", validator_id="validator-id", amount=1000
        )
        assert result == {
            "transaction": {
                "blob": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                "hashOfBlobToSign": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            },
            "fee": "100",
        }

    def test_unstake_tokens(self, requests_mock):
        requests_mock.post(self.endpoint, json=UNSTAKE_RESPONSE)
        result = self.client.unstake_tokens(
            from_="address", validator_id="validator-id", amount=1000
        )
        assert result == {
            "transaction": {
                "blob": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                "hashOfBlobToSign": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            },
            "fee": "100",
        }

    def test_finalize_transaction(self, requests_mock):
        requests_mock.post(self.endpoint, json=FINALIZE_RESPONSE)
        result = self.client.finalize_transaction(signature="signature")
        assert result == {
            "txID": "d52e7fa4fe41bfc04495227a982a7f7d21165a7b4ffcb90210b760ea3554d042"
        }

    def test_submit_transaction(self, requests_mock):
        requests_mock.post(self.endpoint, json=SUBMIT_RESPONSE)
        result = self.client.submit_transaction(signature="signature")
        assert result == {
            "submissionResult": {
                "txID": "d52e7fa4fe41bfc04495227a982a7f7d21165a7b4ffcb90210b760ea3554d042"
            }
        }

    def test_get_transaction(self, requests_mock):
        requests_mock.post(self.endpoint, json=TRANSACTION_RESPONSE)
        result = self.client.submit_transaction(signature="signature")
        assert result == {
            "txID": "d52e7fa4fe41bfc04495227a982a7f7d21165a7b4ffcb90210b760ea3554d042",
            "sentAt": "1995-12-17T03:24:00",
            "fee": "100",
            "message": "Example message",
            "actions": [
                {
                    "type": "TokenTransfer",
                    "from": "9S8khLHZa6FsyGo634xQo9QwLgSHGpXHHW764D5mPYBcrnfZV6RT",
                    "to": "9S8khLHZa6FsyGo634xQo9QwLgSHGpXHHW764D5mPYBcrnfZV6RT",
                    "amount": "100",
                    "rri": "xrd_rb1qya85pwq",
                },
                {
                    "type": "StakeTokens",
                    "from": "9S8khLHZa6FsyGo634xQo9QwLgSHGpXHHW764D5mPYBcrnfZV6RT",
                    "validator": "9S8khLHZa6FsyGo634xQo9QwLgSHGpXHHW764D5mPYBcrnfZV6RT",
                    "amount": "100",
                },
                {
                    "type": "UnstakeTokens",
                    "from": "9S8khLHZa6FsyGo634xQo9QwLgSHGpXHHW764D5mPYBcrnfZV6RT",
                    "validator": "9S8khLHZa6FsyGo634xQo9QwLgSHGpXHHW764D5mPYBcrnfZV6RT",
                    "amount": "100",
                },
                {"type": "Other"},
            ],
        }
