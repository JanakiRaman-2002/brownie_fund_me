from brownie import FundMe, config, network, accounts, MockV3Aggregator
from scripts.helpful_scripts import get_account, deploy_mocks, ACCEPTED_ENVS
from web3 import Web3




def deploy_fund_me():
    account = get_account()
    
    if network.show_active() not in ACCEPTED_ENVS:
        print("not dev")
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
        print("New Price Feed Inserted ...")
  
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account}, publish_source = config["networks"][network.show_active()].get("verify"))

    return fund_me



def main():
    deploy_fund_me()