iTunes Remote
------
This is like the Remote app in the App Store, except it is a
webapp. It allows you to control iTunes on your macbook/iMac from
another computer's browser. I use it to control my laptop's audio
output from my phone or tablet.

Why not just use the Remote app? In the future, I'd like hook up my
home theater to, say, a Raspberry Pi. An iTunes-like web
interface that is accessbile from all my devices (smartphone, tablet,
laptop) for playing music and videos would be amazing. This project will
eventually morph into that system.

Installation
------
`git clone git@github.com:dvdt/home-theater-remote.git`  
`cd home-theater-remote`  
`virtualenv --distribute venv` (optional)  
`pip install -r requirements.txt`  

Running
-----
`python server.py`  
Point your tablet's browser to http://<server's-ip-address>:5000
