import docker
import requests
import subprocess

docker_ = docker.from_env()

def hello_function():
    r = requests.get("https://evilinsult.com/generate_insult.php?lang=en&amp;type=json")
    insult = str(r.text)
    print(f"{r}\n{insult}")
    return insult


def kanye_quote():
    url = "http://api.kanye.rest?"
    r = requests.get(url)
    kanye = r.json()
    kanye = kanye["quote"]
    print(f"{r}\nKanye quote: {kanye}")
    return kanye


# for now, everything as seperate commands, implement automated git pull on start
# might need to rebuild docker image instead of docker start
def launch_bubblebot():
    docker_.containers.start("bubblebot", detach=True)
    return "Starting BubbleBot..."

def stop_bubblebot():
    docker_.containers.stop("bubblebot", detach=True)
    return "Stopping BubbleBot..."