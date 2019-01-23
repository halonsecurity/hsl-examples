This example provides a [Mail::SRS](http://search.cpan.org/perldoc?Mail::SRS) compatible sender rewrite scheme implementation, our [documentation](https://support.halon.io/hc/en-us/articles/360001368529) shows how to implement it properly.

## SRS_forward(address, alias, opts)

Apply the SRS forward scheme to an address

**Params**

- address `string` - The email address
- alias `string` - The domain to use when rewriting
- opts `array` - options array

**Returns**: A `string` containing an email address with SRS applied

The following options are available in the **opts** array.

- secret `string` - A secret. The default is an empty secret.
- hashlen `number` - Number of charaters to include from the secret hash. The default is 4.

## SRS_reverse(address, opts)

Apply the SRS forward scheme to an address

**Params**

- address `string` - The email address
- opts `array` - options array

**Returns**: A `string` containing an email address the SRS removed. On error `none` is returned.

The following options are available in the **opts** array.

- secret `string` - A secret. The default is an empty secret.
- hashlen `number` - Number of charaters to include from the secret hash. The default is 4.
- maxage `number` - Number of days the SRS address should be valid. The default is 21 days.
