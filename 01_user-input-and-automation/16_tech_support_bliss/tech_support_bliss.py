# 組み込みの「platform」モジュールを使って以下の情報を出力します。

placeholder = "remove me :)"
 
print(f"{'Platform:':>10} {placeholder}",)  # platform.platform()
print(f"{'Compiler:':>10} {placeholder}",)  # platform.python_compiler()
print(f"{'Python:':>10} {placeholder}",)  # platform.python_version()
print(f"{'System:':>10} {placeholder}",)  # platform.system()
print(f"{'Release:':>10} {placeholder}",)  # platform.release()
print(f"{'System:':>10} {placeholder}",)  # platform.processor()