## MySQL(address, user, password, database[, opts])
MySQL client class.

**Params**

- address `string` - IP-address to MySQL server. Required.
- user `string` - The user. Required.
- password `string` - The password. Required.
- database `string` - The database. Required.
- opts `array` - options array

**Returns**: class object.

The following options are available in the **opts** array.

- port `number` - TCP port. The default is 3306.
- timeout `number` - Timeout in seconds. The default is 30 seconds.

## connect()
Establish a connection to the IP-address that was passed to the class constructor.

**Returns**: true if connection was successful, None on error.

## disconnect()
Disconnects the current connection.

**Returns**: None.

## query(query, params)
Pass a "prepared" statement to the MySQL server.

**Params**

- statement `string` - Query to be executed.
- params `array` - Params to be executed.

**Returns**: response as array (SELECT) or number of affected rows (eg. UPDATE), None on error.

## execute(statement)
Pass a statement as-is to the MySQL server.

**Params**

- statement `string` - Query to be executed.

**Returns**: response as array (SELECT) or number of affected rows (eg. UPDATE), None on error.

## getLastError()
Returns the last error that was sent by the server.

**Returns**: string, None if no errors found.
