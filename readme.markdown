iTunes Remote
------
This is like the Remote app in the App Store, except it is a webapp.

Listening to music helps me drift off to sleep at night. Resting my head against a pillow with earphones in is uncomfortable, so I prefer to listein to music playing through my speakers. Unfortunately, turning those speakers off right before I fall asleep requires me to get out of bed and walk across the room, and the resulting physical exertion invovled shakes me out of my half sleep like state.

Since I usually have either or both my iPhone or iPad in bed with me, my solution was to build a webapp that allows me to control iTunes from a simple webapp. Of course I could have just used the Apple's official Remote app, but that would have been less fun.

I'm also thinking of hooking up a Raspberry Pi up to my speakers in the future. I envision an iTunes-like webapp as the interface for controlling the Raspberry Pi's audio output. This project will eventually evolve into that iTunes-like webapp.

Installation
------
`git clone blahblahbalh`  
`cd blah blah blah`  
`virtualenv --distribute venv` (optional)  
`pip install -r requirements.txt`  

Running
-----
`python server.py`  
Point your browser to http://[server's ip address']:5000
