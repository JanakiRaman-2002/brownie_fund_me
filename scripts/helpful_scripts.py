from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3


DECIMAL = 8
INTIAL_VAL = 200000000000

FORKED_LOCAL = ["mainnet-fork", "mainnet-fork-dev"]
ACCEPTED_ENVS = ["development", "ganache-local", "ganache--local"]

def get_account():
    if network.show_active() in ACCEPTED_ENVS or network.show_active() in FORKED_LOCAL:
        return accounts[0]
    
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    print("The active network is  development")
    print("Deploying mocks ...")
    if len(MockV3Aggregator)<=0:
            MockV3Aggregator.deploy(DECIMAL, INTIAL_VAL ,{"from": get_account()})
            print("Mocks deployed !")
            
