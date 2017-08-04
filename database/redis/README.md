## Redis(address, opts)
Redis client class with support to pass commands as-is.

**Params**

- address `string` - IP-address to redis server. Required.
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

## query(cmd)
Pass a command as-is to the redis server.

**Params**

- cmd `string` - Command to be executed.

**Returns**: response as string, array or integer, None on error.

## getLastError()
Returns the last error that was sent by the server.

**Returns**: array, None if no errors found.
