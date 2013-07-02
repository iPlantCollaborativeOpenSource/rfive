rfive
=====

Example use of the class

```python
from fabricSSH import *
client = fabricSSHClient("128.196.142.120",ssh_config_path="/root/.ssh/config")
client.connect()
client.run("apt-get update; apt-get install -y emacs vim wget language-pack-en" + " make gcc g++ gettext texinfo autoconf automake")
test = client.put("~/test","sampleScript.sh",True, 0755)  # This is to copy a local version of sampleScript.sh over to a remote box. This will be placed in ~/test.

value = client.delete("test/sampleScript.sh") #This will delete the file sampleScript.sh
```



Based upon the success of prior astromech models, such as the wildly popular R2-series, Industrial Automaton intended the R5-series to cater to budget buyers at the cost of some functionality.
