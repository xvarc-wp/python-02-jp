# 空腹度メーターは現在、文字列入力しか正確に扱えません。
# 最初の`if`文を型チェックにしてください。
# `hunger`の値が`str`型でない場合、
# 空腹度を文字列で宣言するように
# 注意するメッセージを出力します。


hunger = 2

if hunger == "big":
    print("Eat the pizza")
elif hunger == "small":
    print("Eat the apple")
else:
    print("Don't eat anything")
