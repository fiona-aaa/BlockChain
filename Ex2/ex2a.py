from sys import exit
from bitcoin.core.script import *

from Ex1.utils import *
from Ex1.config import my_private_key, my_public_key, my_address, faucet_address
from Ex1.ex1 import send_from_P2PKH_transaction
"""
少一个包CBitcoinSecret
"""
from bitcoin.wallet import CBitcoinSecret

# 三个客户的私钥和生成的公钥
cust1_private_key = CBitcoinSecret(
    'cVZHPdsDGGd9Wmry1ZfM4vjY32v11GR6E4wsfSp2eWRGTWYZkLXn')
cust1_public_key = cust1_private_key.pub

cust2_private_key = CBitcoinSecret(
    'cT6L7ZvQS9vW68psjxpHe4VBThbrjWFNpVR3Mhe969E5zR9LiNJ8')
cust2_public_key = cust2_private_key.pub

cust3_private_key = CBitcoinSecret(
    'cVGGcfbchQ6aUmzq4NTHzjvnC7t6vmVovG1uU85rT8uuwiUr7d8u')
cust3_public_key = cust3_private_key.pub


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 2

# You can assume the role of the bank for the purposes of this problem
# and use my_public_key and my_private_key in lieu of bank_public_key and
# bank_private_key.
"""
我是银行
"""
# 我（bank）的私钥
bank_private_key = CBitcoinSecret('cQvAwbiURvrbjaVHVyNMiyWQgUvHwMcdgTitsKvcJMYUZkNUZjnc')

# 我（bank）的公钥
bank_public_key = bank_private_key.pub

ex2a_txout_scriptPubKey = [bank_public_key, #银行公钥
OP_CHECKSIGVERIFY,
OP_1,
cust1_public_key,# cust1公钥
cust2_public_key,# cust2公钥
cust3_public_key,# cust3公钥
OP_3,
OP_CHECKMULTISIG
]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00008 #平均每份0.0001
    txid_to_spend = (
        '8e087aa8922a1c27e5623f47bffb679e93a83c9044a7771c3fb262769ade8333')
    # 在ex1中，我把bitcoin分了5份，ex1用了第0份，现在用第1份
    utxo_index = 1
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        ex2a_txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text)
