# coding=utf-8
import jieba.posseg as psg

if __name__ == '__main__':
    sent = "中文分词"
    seg_list = psg.cut(sent)
    print(u' '.join(['{0}/{1}'.format(w, t) for w, t in seg_list]).encode('utf-8').strip())
