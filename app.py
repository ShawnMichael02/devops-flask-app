
from flask import Flask
import redis
import json
import time

app = Flask(__name__)

# Connect to Redis container
r = redis.Redis(
    host='redis-server',
    port=6379,
    decode_responses=True
)

# Cache duration: 10 minutes
CACHE_DURATION = 600


def get_cached_page(key, html):
    data = r.get(key)

    if data is not None:
        data = json.loads(data)

        if time.time() - data['time'] <= CACHE_DURATION:
            return data['html']

    # Store newly generated HTML in Redis
    r.set(key, json.dumps({
        'html': html,
        'time': time.time()
    }))

    return html


@app.route("/")
def home():
    html = """
    <h1>Welcome!</h1>
    <a href="/about">About</a><br>
    <a href="/contact">Contact</a>
    """

    return get_cached_page('home', html)


@app.route("/about")
def about():
    html = """
    <h1>About</h1>
    <a href="https://python.com/">Python website</a><br>
    <a href="https://flask.palletsprojects.com/">
        Flask website
    </a>
    """

    return get_cached_page('about', html)


@app.route("/contact")
def contact():
    html = """
    <h1>Contact</h1>
    <p>Email: "C24709519@mytudublin.ie"</p>
    <a href="/">Home</a>
    """

    return get_cached_page('contact', html)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

