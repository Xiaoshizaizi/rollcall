import re
import random
import time

def main():
    print('\n正在抽取幸运儿......\n')
    try:
        with open('../student.txt','r',encoding='utf-8') as f:
            text = f.read()
    except:
        print('当前目录没找到student.txt')
    par = '[\u4e00-\u9fa5]+'
    s_list = re.findall(par,text)
    count = len(s_list)
    num = random.randint(1,count)
    time.sleep(2)
    print('-----------------------------\n')
    print('恭喜 %s 同学\n' %s_list[num-1])
    print('-----------------------------\n')
    input('如需继续抽取幸运同学，请按回车：')
    main()
    
main()