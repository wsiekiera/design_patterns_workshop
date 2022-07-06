import json
import uuid
import hashlib


class LoginRequest:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return self.username + ' ' + self.password


class Target:
    """
    The Target defines the domain-specific interface used by the client code.
    """

    def request(self, login_request) -> str:
        return "Trying to login with credentials: " + str(login_request)


class Adaptee:
    """
    The Adaptee contains some useful behavior, but its interface is incompatible
    with the existing client code. The Adaptee needs some adaptation before the
    client code can use it.
    """

    def specific_request(self, login_request_in_json) -> str:
        return "Trying to login with JSON credentials: " + login_request_in_json


class Adapter(Target):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface via composition.
    """

    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    # {"uuid": "2832y2", "login":  "sss", "pass":  "MD5aaa"}

    def request(self, login_request: LoginRequest) -> str:
        json_data = dict()
        json_data['uuid'] = str(uuid.uuid4())
        json_data['login'] = login_request.username
        json_data['pass'] = hashlib.md5(str(login_request.password).encode()).hexdigest()

        return self.adaptee.specific_request(json.dumps(json_data))


def client_code(target: Target, request: LoginRequest) -> None:
    """
    The client code supports all classes that follow the Target interface.
    """

    print(target.request(request), end="")


if __name__ == "__main__":
    login_request = LoginRequest('some_user', 'some_pass')
    target = Target()
    client_code(target, login_request)
    print('###')
    adaptee = Adaptee()
    adapter = Adapter(adaptee)

    client_code(adapter, login_request)