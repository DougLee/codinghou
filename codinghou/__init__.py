# -*- coding: utf-8 -*-
"""
 @Date    : 2021/2/3 21:51
 @Author  : Douglee
"""
from pyfiglet import Figlet, FigletFont
import random


greetings = [
    '愿你在新的一年里，学习进步，成绩优异！',
    '新年新开始，愿你所有的梦想都能在新的一年里实现！',
    '新年快乐！愿你在新的一年里，变得更有趣，获得更多的关注！不过要记住，学习永远是第一位的！',
    '新的一年，新的开始，愿你拥有无限的能量和活力，让周围的人都炸掉！',
    '新年新气象，愿你心想事成，万事如意，让敌人都嫉妒得要命！',
    '祝你新年学习进步，成绩优异！再没有像你这么厉害的小学生了！',
    '愿你在新的一年里，成为学校里最帅/美的学生！虽然我知道这是不可能的，但还是祝你好运！',
    '新年新开始，愿你的梦想在新的一年里都能实现！当然，如果你的梦想是成为世界最强大超级英雄，那可能有点难度。',
    '愿你在新的一年里，健康快乐，获得更多的成就！当然，如果你能在新的一年里变成外星人，那就更好了！',
    '愿你在新的一年里，与同学们相处融洽，老师指导有方！不过，如果你能在新的一年里成为老师的宠儿，那就真的太棒了！',
    '祝你新年学习进步，成绩优异！也许你会成为下一个诺贝尔奖得主呢！',
    '愿你在新的一年里，成为学校里最帅/美的学生！哇，你真的长大了！',
    '新年新开始，愿你的梦想在新的一年里都能实现！虽然我知道你的梦想是当一个超级英雄，但是，你知道吗？现在的超级英雄都是用科技武器的。',
    '愿你在新的一年里，健康快乐，获得更多的成就！当然，如果你能在新的一年编程更厉害，那就更好了！虽然你已经是我们心目中很厉害的小小程序员了！'
]


def greeting():
    greet = random.choice(greetings)
    print(greet)


def default(font="larry3d"):
    f = Figlet(font=font, width=200)
    print(f.renderText('CODINGHOU'))
    print(f.renderText('Happy New Year'))


def get_fonts():
    """
    show all fonts
    :return:
    """
    all_fonts = FigletFont().getFonts()
    return all_fonts


default()
greeting()