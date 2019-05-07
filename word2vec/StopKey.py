# coding=utf-8
import jieba


def delete(cls):
    c = jieba.cut(cls)
    return ' '.join(list(set(c) - set(stop_key)))


stop_key = [line.strip().decode('utf-8') for line in open('stopkey.txt').readlines()]
document = [line.strip().decode('utf-8') for line in open('Output/participle_result.txt').readlines()]

print "=== [ Start deleting stop keys. ] ==="

for item in document:
    print item + " => " + delete(item)
    # 删除停用词
    result = delete(item)
    # 删除首尾空格
    result = result.strip()
    # 跳过空字符串
    if len(result) == 0:
        continue
    result = result + '\n'
    with open('Output/stop_key_result.txt', 'a') as f:
        f.write(result.encode('utf-8'))
f.close()

print "=== [ Deleting success ] ==="
