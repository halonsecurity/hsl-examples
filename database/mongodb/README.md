## MongoDB(address, database[, opts])
MongoDB client class.

**Params**

- address `string` - IP-address to MongoDB server. Required.
- database `string` - The database. Required.
- opts `array` - options array

**Returns**: class object.

The following options are available in the **opts** array.

- port `number` - TCP port. The default is 27017.
- timeout `number` - Timeout in seconds. The default is 30 seconds.

## connect()
Establish a connection to the IP-address that was passed to the class constructor.

**Returns**: true if connection was successful, None on error.

## disconnect()
Disconnects the current connection.

**Returns**: None.

## find(query[, fieldSelector[, offset[, limit]]])
Execute query on the MongoDB server.

**Params**

- query `array` - Query to be executed.
- fieldSelector `array` - Field selector.
- offset `number` - The offset. The default is 0 (no offset).
- limit `number` - The offset. The default is 0 (no limit).

**Returns**: response as array, None on error.
