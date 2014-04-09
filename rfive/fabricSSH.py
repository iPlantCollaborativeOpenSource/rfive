import os
from StringIO import StringIO
import sys
from fabric.api import env as fenv
from fabric.api import get as fget
from fabric.api import put as fput
from fabric.api import run as frun
from fabric.api import settings as fsettings
from fabric.network import disconnect_all

class FabricSSHClient(object):

    """
    Base class representing a connection over SSH/SCP to a remote node.
    """
    def __init__(self, hostname, port=22, username='root', password=None,
                 key=None, timeout=None, ssh_config_path=None):
        """
        @type hostname: C{str}
        @keyword hostname: Hostname or IP address to connect to.

        @type port: C{int}
        @keyword port: TCP port to communicate on, defaults to 22.

        @type username: C{str}
        @keyword username: Username to use, defaults to root.

        @type password: C{str}
        @keyword password: Password to authenticate with.

        @type key: C{list}
        @keyword key: Private SSH keys to authenticate with.

        @type ssh_config_path: C{str}
        @keyword ssh_config_path: SSH config file to authenticate with.
        """
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.key = []
        self.key.append(key)
        self.timeout = timeout
        self.ssh_config_path = ssh_config_path

    def connect(self, ignore_hosts=False):
        """
        Connect to the remote node over SSH.
        """
        fenv.abort_exception = Exception
        fenv.user = self.username
        fenv.host_string = self.hostname
        fenv.port = self.port
        if ignore_hosts:
            fenv.disable_known_hosts = True

        if self.ssh_config_path is not None:
            fenv.use_ssh_config = True
            fenv.ssh_config_path = self.ssh_config_path
        else:
            fenv.key_filename = self.key
        return True

    def put(self, path, contents=None, chmod=None, mode="w"):
        """
        Upload a file to the remote node

        @type path: C{str}
        @keyword path: File path on the remote node.

        @type contents: C{str}
        @keyword contents: File Contents.

        @type chmod: C{int}
        @keyword chmod: Mode in which the file settings will be created
                       with. Example 0755, 0777 etc.

        @type mode: C{int}
        @keyword mode: Mode to write to 

        @return: Full path to the location where a file has been saved.
        @rtype: C{str}
        """
        # make sure the directory is there!
        dir_ = os.path.split(path)[0]
        if dir_ and dir_ != ".":
            command = "mkdir -p " + dir_
            mkdir_return = self.run(command)
        if mode == "w":
            fput(StringIO(contents), path, mode=chmod)
        elif mode == "a" and contents:
            contents_ = StringIO()
            fget(path, contents_)
            contents_.seek(0, 2)
            contents_.write(contents) # append new contents
            contents_.seek(0)
            fput(contents_, path, mode=chmod)
        else:
            raise ValueError('Invalid mode: ' + mode)
        return path

    def delete(self, path):
        """
        Delete/Unlink a file on the remote node.

        @type path: C{str}
        @keyword path: File path on the remote node.

        @return: True if the file has been successfuly deleted, False otherwise
        @rtype: C{bool}
        """
        successful = True
        command = '[ -f ' + path + ' ] && echo "1" || echo "0"'
        mkdir_return = self.run(command)

        if mkdir_return[0] == "0":
            successful = False
        else:
            delete_value = self.run("rm -f " + path)
            if delete_value[2] != 0:
                successful = False
            else:
                return successful

    def run(self, cmd, test=True):
        """
        Run a command on a remote node.

        @type cmd: C{str}
        @keyword cmd: Command to run.

        @type warn_only: C{bool}
        @keyword warn_only: If set to true, this will keep executing the
        command, if set to false, will halt the running of commands when
        an error occurs. Defaults to true.

        @return C{list} of [stdout, stderr, exit_status]
        """
        with fsettings(warn_only=test):
            results = frun(cmd)
            return_values = [results, results.stderr, results.return_code]
            return return_values

    def close(self):
        """
        Close a fabric connection to a remote box
        """
        disconnect_all()
        return True
