#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."


def install():
    pisitools.insinto("/opt/hipchat", "hipchat/HipChat4/*")
    pisitools.insinto("/usr/share/icons/hicolor", "hipchat/icons/hicolor/*")
    pisitools.dosym("/opt/hipchat/bin/HipChat4", "/usr/bin/hipchat")
