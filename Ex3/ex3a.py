from sys import exit
from bitcoin.core.script import *

from Ex1.utils import *
from Ex1.config import my_private_key, my_public_key, my_address, faucet_address
from Ex1.ex1 import send_from_P2PKH_transaction


######################################################################
#  Complete the scriptPubKey implementation for Exercise 3
"""
studentID 2012679 ----- 2012 678（调整最后一位保证奇偶性相同）
x + y = 2012
x - y = 678
得：x = 1345 y = 667
scriptSig 提供两个整数x y，压入栈
因为要进行加、减两个运算，所以先使用OP_2DUP将x y复制一遍
OP_ADD ： 将复制得到的x y相加
2012：我学号的前四位
OP_EQUALVERIFY：比较x + y是否等于2012
OP_SUB：计算x - y
678：学号后三位，为了保持奇偶性相同，我将最后一位减一
OP_EQUAL：比较x - y是否与678相等，如果相等，则证明x和y是正确的解
"""

ex3a_txout_scriptPubKey = [OP_2DUP, OP_ADD, 2012, OP_EQUALVERIFY, OP_SUB, 678, OP_EQUAL]

######################################################################

if __name__ == '__main__':
    ######################################################################
    # set these parameters correctly
    # 平均每份0.0001 小费0.00001
    amount_to_send = 0.00009
    txid_to_spend = (
        '8e087aa8922a1c27e5623f47bffb679e93a83c9044a7771c3fb262769ade8333')
    # 在ex1中，我把bitcoin分了5份，ex1用了第0份，ex2用了第1份，现在用第2份
    utxo_index = 2
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        ex3a_txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text)
