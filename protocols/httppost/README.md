##httppost(options, fp)
Upload a File to a HTTP sever.

**Params**

- options `array` - options array
- fp `File` - file object

**Returns**: status code if the request succeeded, none if the an error occurred.

The following options are available in the **options** array.

- host `string` - IP-address or hostname of the HTTP server. required
- port `number` - TCP port. The default is 80.
- timeout `number` - Timeout in seconds. The default is 5 seconds.
- uri `string` - The request URI. The default is /.
- name `string` - The uploaded file name. The default is file.ext.
