import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transcations = []

        #create the genesis block
        self.new_block(previous_hash=1 , proof=100)

    def new_block(self, proof , previous_hash=None):
        '''
        Create a new block in the Blockchain
        '''
        block = {
            'index':len(self.chain) + 1,
            'timestamp':time(),
            'transaction':self.current_transactions,
            'proof':proof,
            'previous_hash':previous_hash or self.hash(self.chain[-1])
        }

        self.current_transcations=[]

        self.chain.append(block)

        return block

    def new_transaction(self,sender,recipient,amount):
        '''
        Creates a new transaction to go into the next mined block
        '''
        self.current_transcations.append({
            'sender':sender,
            'recipient':recipient,
            'amount':amount,
        })

        return self.last_block['index'] + 1
        

    @staticmethod
    def hash(block):
        '''
        Creates SHA-256 hash of a Block
        '''
        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_string = json.dumps(block , sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]