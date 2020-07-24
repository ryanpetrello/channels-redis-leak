```
~ docker run -p 6379:6379 -d redis:5
~ python manage.py runserver 0.0.0.0:8000
~ python manage.py spam
```

Open a web browser console and run this JavaScript several times to establish several connections:

```
new WebSocket("ws://localhost:8000/ws/")
```

...and observe "Hello, World" messages coming over the websocket in the browser console:

<img src="https://user-images.githubusercontent.com/214912/88429179-2ff39c80-cdc4-11ea-82f9-bdc1dbfdd51b.png">

Hard refresh the webpage (F5, or what have you), and continue this process of
opening websocket connections.  Do this repeatedly for a minute or two -
the goal is to open a bunch of connections while messages are flowing, then
close then in a batch w/ a page reload (over and over).

Watch as the memory space of the Daphne/runserver.py process grows (and never
shrinks, even when you stop publishing new messages via the spam command):

http://ryanpetrello.com/repro.gif
