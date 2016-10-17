##minger_lookup(host, address[, options])
Implementation of Alt-N Technologies' MDaemon minger protocol; [draft-hathcock-minger-07](https://tools.ietf.org/html/draft-hathcock-minger-06) for recipient lookup.

**Params**

- host `string` - the minger host
- address `string` - the sender adress
- options `array` - options array

**Returns**: if request was made an number is returned, otherwise the type None is returned.

The following options are available in the **options** array.

- port `number` - TCP port. The default is 4069
- timeout `number` - Timeout in seconds. The default is 5 seconds.
