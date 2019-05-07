# encoding=utf-8
import jieba.analyse

if __name__ == '__main__':
    with open('../BulletOutput/douyu/606118') as f:
        document = f.read()
        document_cut = jieba.cut(document)

        # 原始单纯分词版本
        result = ' '.join(document_cut)

        result = result.encode('utf-8')
        print result
        with open('Output/participle_result.txt', 'a') as f2:
            f2.write(result)
    f.close()
    f2.close()
    print "=== write success ==="
