## ScanCM(options, senderip, senderhelo, sender, recipients, message)
Scan a message with Cloudmarks Authority server (using HTTP POST). This function should be used with the "per_message" cache.

**Params**

- options `array` - options array

**Returns**: score as number, None on error.

The following options are available in the **options** array.

- host `string` - IP-address or hostname of the Authority server. required
- port `number` - TCP port. The default is 80.
- timeout `number` - Timeout in seconds. The default is 5 seconds.
- max_message_size `number` - The max message size in bytes. The default is 5 MiB.

## ScanCMIP(options, ip)
Scan an IP with Cloudmarks Authority server (using HTTP POST). This function should be used with the "per_message" cache.

**Params**

- options `array` - options array
- ip `string` - IP address

**Returns**: score as number, None on error.

The following options are available in the **options** array.

- host `string` - IP-address or hostname of the Authority server. required
- port `number` - TCP port. The default is 80.
- timeout `number` - Timeout in seconds. The default is 5 seconds.
