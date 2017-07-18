#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."


def install():
    icon_sizes = [
            "16x16", 
            "24x24", 
            "32x32", 
            "48x48",
            "128x128",
            "256x256", 
            "512x512",
            "1024x1024",
            ]
    pisitools.insinto("/opt/hipchat", "hipchat4-4.29.4.1662/HipChat4/*")
    for i in icon_sizes:
        pisitools.domove(
                "hipchat4-4.29.4.1662/icons/hicolor/" + i + "/apps/*", 
                "/usr/share/icons/hicolor/" + i + "/apps/"
                )
    pisitools.dosym("/opt/hipchat/bin/HipChat4", "/usr/bin/hipchat")
