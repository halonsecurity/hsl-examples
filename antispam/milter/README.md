## milter_v2(options, senderip, senderport, senderhelo, sender, recipients, fp)

Implementation of the Milter protocol v2. It's tested with [clamav-milter](http://www.clamav.net/), however minor changes may allow it to connect to other servers as well.

```java
$opts = ["host" => "1.1.1.1", "port" => 3381, "timeout_eod" => 15];
$fp = $arguments["mail"]->toFile(); // Or use "GetMailMessage()->toFile();" in a EOD "Per recipient" script
$result = milter_v2($opts, $senderip, $senderport, $senderhelo, $sender, $recipients, $fp);
if (is_array($result))
  foreach ($result as $r)
	  echo $r;
```

#### clamav-milter
When using clamav-milter, you should use `AddHeader Replace` in the clamav-mitler.conf and parse the `"h"` response array item from `milter_v2` for viruses.
