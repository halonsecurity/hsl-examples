## dsn_parse($message)

Parse a rfc3464 compliant MIME part (message/delivery-status), into a associative array containing the per-message fields and per-recipient fields (all lowercased).

```
{
  "message": {
    "reporting-mta": "dns; mail.example.org",
    "received-from-mta": "smtp; mx1.example.com (1.2.3.4)",
    "original-envelope-id": "f03cf414-5fa5-11e9-9074-d9e886935329",
    "arrival-date": "Mon, 15 Apr 2019 19:42:44 +0200"
  },
  "recipients": [
    {
      "final-recipient": "rfc822; user@example.org",
      "action": "failed",
      "status": "5.7.1 An error message",
      "remote-mta": "dns; imap.example.org",
      "diagnostic-code": "smtp; 550 5.7.1 An error message"
    }
  ]
}
```

On errors `none` is returned.
