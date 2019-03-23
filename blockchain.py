import hashlib
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        #genesis block 생성
        self.new_block(previous_hash = 1)
        
    def new_block(self, previous_hash, nonce, difficulty, merkleroot):
        block = {
            'index' : len(self.chain) + 1,
            'timestamp' : time(),
            'transactions' : self.current_transactions,
            'previous_hash' : previous_hash or self.hash(self.chain[-1]),
            'nonce' : nonce,
            'difficulty' : difficulty, #난이도
            'merkleroot' : merkleroot,
        }

        self.current_transactions = []

        self.chain.append(block)
        return block
    
    def new_transaction(self, number, user, checkpoint, time, pass_fail):
        
        self.current_transactions.append({
            'number' : number,          #인덱스번호
            'user': user,               #user = 출입자
            'checkpoint' : checkpoint,  #checkpoint = 보안장치(문)
            'time' : time(),            #time = 출입시도 시각
            'pass_fail' : pass_fail,    #pass_fail = 출입여부
        })

        return self.last_block['index'] + 1
    
    def hash(block):
        block_string = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(block_string).hexdigest

    def last_block(self):
        return self.chain[-1]
