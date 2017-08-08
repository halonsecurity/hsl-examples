## PostgreSQL(address, user, database[, opts])
PostgreSQL client class.

**Params**

- address `string` - IP-address to PostgreSQL server. Required.
- user `string` - The user. Required.
- database `string` - The database. Required.
- opts `array` - options array

**Returns**: class object.

The following options are available in the **opts** array.

- port `number` - TCP port. The default is 5432.
- timeout `number` - Timeout in seconds. The default is 30 seconds.

## connect()
Establish a connection to the IP-address that was passed to the class constructor.

**Returns**: true if connection was successful, None on error.

## disconnect()
Disconnects the current connection.

**Returns**: None.

## query(query, params)
Pass a "prepared" statement to the PostgreSQL server.

**Params**

- statement `string` - Query to be executed.
- params `array` - Params to be executed.

**Returns**: response as array, None on error.

## execute(statement)
Pass a statement as-is to the PostgreSQL server.

**Params**

- statement `string` - Query to be executed.

**Returns**: response as array, None on error.

## getLastError()
Returns the last error that was sent by the server.

**Returns**: array, None if no errors found.
