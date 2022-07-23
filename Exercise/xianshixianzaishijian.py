#显示现在的时间

import time
for i in range(1):
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))