__author__ = 'jmagady'

from requests import get
from urllib import urlencode
from config import trackers
import bencode
import hashlib
import itertools


def torrent2meta(torurl):
    try:
        return bencode.bdecode(get(torurl).content)
    except bencode.BTFailure:
        return False


def meta2magnet(metadata):
    hashcontent = bencode.bencode(metadata['info'])
    digest = hashlib.sha1(hashcontent).hexdigest()

    params = {'dn': metadata['info']['name'],
              'tr': trackers}
    paramstr = urlencode(params, doseq=True)
    return 'magnet:?xt=urn:btih:{hash}&{param}'.format(hash=digest,param=paramstr)

def meta2files(metadata):
    if 'files' in metadata['info'].keys():
        return itertools.chain(*(f["path"] for f in metadata["info"]["files"]))
    else:
        return [metadata['info']['name']]