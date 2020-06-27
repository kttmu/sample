import os
import sys
import pathlib

for i in range(3):
    os.chdir("./" + str(i+1))

    for j in range(100):
        file_ = pathlib.Path("./test_" + str(j+1) +".txt")
        file_.touch()

    os.chdir("../")


