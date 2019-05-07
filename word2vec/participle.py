# encoding=utf-8
import jieba.analyse

stop_key = [line.strip().decode('utf-8') for line in open('stopkey.txt').readlines()]


def delete_stop_key(cls):
    c = jieba.cut(cls)
    return ' '.join(list(set(c) - set(stop_key)))


if __name__ == '__main__':
    with open('../BulletOutput/douyu/606118') as f:
        document = f.read()
        
        # 原始单纯分词版本
        # document_cut = jieba.cut(document)
        # result = ' '.join(document_cut)
       
        # 删除停用词
        result = delete_stop_key(document)
        # result = result.encode('utf-8')

        print result
        with open('Participle/output.txt', 'a') as f2:
            f2.write(result)
    f.close()
    f2.close()
    print "=== write success ==="
