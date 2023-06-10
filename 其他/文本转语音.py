# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/9/21 20:54
# @Author : south(南风)
# @File : 文本转语音.py
# Describe: 利用工具将文本转化为语音读取
# -*- coding: utf-8 -*-
import pyttsx3


def use_pyttsx3():
    # 创建对象
    engine = pyttsx3.init()

    # 获取当前语音速率
    # rate = engine.getProperty('rate')
    # print(f'语音速率：{rate}')
    # 设置新的语音速率
    engine.setProperty('rate', 130)
    # rate = engine.getProperty('rate')
    # print(f'更改后的语音速率：{rate}')

    # 获取当前语音音量
    # volume = engine.getProperty('volume')
    # print(f'语音音量：{volume}')
    # 设置新的语音音量，音量最小为 0，最大为 1
    engine.setProperty('volume', 0.5)

    # 获取当前语音声音的详细信息  # 这里我也是找到的实例代码感觉写的很矛盾，最后发出的还是女声
    voices = engine.getProperty('voices')
    # print(f'语音声音详细信息：{voices}')
    # 设置当前语音声音为女性，当前声音不能读中文
    # engine.setProperty('voice', voices[1].id)
    # 设置当前语音声音为男性，当前声音可以读中文
    engine.setProperty('voice', voices[0].id)
    # 获取当前语音声音
    voice = engine.getProperty('voice')
    # print(f'语音声音：{voice}')

    # 语音文本
    # words = input('请输入要说的话：')
    # 将语音文本说出来
    with open("1.txt", 'r', encoding='utf-8') as f:
        words = f.read()
    # engine.say(words)
    engine.runAndWait()
    engine.stop()

    # 保存音频
    engine.save_to_file(words, filename='test.mp3')
    engine.runAndWait()


if __name__ == '__main__':
    use_pyttsx3()






