# 以下の関数にGoogleスタイルのdocstringを追加してください。docstringには、
# 少なくとも関数の処理内容、引数、
# 戻り値について記述してください。

def km_to_miles(km):
    """Add your docstring here."""
    miles = km * 0.6
    return miles

print(km_to_miles.__doc__)
