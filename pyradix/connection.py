import os
import requests


class Connection:
    def __init__(self, node_url=None):
        self.node_url = node_url or os.getenv("RADIX_NODE_URL")

    def _request(self, method, params=None):
        response = requests.post(
            self.node_url,
            json=dict(
                jsonrpc="2.0",
                method=f"radix.{method}",
                params=params if not None else [],
                id=1,
            ),
        )
        if response.ok:
            json_response = response.json()
            self._handle_errors(json_response)
            return json_response["result"]
        else:
            raise Exception("Request failed")

    def _handle_errors(self, json_response):
        if "error" in json_response:
            message = json_response["error"]["message"]
            code = json_response["error"]["code"]
            raise Exception(f"{code}: {message}")
