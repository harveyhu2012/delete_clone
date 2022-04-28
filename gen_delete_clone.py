#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
from xml.dom.minidom import parse
import xml.dom.minidom
 
# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse("FinalBurn Neo (ClrMame Pro XML, Arcade only).dat")
collection = DOMTree.documentElement
 
# 在集合中获取所有游戏
games = collection.getElementsByTagName("game")

f = open("delete_clone.bat","w")

if f:
    # 只要是克隆的游戏，del
    for game in games:
       if game.hasAttribute("cloneof"):
          f.write("del %s.zip\n" %(game.getAttribute("name")) )
    f.close()