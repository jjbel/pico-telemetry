Following
https://www.donskytech.com/using-websocket-in-micropython-a-practical-example/  

---

1. `boot.py` logs in to wifi after booting

2. `main.py` starts the webserver and sockets

3. `get_data.py` gets the data, for now from the CSV file `sample_data_trimmed2.csv`

4. the html, css and js for the website is in `/static`, and is served by the webserver

5. Files starting with `microdot` are library files, ignore them.

    Microdot is used to run the webserver and sockets.

6. `simplify_data.py` is a helper script to filter for a subset of the data

---

Put the code in root `/` so that:
1. main.py, boot.py run automatically
2. python imports work correctly


Open Thonny and run `main.py`:

Get the Pico's address from the terminal, and go to `address:port` where port 5000 is being used currently.

---

should transfer data as binary, not text
have it fixed width then no need to split

TODO: on client side, remove old data else uses up memory
