key2='66396e89c9dbd8cc9874352acd6395102eafce78aa7fed08a07f6bc98d29c50b69b0339a19f8aa401a9c6d708f80c066c763fef0123148cdd8e802d05ba98777335daefcecd59c433a6b268b60bf4ef03c9a61'
ciphertext='32510ba9babebbbefd001547a810e67149caee11d945cd7fc81a05e9f85aac650e9052ba6a8cd8257bf14d13e6f0a803b54fde9e77472dbff89d71b57bddef121336cb85ccb8f3315f4b52e301d16e9f52f904'
key1='66396e89c9dbd8cb9874352acd63da102eaf0078aa7fed28a06e6bc98d29c50b69b033db14f8aa401a9c6d708f80c066c763fef0123148cd00e802d05ba98777335daefcecd59c433a6b268b60bf4ef03c9a611098bb009a3161edc70004a3'
#流加密求明文
def xor(a,b):
    return bytes([i^j for i,j in zip(a,b)])
plaintext1=xor(bytes.fromhex(key1),bytes.fromhex(ciphertext))
print(plaintext1)
plaintext2=xor(bytes.fromhex(key2),bytes.fromhex(ciphertext))
print(plaintext2)