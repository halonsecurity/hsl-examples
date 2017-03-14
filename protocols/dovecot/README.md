## dovecot_lookup_auth(options, username, password)
Try to authenticate the username against a dovecot server.

**Params**

- options `array` - options array
- username `string` - username
- password `string` - password

**Returns**: 1 if the authentication succeeded, 0 if the authentication failed and -1 if an error occurred.

The following options are available in the **options** array.

- host `string` - IP-address or hostname of the dovecot server. required
- port `number` - TCP port. required
- timeout `number` - Timeout in seconds. The default is 5 seconds.

There are also some protocol specific flags that may be configured.

- service `string` - ervice name to identify this request. The default is smtp.
- rip `string` - The IP-address of the client (remote IP).
- lip `string` - The IP-address of the Halon (local IP).
- secured `boolean` - Set to true if the client has tlsstarted. The default is false
