## Authentication-Results Header Field 
Add a Authentication-Results Header Field (https://tools.ietf.org/html/rfc7001).

```java
include "authentication.header";

$mail->addHeader("Authentication-Results", AuthenticationResults()
				->SPF(["smtp.remote-ip" => $senderip])
				->DKIM()
				->DMARC()
				->toString()
		));
```
