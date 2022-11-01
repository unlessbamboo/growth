from unittest import TestCase, mock
from linux_tool import LinuxTool


class TestLinuxTool(TestCase):
    def setUp(self):
        self.linux_tool = LinuxTool()

    def tearDown(self):
        pass

    @mock.patch.object(LinuxTool, "send_shell_cmd")
    def test_check_cmd_response(self, mock_send_shell_cmd):
        def t():
            return 'xxxxxxxxxxxxxxxxx'
        mock_send_shell_cmd = t
        #  mock_send_shell_cmd.return_value = "Response from emulated mock_send_shell_cmd function"

        status = self.linux_tool.check_cmd_response()
        print("check result: %s" % status)
        self.assertTrue(status)
