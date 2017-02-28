# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 18:42:42 2017

@author: elara
"""

import pandas as pd
import numpy as np

pa = 0.7
pga = 0.9
pya = 1 - pga
pb = 0.3
pgb = 0.3
pyb = 1 - pgb

pby = pyb * pb / (pyb * pb + pya * pa);pby # 0.75
pbg = pgb * pb / (pgb * pb + pga * pa);pbg # 0.125
pay = pya * pa / (pya * pa + pyb * pb);pay # 0.25
pag = pga * pa / (pga * pa + pgb * pb);pag # 0.875

# (a)
# pby > pay, 所以黄色判为香蕉
# pag > pbg, 所以绿色判为苹果

# (b)
# 黄色输入，正确率 75%， 绿色输入，正确率 87.5%。总正确率加权平均

# (c)
# 500 香蕉， 70% 黄色（350个黄色香蕉），150个绿色香蕉
500* 0.7
# 500苹果， 90% 绿色（450个绿色苹果）， 50个黄色苹果
500* 0.9
# 黄色水果400个，绿色水果600个
0.6 * 0.875 + 0.4 * 0.75 # 0.825 预期正确率
# 预期错误个数
1000 -( 600 * 0.875 + 400 * 0.75 ) # 175个

#(d)
 
