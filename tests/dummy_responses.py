NETWORK_ID_RESPONSE = {"result": {"networkId": 17}, "id": 1, "jsonrpc": "2.0"}
NETWORK_TPS_RESPONSE = {
    "result": {"tps": 10000},
    "id": "1",
    "jsonrpc": "2.0",
}
NETWORK_TPS_DEMAND_RESPONSE = {"result": {"tps": 100000}, "id": 1, "jsonrpc": "2.0"}
NATIVE_TOKEN_RESPONSE = {
    "result": {
        "tokenInfoURL": "https://tokens.radixdlt.com/",
        "symbol": "xrd",
        "isSupplyMutable": True,
        "granularity": "1",
        "name": "Rads",
        "rri": "xrd_rb1qya85pwq",
        "description": "Radix Betanet Tokens",
        "currentSupply": "999999999999999999999998479700000000000000000",
        "iconURL": "https://assets.radixdlt.com/icons/icon-xrd-32x32.png",
    },
    "id": 1,
    "jsonrpc": "2.0",
}
TOKEN_INFO_RESPONSE = NATIVE_TOKEN_RESPONSE
TOKEN_BALANCES_RESPONSE = {
    "result": {
        "owner": "brx1qsp6ckn3ylhqgf0g80c4vrl0c60f96mdnrc4ukfgppnnjfvjfsu4gsg35hja6",
        "tokenBalances": [
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
        ],
    },
    "id": 1,
    "jsonrpc": "2.0",
}
TRANSACTION_HISTORY_RESPONSE = {
    "result": {
        "cursor": "cursor",
        "transactions": [
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
        ],
    },
    "id": "1",
    "jsonrpc": "2.0",
}
STAKE_POSITIONS_RESPONSE = {
    "result": {
        "stakePositions": [
            {
                "validator": "9S8khLHZa6FsyGo634xQo9QwLgSHGpXHHW764D5mPYBcrnfZV6RT",
                "amount": "100",
            }
        ]
    },
    "id": "1",
    "jsonrpc": "2.0",
}
UNSTAKED_POSITIONS_RESPONSE = {
    "result": [
        {
            "amount": "100",
            "validator": "9S8khLHZa6FsyGo634xQo9QwLgSHGpXHHW764D5mPYBcrnfZV6RT",
        }
    ],
    "id": "1",
    "jsonrpc": "2.0",
}
TRANSACTION_STATUS_RESPONSE = {
    "result": {
        "transactionStatus": {
            "txID": "1b69e967eccfd2b8b5f4bea21a4efd74dc53c590994b725ea7600bff1020c132",
            "status": "CONFIRMED",
        }
    },
    "id": "1",
    "jsonrpc": "2.0",
}
VALIDATORS_RESPONSE = {
    "result": {
        "cursor": "validatorCursor",
        "validators": [
            {
                "address": "9S8khLHZa6FsyGo634xQo9QwLgSHGpXHHW764D5mPYBcrnfZV6RT",
                "ownerAddress": "9S8khLHZa6FsyGo634xQo9QwLgSHGpXHHW764D5mPYBcrnfZV6RT",
                "name": "Cerby",
                "infoURL": "https://www.radixdlt.com",
                "totalDelegatedStake": "100",
                "ownerDelegation": "100",
                "isExternalStakeAccepted": "true",
            }
        ],
    },
    "id": "1",
    "jsonrpc": "2.0",
}
VALIDATOR_RESPONSE = {
    "result": {
        "address": "vb1q00jd22ygzsg8p05ht5hwz5qvx9yjc532ffe895jkez0lkgqztmny9uzhav",
        "ownerAddress": "9S8khLHZa6FsyGo634xQo9QwLgSHGpXHHW764D5mPYBcrnfZV6RT",
        "name": "Cerby",
        "infoURL": "https://www.radixdlt.com",
        "totalDelegatedStake": "100",
        "ownerDelegation": "100",
        "isExternalStakeAccepted": "true",
    },
    "id": "1",
    "jsonrpc": "2.0",
}
TOKEN_TRANSFER_RESPONSE = {
    "result": {
        "transaction": {
            "blob": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            "hashOfBlobToSign": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        },
        "fee": "100",
    },
    "id": "1",
    "jsonrpc": "2.0",
}
STAKE_RESPONSE = {
    "result": {
        "transaction": {
            "blob": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            "hashOfBlobToSign": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        },
        "fee": "100",
    },
    "id": "1",
    "jsonrpc": "2.0",
}
UNSTAKE_RESPONSE = {
    "result": {
        "transaction": {
            "blob": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            "hashOfBlobToSign": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        },
        "fee": "100",
    },
    "id": "1",
    "jsonrpc": "2.0",
}
FINALIZE_RESPONSE = {
    "result": {
        "txID": "d52e7fa4fe41bfc04495227a982a7f7d21165a7b4ffcb90210b760ea3554d042"
    },
    "id": "1",
    "jsonrpc": "2.0",
}
SUBMIT_RESPONSE = {
    "result": {
        "submissionResult": {
            "txID": "d52e7fa4fe41bfc04495227a982a7f7d21165a7b4ffcb90210b760ea3554d042"
        }
    },
    "id": "1",
    "jsonrpc": "2.0",
}
TRANSACTION_RESPONSE = {
    "result": {
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
    },
    "id": "1",
    "jsonrpc": "2.0",
}
