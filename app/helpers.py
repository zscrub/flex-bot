import docker
import requests
import subprocess

from requests import exceptions

docker_ = docker.from_env()

def hello_function() -> str:
    r = requests.get("https://evilinsult.com/generate_insult.php?lang=en&amp;type=json")
    insult = str(r.text)
    print(f"{r}\n{insult}")
    return insult


def kanye_quote() -> str:
    url = "http://api.kanye.rest?"
    r = requests.get(url)
    kanye = r.json()
    kanye = kanye["quote"]
    print(f"{r}\nKanye quote: {kanye}")
    return kanye


def launch_bubblebot() -> str:
    try:
        docker_.containers.run("bubblebot:0.2", name="bubblebot", detach=True)
        return "Starting BubbleBot..."
    except exceptions.HTTPError as e:
        print(e)
        return "BubbleBot already running!"


def stop_bubblebot() -> str:
    try:
        docker_.containers.get("bubblebot").remove(force=True)
        return "Stopping BubbleBot..."
    except exceptions.HTTPError as e:
        print(e)
        return "No bots named bubblebot..."

]