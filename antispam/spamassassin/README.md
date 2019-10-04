## SPAMC (address, mail, opts)
Client for the [SpamAssassin (spamd) Network Protocol](https://github.com/apache/spamassassin/blob/trunk/spamd/PROTOCOL).

**Params**

- address `string` - IP-address to the spamd server. **Required**.
- mail `File` - file object such as return type of [toFile()](https://docs.halon.io/hsl/functions.html#MailMessage.toFile). **Required**.
- opts `array` - options array

**Returns**: class object.

The following options are available in the **opts** array.

- port `number` - TCP port. The default is 783.
- user `string` - Username of the user for which the scan is being performed.
- sender `string` - Prepends a "Return-Path" header to the mail file with the provided envelope sender.
- size_limit `number` - Size limit in bytes. The default is 512 000.
- timeout `number` - Timeout in seconds. The default is 30 seconds.

## ping()
Check if the spamd server is alive.

**Returns**: `true` if response is valid, `false` for invalid response

**Return type**: `boolean`, `none` on error

## check()
Check if message is spam or not.

**Returns**: associative array containing the result of the scan

**Return type**: `array`, `none` on error

## symbols()
Check if message is spam or not and also include symbols hit in the response.

**Returns**: associative array containing the result of the scan and list of symbols hit

**Return type**: `array`, `none` on error