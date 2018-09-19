## Wforced (opts)
A HSL client for [Weakforced](https://github.com/PowerDNS/weakforced). Detects brute force of passwords across multiple servers and services. Can be used in Halon's [AUTH](https://docs.halon.io/hsl/auth.html) context to allow, defer or reject a session.

**Params**

- opts `array` - options array

**Returns**: class object.

The following options are available in the **opts** array.

- host `string` - IP-address of the weakforced service.
- port `number` - TCP port. The default is 8084.
- opts `array` - Options array for the [http](https://docs.halon.io/hsl/functions.html#http) function.
- timeout `number` - Timeout in seconds. The default is 5 seconds.
- username `string` - Username for the weakforced service.
- password `string` - Password for the weakforced service.

## allow(args)
Query the weakforced service if the login should be allowed or not.

**Params**

- wfuser `object` - WforcedUser object. 

**Returns**: `number`, `0` if allowed, `-1` if denied or a positive number for sleep / defer. `-1` if an error occurred.

## report(args, authsuccess)
Report the authentication result to the weakforced service.

**Params**

- wfuser `object` - WforcedUser object.
- authsuccess `boolean` - Result from the authentication attempt. 

**Returns**: `boolean`

## ping()
Check if the weakforced service is available.

**Returns**: `boolean`

## cmd(command, args)
Send any kind of available command to the weakforced service.

**Params**

- command `string` - A weakforced command.
- args `array` - Arguments to pass with the command.

**Returns**: `array`

## WforcedUser (username, password, ip [, attrs [, trunclen]])

**Params**

- username `string` - A username or any type of identifier.
- password `string` - The password that was used, will be hashed by the hashpwd function.
- ip `string` - The IP address for the session.
- attrs `array` - Optional array that will be passed on to the weakforced service.
- trunclen `number` - Truncate the hashed password by bits, by default it will use full length.

**Returns**: class object.

## hashpwd(username, password [, trunclen])

**Params**
- username `string` - A username or any type of identifier.
- password `string` - The password that was used.
- trunclen `number` - Truncate the hashed password by bits, by default it will use full length.

**Returns**: `string`

## Example

```java
$wfuser = WforcedUser($saslusername, $saslpassword, $senderip, ["attrs" => ["policyclient" => $serverip]]);
$wf = Wforced(["url" => "http://172.16.78.25", "port" => 8084, "username" => "admin", "password" => "admin"]);

switch ($wf->allow($wfuser)) {
   case 0:
       if (validate_credentials($saslusername, $saslpassword) == 1) {
           $wf->report($wfuser, true);
           Accept();
       } else {
           $wf->report($wfuser, false);
           Reject();
       }
   case -1:
       Reject();
   default:
       Defer();
}
```
