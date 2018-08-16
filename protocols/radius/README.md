## Radius(address, secret [, opts])
Radius client class.

**Params**

- address `string` - IP-address to Radius server. Required.
- secret `string` - Radius secret. Required.
- opts `array` - options array

**Returns**: class object.

The following options are available in the **opts** array.

- port `number` - UDP port. The default is 1812.
- timeout `number` - Timeout. The default is 5 seconds.

## auth(username, password, clientip = "")
Authenticate

- username `string` - The username
- password `string` - The password
- clientip `string` - The client ip

**Returns**:

* On accept: an array of all returned vendor sepecific attributes for Halon (33234)
* On reject: 0
* On error: -1

The following is a replacement implementation for the deprecated radius_authen function

```
function radius_authen($options, $username, $password)
{
 $r = Radius($options["host"], $options["secret"], $options);
 return $r->auth($username, $password, $options["clientip"] ?? none);
}
```
