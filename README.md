# Quick start :

### 1 - Requirements 
- You need to install the Akash CLI tools. refers to this tutorial 
    https://docs.akash.network/guides/deploy#part-1-install-akash

### 2 - Install the package.
```
pip install akash-python
```

### 3 - Import the akash-python client.

```
from akash.akash import Akash

client = Akash()

balances = client.query.bank.balances(address="akash_address", output="json")
```

All the commands lines availables in the CLI has been added to the akash-python packages
https://docs.akash.network/general-commands