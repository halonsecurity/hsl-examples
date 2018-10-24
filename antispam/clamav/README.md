## clamav(mailpath)

Scan a message (mailpath) for virus using a ClamAV.

**Params**

- mailpath `string` - Path to a mail file

**Returns**: A `string` if a virus is found (with the virus name), `false` if the message was clean or `none` on error.