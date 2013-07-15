rfive
=====

Example use of the class

```python
from fabricSSH import *

client = fabricSSHClient("128.196.142.120",ssh_config_path="~/.ssh/config")
client.connect()
client.run("apt-get update; apt-get install -y emacs vim wget language-pack-en"
            + " make gcc g++ gettext texinfo autoconf automake")

# This is to copy a local version of sampleScript.sh over to a remote
# box. This will be placed in ~/test.
test = client.put("~/test","sampleScript.sh",True, 0755)  

#This will delete the file sampleScript.sh
value = client.delete("test/sampleScript.sh") 
```

Based upon the success of prior astromech models, such as the wildly popular R2-series, Industrial Automaton intended the R5-series to cater to budget buyers at the cost of some functionality.
