# pyOpenVk
<a href='https://pypi.org/project/pyOpenVk/'>
    <img src='https://img.shields.io/pypi/v/pyOpenVk.svg' alt='Documentation Status' />
</a>

### Installing

```
pip install pyOpenVk==1.2
```


### Quick Example
```python
from pyOpenVk import api
from pyOpenVk import messages


client = api.auth(login='youre@gmail.com', password='password', instance='openvk.co') # recommend installing an instance "openvk.co"
user_id = 1010
messages.send(client, user_id, 'Привіт світ!')
```

### Links
[LeenzeryDev](https://github.com/leenzerydev)             
[.NET version](https://github.com/LyStudios/OpenVkNetApi)  
