#!/usr/bin/env python
# -*- coding=utf-8 -*-

# @author: adbibo
# @contact: laoliu.yin@gmail.com
# @file: block_chain.py
# @time: 2018/7/17 下午4:09
# @desc: 区块链示例

import datetime as date
import hashlib as hasher


# 构造一个block结构 得到一个哈希值
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        data = (str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode("utf8")
        sha.update(data)
        return sha.hexdigest()


def create_genesis_block():
    return Block(0, date.datetime.now(), "Genesis Block", "0")


def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "hey! I'm block" + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)


blockchain = [create_genesis_block()]
previous_block = blockchain[0]

num_of_blocks_to_add = 20

for i in range(0, num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add

    print("Block #{} has been added to the block chain!".format(block_to_add.index))
    print("Hash: {}n".format(block_to_add.hash))
