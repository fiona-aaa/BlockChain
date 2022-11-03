from sys import exit
from bitcoin.core.script import *

from Ex1.utils import *
from Ex1.config import my_private_key, my_public_key, my_address, faucet_address
from Ex1.ex1 import P2PKH_scriptPubKey
from ex3a import ex3a_txout_scriptPubKey

######################################################################
# set these parameters correctly
# ex3a.py 是 amount_to_send = 0.00009，这里要比它少一点
amount_to_send = 0.00008
txid_to_spend = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
utxo_index = 0
######################################################################

txin_scriptPubKey = ex3a_txout_scriptPubKey
######################################################################
# implement the scriptSig for redeeming the transaction created
# in  Exercise 3a.
# 一个有效的 scriptSig 应该是简单地将两个整数 x 和 y 发送到堆栈中。
txin_scriptSig = [1345, 667]
######################################################################
txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)

response = send_from_custom_transaction(
    amount_to_send, txid_to_spend, utxo_index,
    txin_scriptPubKey, txin_scriptSig, txout_scriptPubKey)
print(response.status_code, response.reason)
print(response.text)
