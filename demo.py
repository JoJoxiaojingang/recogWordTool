import keyboard
from PIL import ImageGrab
import time
import json
import pyperclip
from aip import AipOcr
""" 你的 APPID AK SK """
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


while 1:
    array=[]
    keyboard.wait(hotkey='ctrl+shift+s')
    time.sleep(7)
    # print('11111')
    # 保存图片到电脑上
    image=ImageGrab.grabclipboard() # 从剪切板里获取图片
    image.save('001.jpg')
    """ 读取文件 """
    def get_file_content(filePath):
        with open(filePath, "rb") as fp:
            return fp.read()
    image = get_file_content('001.jpg')
    # 调用通用文字识别（高精度版）
    res_image = client.basicAccurate(image)
    filePath="ai_count.json"
    # 读
    with open(filePath,mode='r',encoding='utf-8') as f:
        data=f.read()
    # 操作
    data=int(data)-1
    # 写
    with open(filePath,mode='w',encoding='utf-8') as f:
        json.dump(data,f)
    print("$"*64)
    print(f"次数还剩{data}次")
    print("$"*64)
    # print (res_image)
    num=len(res_image['words_result'])
    for item in res_image['words_result']:
        array.append(item.get('words'))
        
        
        # print (item.get('words'))
    strMy="\n".join(array)
    pyperclip.copy(strMy)
    print(strMy)
    print("="*64)
