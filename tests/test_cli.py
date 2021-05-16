from unittest.mock import patch, MagicMock

from click.testing import CliRunner
import pytest

from pyradix.cli import main
from pyradix.client import Client


@patch('pyradix.cli.Client')
class TestCLI:
    @pytest.fixture(autouse=True)
    def setup_case(self):
        self.runner = CliRunner()

    def test_network_id(self, Client):
        Client.return_value = MagicMock(network_id=3)
        result = self.runner.invoke(main, ['network-id'], obj={})
        assert result.exit_code == 0
        assert result.output == '3\n'

    def test_network_tps(self, Client):
        Client.return_value = MagicMock(network_tps=15000)
        result = self.runner.invoke(main, ['network-tps'], obj={})
        assert result.exit_code == 0
        assert result.output == '15000\n'

    def test_network_tps_demand(self, Client):
        Client.return_value = MagicMock(network_tps_demand=20000)
        result = self.runner.invoke(main, ['network-tps-demand'], obj={})
        assert result.exit_code == 0
        assert result.output == '20000\n'

    def test_native_token(self, Client):
        Client.return_value = MagicMock(native_token=dict(rri='xrd'))
        result = self.runner.invoke(main, ['native-token'], obj={})
        assert result.exit_code == 0
        assert result.output == "{'rri': 'xrd'}\n"

    def test_token_balances(self, Client):
        mock_client = MagicMock(
            get_token_balances=MagicMock(
                return_value=dict(rri='xrd', amount='200')
            )
        )
        Client.return_value = mock_client
        result = self.runner.invoke(
            main, ['token-balances', '--address', 'address'], obj={}
        )
        assert result.exit_code == 0
        assert result.output == "{'amount': '200', 'rri': 'xrd'}\n"
        mock_client.get_token_balances.assert_called_once_with('address')

    def test_transaction_info(self, Client):
        mock_client = MagicMock(
            get_transaction=MagicMock(
                return_value=dict(txID='tx-id', sentAt='1995-12-17T03:24:00')
            )
        )
        Client.return_value = mock_client
        result = self.runner.invoke(
            main, ['transaction-info', '--id', 'tx-id'], obj={}
        )
        assert result.exit_code == 0
        assert (
            result.output
            == "{'sentAt': '1995-12-17T03:24:00', 'txID': 'tx-id'}\n"
        )
        mock_client.get_transaction.assert_called_once_with('tx-id')

    def test_transaction_status(self, Client):
        mock_client = MagicMock(
            get_transaction_status=MagicMock(return_value='CONFIRMED')
        )
        Client.return_value = mock_client
        result = self.runner.invoke(
            main, ['transaction-status', '--id', 'tx-id'], obj={}
        )
        assert result.exit_code == 0
        assert result.output == "CONFIRMED\n"
        mock_client.get_transaction_status.assert_called_once_with('tx-id')

    def test_transaction_history(self, Client):
        mock_client = MagicMock(
            get_transaction_history=MagicMock(return_value=[1, 2, 3])
        )
        Client.return_value = mock_client
        result = self.runner.invoke(
            main,
            [
                'transaction-history',
                '--address',
                'address',
                '--n',
                '10',
                '--cursor',
                'cursor',
            ],
            obj={},
        )
        assert result.exit_code == 0
        assert result.output == '[1, 2, 3]\n'
        mock_client.get_transaction_history.assert_called_once_with(
            'address', 10, 'cursor'
        )

    def test_stake_positions(self, Client):
        mock_client = MagicMock(
            get_stake_positions=MagicMock(return_value=[1, 2, 3])
        )
        Client.return_value = mock_client
        result = self.runner.invoke(
            main, ['stake-positions', '--address', 'address'], obj={}
        )
        assert result.exit_code == 0
        assert result.output == '[1, 2, 3]\n'
        mock_client.get_stake_positions.assert_called_once_with('address')
