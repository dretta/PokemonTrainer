# -*- coding: utf-8 -*-
from pokemontrainer import helpers


import streamlink
import subprocess
import requests

if __name__ == "__main__":
    streams = streamlink.streams("http://twitch.tv/twitchplayspokemon")
    stream = streams["worst"]
    fd = stream.open()
    url = fd.writer.stream.url
    fd.close()
    res = requests.get(url)
    tsFiles = list(filter(lambda line: line.startswith('http'), res.text.splitlines()))
    print(tsFiles)
    for i, ts in enumerate(tsFiles):
        vid = 'vid{}.ts'.format(i)
        subprocess.run(['curl', ts, '-o', vid])
        subprocess.run(['ffmpeg', '-i', vid, '-vf', 'fps=1', 'out{}_%d.png'.format(i)])