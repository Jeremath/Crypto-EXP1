# 找出可以与subarr中的值异或成可显示字符的密钥值
# subarr是在Vigenere密码中用同一密钥加密的密文
def findkey(sub_arr):
    required_chars = [chr(32), chr(33), chr(34), chr(44), chr(45), chr(46), chr(58), chr(63), chr(95)]  # 标点和空格
    for x in range(65, 91):
        required_chars.append(chr(x))  # 大写字母
    for x in range(97, 123):
        required_chars.append(chr(x))  # 小写字母
    # print(required_chars)
    all_keys = []
    res_keys = []  
    for x in range(0x00, 0xff + 1):  # 枚举当前字节处所有可能的密钥
        all_keys.append(x)
        res_keys.append(x)
    for i in all_keys:
        for s in sub_arr:
            if chr(s ^ i) not in required_chars:
                res_keys.remove(i)
                break
    return res_keys
ciphertext = "F96DE8C227A259C87EE1DA2AED57C93FE5DA36ED4EC87EF2C63AAE5B9A7EFFD673BE4ACF7BE8923C\
AB1ECE7AF2DA3DA44FCF7AE29235A24C963FF0DF3CA3599A70E5DA36BF1ECE77F8DC34BE129A6CF4D126BF\
5B9A7CFEDF3EB850D37CF0C63AA2509A76FF9227A55B9A6FE3D720A850D97AB1DD35ED5FCE6BF0D138A84C\
C931B1F121B44ECE70F6C032BD56C33FF9D320ED5CDF7AFF9226BE5BDE3FF7DD21ED56CF71F5C036A94D96\
3FF8D473A351CE3FE5DA3CB84DDB71F5C17FED51DC3FE8D732BF4D963FF3C727ED4AC87EF5DB27A451D47E\
FD9230BF47CA6BFEC12ABE4ADF72E29224A84CDF3FF5D720A459D47AF59232A35A9A7AE7D33FB85FCE7AF5\
923AA31EDB3FF7D33ABF52C33FF0D673A551D93FFCD33DA35BC831B1F43CBF1EDF67F0DF23A15B963FE5DA\
36ED68D378F4DC36BF5B9A7AFFD121B44ECE76FEDC73BE5DD27AFCD773BA5FC93FE5DA3CB859D26BB1C63C\
ED5CDF3FE2D730B84CDF3FF7DD21ED5ADF7CF0D636BE1EDB79E5D721ED57CE3FE6D320ED57D469F4DC27A8\
5A963FF3C727ED49DF3FFFDD24ED55D470E69E73AC50DE3FE5DA3ABE1EDF67F4C030A44DDF3FF5D73EA250\
C96BE3D327A84D963FE5DA32B91ED36BB1D132A31ED87AB1D021A255DF71B1C436BF479A7AF0C13AA14794"

arr = []  # 将16进制密文划分成8位2进制数
for x in range(0, len(ciphertext), 2):
    arr.append(int(ciphertext[x:2 + x], 16))

for key_length in range(2, 20):  # 密钥长度
    for class_number in range(0, key_length):  # 密文划分成key_length类，每一类和同一密钥值异或
        sub_arr = arr[class_number::key_length]  # 分割出同一组的密文
        res_keys = findkey(sub_arr)
        print('key_length= ', key_length, 'class_number= ', class_number, 'keys= ', res_keys)
        if len(res_keys) > 1:  # 如果有多个可能的密钥值，查看具体明文情况进行选择
            for x in res_keys:
                print(x)
                for s in sub_arr:
                    print(chr(s ^ x), end='')
                print("\n")
key1=[186,29,145,178,83,205,62]
key2=[186,31,145,178,83,205,62]
plaintext1=""
plaintext2=""
for x in range(0,len(arr)):
    plaintext1+=chr(arr[x]^key1[x%7])

    plaintext2+=chr(arr[x]^key2[x%7])
print('key1的明文=',plaintext1)
print("\n")
print('key2的明文=',plaintext2)