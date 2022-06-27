import hashlib

def md5_hash(Any_String):
        return str(hashlib.md5(str(Any_String).encode('utf8')).hexdigest())