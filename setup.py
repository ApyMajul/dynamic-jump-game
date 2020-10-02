# -*- coding: utf-8 -*-
# @Author: apyju
# @Date:   2018-12-24 10:10:06
# @Last Modified by:   apyju
# @Last Modified time: 2018-12-24 10:38:32
from cx_Freeze import setup, Executable

includefiles = ["n1.txt", "n2.txt", "images/background1.jpg", "images/background3.jpg", "images/background6.jpg", "images/background8.jpg", "images/background12.jpg",
                "images/codescreen.jpg", "images/effets.png", "images/hufflepuff.png", "images/kakashi2.png", "images/loadscreen.png", "images/monster.png", "images/tiles_spritesheet.png"]

setup(
    name="secretproject",
    version="0.1",
    options={'build.exe': {"includes_files": includefiles}},
    description="newgame",
    executables=[Executable("main.py", "constantes.py", "enemis.py", "levels.py", "message.py", "platforms.py", "player.py", "spritelist.py", "spritesheet.py")])


# "main.py", "constantes.py", "enemis.py", "levels.py", "message.py", "platforms.py", "player.py", "spritelist.py", "spritesheet.py"
