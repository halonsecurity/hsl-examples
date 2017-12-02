## RSPAMD (opts)
Scan a message with [rspamd](https://www.rspamd.com/).

**Params**

- opts `array` - options array

**Returns**: class object.

The following options are available in the **opts** array.

- host `string` - IP-address of the rspamd service.
- port `number` - TCP port. The default is 11333.
- tls `array` - TLS options array for the rspamd service.
- controllerhost `string` - IP-address of the rspamd controller.
- controllerport `number` - TCP port. The default is 11334.
- controllertls `array` - TLS options array for the rspamd controller.
- password `string` - Password for the rspamd controller.
- timeout `number` - Timeout in seconds. The default is 5 seconds.
- max_message_size `number` - The max message size in bytes. The default is 5 MiB.

The following options are available in the **tls** and **controllertls** array.

- enabled `boolean` - 
- opts `array` - All available options can be found on [here](http://docs.halon.se/hsl/functions.html?highlight=tlssocket#TLSSocket)

## scan(fp)
Check if a message is spam or not. 

**Params**

- fp `File` - file object such as return type of [GetMailFile()](http://docs.halon.se/hsl/data.html#data.GetMailFile). **Required**.

**Returns**: associative array containing the result of the scan

**Return type**: `array`, `none` on error

## learn(fp, type)
Send a message to the controller for learning.

**Params**

- fp `File` - file object such as return type of [GetMailFile()](http://docs.halon.se/hsl/data.html#data.GetMailFile). **Required**.
- type `string` - Specify a type, either spam or ham. **Required**.

**Returns**: associative array containing the result of the scan

**Return type**: `array`, `none` on error