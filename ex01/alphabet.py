import random

taisyou = 10
kesson = 2
max = 2

def main():
    seikai = shutsudai()
    for i in range(max):
        kaito()
        if set(seikai) == set(kaito()):
            print("正解")
            break
        elif set(seikai) != set(kaito()):
            print("もう一度")
        elif i == max-1 and set(seikai) != set(kaito()):
            print("残念でした")

def shutsudai():
    alphabet = [chr(i + 65) for i in range(26)]
    random_alphabet = random.sample(alphabet, taisyou)
    print(f"対象文字は{random_alphabet}")
    hyouzi = random.sample(random_alphabet, taisyou-kesson)
    print(f"表示文字は{hyouzi}")

    kessonmoji = []
    for j in random_alphabet:
        if j not in hyouzi:
            kesson.append(j)

    return kessonmoji 

def kaito():
    kotae = []
    ans = input("欠損文字は何個?")
    if ans != kesson:
        print("不正解")
        return 0
    else:
        print("正解。具体的に何が欠損したか一文字ずつ入力せよ")
        for i in range(kesson):
            a = input(f"{i}個目の欠損文字")
            kotae.appned(a)
    return kotae        