## ScanVADE(options)
Scan a message with Vadesecure's Daemon remotely over IP. This function should be used with the "per_message" cache.

**Params**

- options `array` - options array

**Returns**: array of results, None on error.

The following options are available in the **options** array.

- host `string` - IP-address or hostname of the Vadesecure daemon. required
- port `number` - TCP port. The default is 8083.
- timeout `number` - Timeout in seconds. The default is 5 seconds.

The result array usually contains, "Score" (Number), "State" (Number) and "Cause" (String).
