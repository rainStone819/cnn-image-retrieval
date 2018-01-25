Enviroment prepare:
---
Step 0: System requirements:
1. ubuntu 16 OS
2. CPU 4 cores
3. memory >= 8G

install the prerequisites
```bash
apt-get install openssl
apt-get install libssl-dev
```

--- 
Step 1: Install python pip from apt-get
sudo apt-get install python-pip

---
Step 2: Install python package.
firstly, install the numpy, because other packages depend on numpy:
pip install numpy==1.11.3
I have frozen the python enviroment by pip freeze. You can run following command to restore the enviroment directly:
pip install -r python-requirements.txt


You also can install the python package manually.
Have to install follow packages:
1. numpy, scipy, tensorflow, opencv2...

---
Step 3: How to verify the enviroment
1. run following commands in the python shell
root@iZ2ze0ssd5lunjdhnl75evZ:~# python
Python 2.7.12 (default, Nov 19 2016, 06:48:10) 
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow
>>> import numpy as np
>>> import scipy as np
>>> import scipy as scipy

