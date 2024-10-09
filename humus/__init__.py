from os import environ

import requests

class Client:
    def __init__(self, host=None, port=None, protocol=None):
        if host:
            self.host = host
        else:
            self.host = environ.get("HUMUS_HOST", "localhost")
        if port:
            self.port = port
        else:
            self.port = environ.get("HUMUS_PORT", 3030)
        if protocol:
            self.protocol = protocol
        else:
            self.protocol = environ.get("HUMUS_PROTOCOL", "http")

    def insert(self, path, entity):
        requests.post(self.base_path + path.strip("/"), json=entity)


    def get(self, path):
        return requests.get(self.base_path + path.strip("/")).json()

    @property
    def base_path(self):
        return f"{self.protocol}://{self.host}:{self.port}/"
