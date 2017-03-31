
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
    r = requests.get(_vlc_url + path, auth=_vlc_auth)
    r.raise_for_status()
    return r

# Commands. {{{

def pause(engine, cmdline):
    _vlc_request('?command=pl_forcepause')
    return ''

def resume(engine, cmdline):
    _vlc_request('?command=pl_forceresume')
    return ''

def seek(engine, cmdline):
    _vlc_request('?command=seek&val='+cmdline)
    return ''

def stop(engine, cmdline):
    _vlc_request('?command=pl_stop')
    return ''

def toggle_pause(engine, cmdline):
    _vlc_request('?command=pl_pause')
    return ''

# }}}

# Metas. {{{

def timestamp(ctx, cmdline):
    r = _vlc_request()
    seconds = r.json()['time']
    hours = seconds // 3600
    seconds -= hours * 3600
    minutes = seconds // 60
    seconds -= minutes * 60
    timestamp = '%02u:%02u:%02u' % (hours, minutes, seconds)
    action = ctx.new_action()
    action.text = timestamp
    return action

# }}}
