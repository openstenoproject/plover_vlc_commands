
from urllib.parse import quote_plus, urljoin
import os
import json

import requests

from plover.oslayer.config import CONFIG_DIR


_VLC_CONFIG = {
    'host': 'localhost',
    'port': '8080',
    'user': '',
    'pass': 'password',
}

_vlc_config = dict(_VLC_CONFIG)
_vlc_config_path = os.path.join(CONFIG_DIR, 'vlc.json')
if os.path.exists(_vlc_config_path):
    with open(_vlc_config_path) as fp:
        _vlc_config.update(json.load(fp))

_vlc_url = 'http://%s:%s/requests/status.json' % (
    _vlc_config['host'], _vlc_config['port']
)
_vlc_auth = (_vlc_config['user'], _vlc_config['pass'])


def _vlc_request(path=''):
    url = urljoin(_vlc_url, path)
    print('_vlc_request(%r)' % url)
    r = requests.get(url, auth=_vlc_auth)
    r.raise_for_status()
    return r

def _find_playlist_id_by_name(playlist, name):
    kind = playlist['type']
    if kind == 'node':
        for child in playlist['children']:
            pid = _find_playlist_id_by_name(child, name)
            if pid is not None:
                return pid
    elif kind == 'leaf':
        if name == playlist['name']:
            return playlist['id']
    return None

# Commands. {{{

def add(engine, cmdline):
    _vlc_request('?command=in_enqueue&input=' + quote_plus(cmdline))

def clear(engine, cmdline):
    _vlc_request('?command=pl_empty')

def pause(engine, cmdline):
    _vlc_request('?command=pl_forcepause')

def play(engine, cmdline):
    request = '?command=pl_play'
    if cmdline:
        playlist = _vlc_request('playlist.json').json()
        pid = _find_playlist_id_by_name(playlist, cmdline)
        if pid is None:
            raise ValueError('no playlist item named: %r' % cmdline)
        request += '&id=' + pid
    _vlc_request(request)

def rate(engine, cmdline):
    relative, percent = False, False
    if cmdline[0] in ('-', '+'):
        relative = True
    if cmdline[-1] == '%':
        percent = True
        cmdline = cmdline[:-1]
    if relative:
        rate = round(_vlc_request().json()['rate'], 2)
        if percent:
            rate += float(cmdline) / 100 * rate
        else:
            rate += float(cmdline)
        cmdline = str(rate)
    elif percent:
        rate = float(cmdline) / 100
        cmdline = str(rate)
    _vlc_request('?command=rate&val='+cmdline)

def resume(engine, cmdline):
    _vlc_request('?command=pl_forceresume')

def seek(engine, cmdline):
    _vlc_request('?command=seek&val='+cmdline)

def stop(engine, cmdline):
    _vlc_request('?command=pl_stop')

def toggle_pause(engine, cmdline):
    _vlc_request('?command=pl_pause')

# }}}

# Metas. {{{

def timestamp(ctx, cmdline):
    status = _vlc_request().json()
    seconds = status['time']
    hours = seconds // 3600
    seconds -= hours * 3600
    minutes = seconds // 60
    seconds -= minutes * 60
    timestamp = '%02u:%02u:%02u' % (hours, minutes, seconds)
    action = ctx.new_action()
    action.text = timestamp
    return action

# }}}
