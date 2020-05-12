## Syslog(address [, opts])
Syslog client class.

**Params**

- address `string` - IP-address to Syslog server. Required.
- opts `array` - options array

**Returns**: class object.

The following options are available in the **opts** array.

- port `number` - UDP port. The default is 514.
- facility `string` - Log facility (see source code). The default is "LOG_MAIL".
- hostname `string` - Hostname. The default is the system hostname.
- application `string` - The application name. The default is "halon".

## logger(priority, message [, opts])
Send a syslog message

- priority `string` - Any of the documented priorites (see source code).
- message `string` - The message to log
- opts `array` - options array

The following options are available in the **opts** array.

- facility `string` - Log facility (see source code). The default is "LOG_MAIL".

**Returns**: true if send was successful, None on error.
