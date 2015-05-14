__author__ = 'jmagady'

import libtorrent as lt

from app import lt, lses
from app.config import params, tempdir
from time import sleep


def magnet2tor(magnet):
    handle = lt.add_magnet_uri(lses, magnet, params)
    count = 0
    while not handle.has_metadata():
        status = handle.status()
        if status.active_time > 600:
            count += 1
            lses.remove_torrent(handle)
            handle = lt.add_magnet_uri(lses, magnet, params)
        if count > 2:
            lses.remove_torrent(handle)
            return False
    handle.pause()
    return handle

def tor2rawfile(torhandle):
    if torhandle.has_metadata():
        torinfo = torhandle.get_torrent_info()
        filelist = []
        for f in torinfo.files():
            fsplit = f.path.split('//')
            filelist.append(fsplit[-1])
    return filelist
