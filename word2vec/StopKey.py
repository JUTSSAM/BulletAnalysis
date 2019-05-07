# coding=utf-8
import jieba

stop_key = [line.strip().decode('utf-8') for line in open('stopkey.txt').readlines()]


def delete(cls):
    # s = "黄色水友太秀了"
    c = jieba.cut(cls)
    return ' '.join(list(set(c) - set(stop_key)))


print delete('第七天发奖')
