import hashlib
import itertools
import datetime

# 目标哈希和字符集
hash1 = "67ae1a64661ac8b4494666f58c4822408dd0a3e4"
char_sets = [['Q', 'q'], ['W', 'w'], ['%', '5'], ['8', '('], ['=', '0'], ['I', 'i'], ['*', '+'], ['n', 'N']]

def sha_encrypt(s):
    hash_object = hashlib.sha1(s.encode('utf-8'))
    return hash_object.hexdigest()

# 开始计时
starttime = datetime.datetime.now()

# 生成所有可能的字符组合
for combination in itertools.product(*char_sets):
    # 对当前组合生成所有排列
    for perm in itertools.permutations(combination):
        candidate = "".join(perm)
        if sha_encrypt(candidate) == hash1:
            print("密码:", candidate)
            endtime = datetime.datetime.now()
            print("时间:", (endtime - starttime).seconds, "秒")
            exit()
