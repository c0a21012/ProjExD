import random
import datetime

taisyou = 10    #対象文字の数
kesson = 2      #欠損文字の数
max = 2         #最大繰り返し回数

def main():
    seikai = set(shutsudai())
    for i in range(max):
        kaito()
        if seikai == kaito():
            print("正解")
            break
        elif seikai != kaito():
            print("もう一度")
        elif i == max-1 and seikai != kaito():
            print("残念でした")

def shutsudai():
    alphabet = [chr(i + 65) for i in range(26)]
    random_alphabet = random.sample(alphabet, taisyou)
    print(f"対象文字は{random_alphabet}")
    hyouzi = random.sample(random_alphabet, taisyou-kesson)         #表示文字
    print(f"表示文字は{hyouzi}")

    kessonmoji = []
    for j in random_alphabet:
        if j not in hyouzi:
            kessonmoji.append(str(j))

    return kessonmoji 

def kaito():
    kotae = []
    ans = input("欠損文字は何個?")
    if int(ans) != kesson:
        print("不正解")
    else:
        print("正解。具体的に何が欠損したか一文字ずつ入力せよ")
        for i in range(kesson):
            a = input(f"{i+1}個目の欠損文字")
            kotae.append(a)
    return set(kotae)