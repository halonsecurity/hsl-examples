## ctasd(senderip, sender, mailpath)

Classify a message (mailpath) with Cyren's `ctasd`.

**Params**

- senderip `string` - The IP address of the sending server
- sender `string` - The MAIL FROM address
- mailpath `string` - Path to a mail file

**Returns**:
* An `array` with keys `spam` (score), `vod` (virus score), `refid` and `rules` on success
* An `array` with key `error` if Cyren reported an error
* `none` on other errors

## ctipd(senderip)

Classify an IP address (senderip) with Cyren's `ctipd`.

**Params**

- senderip `string` - The IP address of the sending server

**Returns**: a `string` with response "permfail", "tempfail" or "accept", or `none` on error
