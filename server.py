from flask import Flask
from fabric import api
from flask import render_template
app = Flask(__name__)

class AbstractMediaPlayer(object):
    def play(self):
        raise NotImplementedError
    def pause(self):
        raise NotImplementedError
    def next_track(self):
        raise NotImplementedError
    def prev_track(self):
        raise NotImplementedError
    def vol_up(self):
        raise NotImplementedError
    def vol_down(self):
        raise NotImplementedError
    
class ITunesPlayer(AbstractMediaPlayer):
    def _exec_osascript(self, script):
        api.local("osascript -e '%s'" % script)

    def play(self):
        self._exec_osascript('tell app "itunes" to play')
        return 'success'
    def pause(self):
        self._exec_osascript('tell app "itunes" to pause')
        return 'success'
    def next_track(self):
        self._exec_osascript('tell app "itunes" to next track')
        return 'success'
    def prev_track(self):
        self._exec_osascript('tell app "itunes" to previous track')
        return 'success'

media_player = ITunesPlayer()

@app.route('/', methods=['GET'])
def main_page():
    return render_template('main.html')
@app.route('/play', methods=['POST'])
def play():
    media_player.play()
    return ''

@app.route('/pause', methods=['POST'])
def pause():
    media_player.pause()
    return ''

@app.route('/next_track', methods=['POST'])
def next_track():
    media_player.next_track()
    return ''

@app.route('/prev_track', methods=['POST'])
def prev_track():
    media_player.prev_track()
    return ''

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
