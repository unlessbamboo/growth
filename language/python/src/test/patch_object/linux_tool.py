import re

class LinuxTool(object):
    def __init__(self):
        pass

    def send_shell_cmd(self):
        return "Response from send_shell_cmd function"

    def check_cmd_response(self):
        response = self.send_shell_cmd()
        print("response: {}".format(response))
        return re.search(r"mock_send_shell_cmd", response)
