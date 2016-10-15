#ident_lookup(senderip, senderport, serverip, serverport[, options])
Try to lookup the username of the connecting client using the ident (rfc1413) protocol.

**Params**

- senderip `string` - the senderip
- senderport `number` - the senderport
- serverip `string` - the serverip
- serverport `number` - the serverport
- options `array` - options array

**Returns**: if request was made an array is returned, otherwise the type None is returned.

The following options are available in the **options** array.

- port `number` - TCP port. The default is 113
- timeout `number` - Timeout in seconds. The default is 5 seconds.

The array returned may containing index of either "error" or "os" and "username".

``` php
["username" => $username, "error" => $error = "UNKNOWN-ERROR"] = ident_lookup($senderip, $senderport, $serverip, $serverport);
if (is_string($username))
    echo "Ident: $username";
else
    echo "Error: $error";
```
