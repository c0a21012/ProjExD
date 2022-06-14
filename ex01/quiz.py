import random
def main():
    seikai = syutudai()
    kaito(seikai) 
def syutudai():
    mondai = [{"q":"サザエの旦那の名前は？","a":["マスオ", "ますお"]}, 
              {"q":"カツオの妹の名前は？", "a":["ワカメ", "わかめ"]}, 
              {"q":"タラオから見てカツオはどんな関係？", "a":["甥っ子", "おいっこ", "甥", "おい"]}]
    ransu = random.randint(0,2)
    print("問題")
    print(mondai[ransu]["q"])
    return mondai[ransu]["a"]

def kaito(seikai):
    ans = input("回答")
    if ans in seikai:
        print("正解")
    else:
        print("不正解")
