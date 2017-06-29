## Memcached(address, opts)
Memcached client class.

**Params**

- address `string` - IP-address to memcached server. Required.
- opts `array` - options array

**Returns**: class object.

The following options are available in the **opts** array.

- port `number` - TCP port. The default is 6379.
- timeout `number` - Timeout in seconds. The default is 5 seconds.

## connect()
Establish a connection to the IP-address that was passed to the class constructor.

**Returns**: true if connection was successful, None on error.

## disconnect()
Disconnects the current connection.

**Returns**: None.

## set(key, value, flags = 0, exptime = 0)
## get(key)
## add(key, value, flags = 0, exptime = 0)
## del(key)
## replace(key, value, flags = 0, exptime = 0)
## append(key, value, flags = 0, exptime = 0)
## prepend(key, value, flags = 0, $xptime = 0)
