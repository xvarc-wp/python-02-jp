# 目を覚ますと`if`文の迷路の中にいました。脱出するための道を
# 探さなければなりません。
#
# .--.--.--.  .--.--.
# |     |        |  |
# :  :--:  :  :  :  :
# |  |     |  |     |
# :  :  :  :--:--:--:
# |  |  |           |
# :  :  :--:--:--:  :
# |  |  自分  |  |  |
# :  :--:--:  :  :  :
# |     |     |  |  |
# :--:  :  :--:  :  :
# |        |        |
# :--:--:--:--:--:--:
#
# しかし、この迷路には大きな制約があります。
# できることは2つだけで、以下のコード行のどちらかを
# 追加することしかできません。
#
#     flag = True
#     flag = False
#
# 何回でも追加できますが、既にあるコードは
# 変更できません。
#
# コードを追加して、迷路から脱出するために必要なすべてのステップ
# (left: 左、straight ahead: 直進、right: 右、DEAD END: 行き止まり)を出力してください。
# 常に北を向いていて、見ている方向は変わらず
# 横歩きするものとします。

flag = True

if flag == True:
    print("left")

if flag == False:
    print("straight ahead")

if flag == True:
    print("left")

if flag == False:
    print("straight ahead")

if flag == True:
    print("straight ahead")

if flag == True:
    print("straight ahead")

if flag == True:
    print("DEAD END")

if flag == True:
    print("left")

if flag == False:
    print("right")

if flag == True:
    print("straight ahead")

if flag == False:
    print("straight ahead")

if flag == False:
    print("DEAD END")

if flag == True:
    print("right")

if flag == True:
    print("straight ahead")

if flag == True:
    print("left")

if flag == False:
    print("EXIT!!")

if flag == True:
    print("DEAD END")
