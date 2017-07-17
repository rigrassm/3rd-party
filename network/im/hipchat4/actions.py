#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."


def install():
    pisitools.insinto("/opt/hipchat", "hipchat4-4.29.4.1662/HipChat4/*")
    pisitools.insinto("/usr/share/icons/hicolor", "hipchat4-4.29.4.1662/icons/hicolor/*")
    pisitools.dosym("/opt/hipchat/bin/HipChat4", "/usr/bin/hipchat")
