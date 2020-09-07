## arf_parse($mail, $options)

Parse a rfc5965 compliant ARF report (message/feedback-report), into a associative array containing the report header fields (all lowercased).

**Params**

- mail `MailMessage` - The mail message
- options `array` - options array

**Returns**:
* An `array` with keys `date`, `from`, `to`, `subject`, `feedback_report` and optionally `original_message` and `original_headers`
* `none` on errors

The following options are available in the **options** array.

- original_message `boolean` - Include the original mail message in the output (if it exists), the default is `false`
- original_headers `boolean` - Include the original mail message headers in the output (if they exist), the default is `false`

```
{
	"date": "Thu, 8 Mar 2005 17:40:36 EDT",
	"from": "abusedesk@example.com",
	"to": [
		"abuse@example.net"
	],
	"subject": "FW: Earn money",
	"feedback_report": {
		"feedback-type": [
			"abuse"
		],
		"user-agent": [
			"SomeGenerator\/1.0"
		],
		"version": [
			"1"
		],
		"original-mail-from": [
			"<somespammer@example.net>"
		],
		"original-rcpt-to": [
			"<user@example.com>"
		],
		"received-date": [
			"Thu, 8 Mar 2005 14:00:00 EDT"
		],
		"source-ip": [
			"192.0.2.2"
		],
		"authentication-results": [
			"mail.example.com               smtp.mail=somespammer@example.com;               spf=fail"
		],
		"reported-domain": [
			"example.net"
		],
		"reported-uri": [
			"http:\/\/example.net\/earn_money.html",
			"mailto:user@example.com"
		],
		"removal-recipient": [
			"user@example.com"
		]
	}
}
```
