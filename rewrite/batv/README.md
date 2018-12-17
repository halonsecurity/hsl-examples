This example provides a [BATV](http://mipassoc.org/batv/draft-levine-smtp-batv-01.txt) (Bounce Tag Address Validation) implementation, our [documentation](http://wiki.halon.se/BATV) shows how to implement it properly.

## batv_sign(sender, key, opts)

Sign a BATV address.

**Params**

- sender `string` - The sender address
- key `string` - The key used for signing
- opts `array` - options array

**Returns**: A `string` containing a BATV signed address

The following options are available in the **opts** array.

- keyid `number` - A key id between 0-9. The default is 0.
- days `number` - Number of days the BATV address is valid. The default is 7 days.

## batv_verify(recipient, keys, opts)

Verify a BATV address.

**Params**

- recipient `string` - The recipient address
- keys `array` - Array of key to validate (indexed by keyid)
- opts `array` - options array

**Returns**: A `string` containing a BATV result.

The following options are available in the **opts** array.

- days `number` - Number of days the BATV address is valid. The default is 7 days.

The result string may be any of

| Result   | Status  | Description                                                           |
|----------|---------|-----------------------------------------------------------------------|
| pass     | good    | The BATV tag is valid! Message should be batv_stripped and delivered. |
| missing  | neutral | No BATV tag                                                           |
| invalid  | bad     | BATV tag is invalid                                                   |
| checksum | bad     | BATV tag is bad (invalid key)                                         |
| expired  | bad     | BATV tag has expired                                                  |

## batv_strip(recipient)

Strip the BATV tag from the recipient address, the inverse process of batv_sign.

**Params**

- recipient `string` - The recipient address

**Returns**: A `string` containing a the original recipient.
