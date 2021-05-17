from pprint import pprint

import click

from pyradix.client import Client


@click.group()
@click.pass_context
def main(ctx):
    ctx.obj['client'] = Client()


@main.command()
@click.pass_context
def network_id(ctx):
    print(ctx.obj['client'].network_id)


@main.command()
@click.pass_context
def network_tps(ctx):
    print(ctx.obj['client'].network_tps)


@main.command()
@click.pass_context
def network_tps_demand(ctx):
    print(ctx.obj['client'].network_tps_demand)


@main.command()
@click.pass_context
def native_token(ctx):
    pprint(ctx.obj['client'].native_token)


@main.command()
@click.option('--id', help='ID of the token to lookup')
@click.pass_context
def token_info(ctx, id):
    pprint(ctx.obj['client'].get_token_info(id))


@main.command()
@click.option('--address', help='Address to lookup balances for')
@click.pass_context
def token_balances(ctx, address):
    pprint(ctx.obj['client'].get_token_balances(address))


@main.command()
@click.option('--id', help='ID of the transaction to lookup')
@click.pass_context
def transaction_info(ctx, id):
    pprint(ctx.obj['client'].get_transaction(id))


@main.command()
@click.option('--id', help='ID of the transaction to lookup')
@click.pass_context
def transaction_status(ctx, id):
    print(ctx.obj['client'].get_transaction_status(id))


@main.command()
@click.option('--address', help='Address to lookup transaction history for')
@click.option('--n', help='Number of transactions to fetch', default=5)
@click.option('--cursor', help='Continuation cursor', default='1')
@click.pass_context
def transaction_history(ctx, address, n, cursor):
    pprint(ctx.obj['client'].get_transaction_history(address, n, cursor))


@main.command()
@click.option('--address', help='Address to lookup stake positions for')
@click.pass_context
def stake_positions(ctx, address):
    pprint(ctx.obj['client'].get_stake_positions(address))


@main.command()
@click.option('--address', help='Address to lookup unstaked positions for')
@click.pass_context
def unstaked_positions(ctx, address):
    pprint(ctx.obj['client'].get_unstaked_positions(address))


@main.command()
@click.option('--id', help='ID of the validator to lookup')
@click.pass_context
def validator_info(ctx, id):
    pprint(ctx.obj['client'].get_validator(id))


@main.command()
@click.option('--n', help='Number of transactions to fetch', default=5)
@click.option('--cursor', help='Continuation cursor', default='1')
@click.pass_context
def validators(ctx, n, cursor):
    pprint(ctx.obj['client'].get_validators(n, cursor))


@main.command()
@click.option('--from', 'from_')
@click.option('--to', help='')
@click.option('--amount', help='')  # TODO: Make amount an integer (also below)
@click.option('--token-id', help='')
@click.pass_context
def transfer_tokens(ctx, from_, to, amount, token_id):
    pprint(ctx.obj['client'].transfer_tokens(from_, to, amount, token_id))


@main.command()
@click.option('--from', 'from_')
@click.option('--validator-id', help='')
@click.option('--amount', help='')
@click.pass_context
def stake_tokens(ctx, from_, validator_id, amount):
    pprint(ctx.obj['client'].stake_tokens(from_, validator_id, amount))


@main.command()
@click.option('--from', 'from_')
@click.option('--validator-id', help='')
@click.option('--amount', help='')
@click.pass_context
def unstake_tokens(ctx, from_, validator_id, amount):
    pprint(ctx.obj['client'].unstake_tokens(from_, validator_id, amount))


@main.command()
@click.option('--public-key', help='')
@click.option('--blob', help='')
@click.option('--signature', help='')
@click.pass_context
def submit_transaction(ctx, public_key, blob, signature):
    # TODO: Fix me
    pprint(ctx.obj['client'].submit_transaction(public_key, blob, signature))


@main.command()
@click.option('--public-key', help='')
@click.option('--blob', help='')
@click.option('--signature', help='')
@click.pass_context
def finalize_transaction(ctx, public_key, blob, signature):
    pprint(ctx.obj['client'].finalize_transaction(public_key, blob, signature))


def start():
    main(obj={})


if __name__ == '__main__':
    start()
