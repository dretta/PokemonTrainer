import streamlink
import subprocess
import requests


def getLiveStreamImages():
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


def getVideo(url, length):
    subprocess.run(['streamlink', url, 'best', '-O', '|', 'ffmpeg', '-i', 'pipe:0', '-t', length, 'battle.ts'])

def getNFrames(n):
    subprocess.run(['ffmpeg', '-i', 'battle.ts', '-vf', 'select=not(mod(n\,{}))'.format(n), '-vsync', 'vfr', '-q:v',
                    '2', 'img_%03d.jpg'])