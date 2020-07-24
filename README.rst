```
~ docker run -p 6379:6379 -d redis:5
~ python manage.py runserver 0.0.0.0:8000
~ python manage.py spam
```

Open a web browser console and run this JavaScript:

```
new WebSocket("ws://localhost:8000/ws/")
```

...and observe messages coming over the websocket in the browser console.

Hard refresh the webpage (F5, or what have you), and continue this process of
opening websocket connections after page load for a few minutes.

Watch as the memory space of the Daphne/runserver.py process grows (and never
shrinks, even when you stop publishing new messages via the spam command).
