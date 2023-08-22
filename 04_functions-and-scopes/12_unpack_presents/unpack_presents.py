# 指定された辞書を入力として、以下に定義された関数を
# 呼び出すにはどうすればよいでしょうか。
# 明示的にdictの値にアクセスするのではなく、
# 引数を渡す際に辞書のアンパックを使用してください。

def congratulate(name, age):
    return f"Today {name} is {age} years old.\nHappy Birthday!"

user = {"name":"Adelheid", "age":22}
