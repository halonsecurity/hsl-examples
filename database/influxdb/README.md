## InfluxDB(address, opts)
InfluxDB client class to send [line protocol](https://docs.influxdata.com/influxdb/v1.6/write_protocols/line_protocol_reference/) instructions over UDP.

**Params**

- address `string` - IP-address to InfluxDB server. Required.
- opts `array` - options array

**Returns**: class object.

The following options are available in the **opts** array.

- port `number` - UDP port. The default is 8089.

## send(measurement, fieldset, [tagset])
Send a line protocol update.

- measurement `string` - The measurement.
- fieldset `array`- The fieldset, key-value array
- tagset `array`- The tagset, key-value array
