# 文本制作 
1. 从resources.assets的ID-261中导出dat原始文件，执行stringbank.de.py生成261.de.csv文件。
2. 由于是要导入到日文文本当中，所以261.de.csv文件改名为266.csv，并把文件内的script_name从en改为jp，这之后就可以开始翻译了。
3. 翻译完后执行stringbank.se.py生成 266.se.dat 导回resources.assets中的ID-266即可。

# 字库制作
1. 从sharedassets0.assets的ID-24中导出dat原始文件。
2. 利用自己程序的UnityFont类生成新的dat文件后导回即可。

# 图片制作 
1. 直接利用工具导入以及导出即可，需注意不要开启Mipmap选项，具体文件编码已写在文件名中。