from bitcoin import SelectParams
from bitcoin.base58 import decode
from bitcoin.wallet import CBitcoinAddress, CBitcoinSecret, P2PKHBitcoinAddress


SelectParams('testnet')

# TODO: Fill this in with your private key.
# 私钥
my_private_key = CBitcoinSecret(
 'cQvAwbiURvrbjaVHVyNMiyWQgUvHwMcdgTitsKvcJMYUZkNUZjnc')
"""
2022/10/19
为了做ex2，重新申请了密钥，如下
还是用的第一次实验的密钥，因为我第一次生成了五份，ex1用了第0个，ex2我用的第二个
my_private_key = CBitcoinSecret('cUxDQ1ee6T9v58D5NVwURNsYT5iX6thnrHYDTw8feAxCodsntgD1')
"""
my_public_key = my_private_key.pub
my_address = P2PKHBitcoinAddress.from_pubkey(my_public_key)

faucet_address = CBitcoinAddress('mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB')
