## SMTPClient(address, opts)
SMTP client class

**Params**

- address `string` - IP address of SMTP server (required)
- opts `array` - Options array
  - port `number` - TCP port (default 25)
  - timeout `number` - Timeout in seconds (default 5)

**Returns**: class object.

## Example
```
// Returns [success, isPermanent, lastError]
function SMTPDeliver($address, $sender, $recipients, $fp)
{
	$smtp = SMTPClient($address, ["debug" => true]);
	if (!$smtp->connect()) return [false, $smtp->isPermanent(), $smtp->getLastError()];
	if (!$smtp->EHLO(gethostname())) return [false, $smtp->isPermanent(), $smtp->getLastError()];
	if (!$smtp->MAILFROM($sender)) return [false, $smtp->isPermanent(), $smtp->getLastError()];
	foreach ($recipients as $recipient)
		if (!$smtp->RCPTTO($recipient)) return [false, $smtp->isPermanent(), $smtp->getLastError()];
	if (!$smtp->DATA($fp)) return [false, $smtp->isPermanent(), $smtp->getLastError()];
	$smtp->QUIT();
	$smtp->disconnect();
	return [true];
}
[$ok, $ispermanent, $lasterror] = SMTPDeliver("1.2.3.4", $sender, $recipients, GetMailFile());
```

### connect()
Establish a connection to the IP address that was passed to the class constructor.

**Returns**: true if connection was successful, false on error (details in `getLastError`)

### disconnect()
### EHLO(hostname)
### XCLIENT(name, value)
### MAILFROM(sender)
### RCPTTO(recipient)
### DATA(fp)
### QUIT()
### getLastError()
### isPermanent()
