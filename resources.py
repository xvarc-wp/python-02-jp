# このコードスニペットは、1から100までのランダムな数字を含む
# ランダムな長さのリストを生成します。
# これを使用して、他のラボで使用するランダムリストを簡単に生成できます。
# 別のスクリプトファイルで使用するには、
# 次のコマンドを使って「starter」リストからインポートできます
#
# from randlist import starter
#
# ラボで使ってみてください。
# P.S.:ここで行うことは他に何もありません。

import random

list_length = random.randint(1, 20)
randlist = list()
for i in range(list_length):
    randlist.append(random.randint(1, 100))
