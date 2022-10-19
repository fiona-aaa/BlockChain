from bitcoin.core.script import *

from utils import *
from config import (my_private_key, my_public_key, my_address, faucet_address)


def split_coins(amount_to_send, txid_to_spend, utxo_index, n):
    txin_scriptPubKey = my_address.to_scriptPubKey()
    txin = create_txin(txid_to_spend, utxo_index)
    txout_scriptPubKey = my_address.to_scriptPubKey()
    txout = create_txout(amount_to_send / n, txout_scriptPubKey)
    tx = CMutableTransaction([txin], [txout]*n)
    sighash = SignatureHash(txin_scriptPubKey, tx,
                            0, SIGHASH_ALL)
    txin.scriptSig = CScript([my_private_key.sign(sighash) + bytes([SIGHASH_ALL]),
                              my_public_key])
    VerifyScript(txin.scriptSig, txin_scriptPubKey,
                 tx, 0, (SCRIPT_VERIFY_P2SH,))
    response = broadcast_transaction(tx)
    print(response.status_code, response.reason)
    print(response.text)

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    # 一共有0.01672231
    amount_to_send = 0.0005 # amount of BTC in the output you're splitting minus fee
    txid_to_spend = (
        'c74470610be4262fc3efdc16e57ef87ba4995021e4d946816386c81751695c83')
    utxo_index = 1
    # 将输入拆分为的输出数量，我选了5份，每份0.0001
    n = 5 # number of outputs to split the input into
    ######################################################################

    split_coins(amount_to_send, txid_to_spend, utxo_index, n)
