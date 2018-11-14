# 文本制作 
1. 从 resources.assets 的 ID-13236 中导出 dat 原始文件，执行 stringbank.de.py 生成 13236.de.csv 文件。
2. 由于是要导入到日文文本当中，所以 13236.de.csv 文件改名为 13240.csv，并把文件内的 script_name 从 en 改为 jp，这之后就可以开始翻译了。
3. 翻译完后执行 stringbank.se.py 生成 13240.se.dat 导入回 resources.assets 的 ID-13240 即可。

# 字库制作
1. 从 sharedassets0.assets 的 ID-25 中导出 dat 原始文件。
2. 利用自己程序的 UnityFont 类生成新的 dat 文件后导回即可。

# 图片制作 