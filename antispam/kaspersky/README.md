## KasperskyAV(options, fp)
Scan a message with Kaspersky Anti-virus (using HTTP POST). This function should be used with the [`per_message` cache](http://docs.halon.se/hsl/structures.html#cache).

**Params**

- options `array` - options array
- fp `File` - the mail file

**Returns**: an array with ``scanResult`` and optionally ``detectionName`` (see Kaspersky documentation), None on error.

The following options are available in the **options** array.

- host `string` - IP-address of the kavhttpd server. required
- port `number` - TCP port. required
- timeout `number` - Timeout in seconds. The default is 2 seconds.