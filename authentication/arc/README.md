## Authenticated Received Chain (ARC) 
An ARC implementation based on [draft-ietf-dmarc-arc-protocol-18](https://tools.ietf.org/html/draft-ietf-dmarc-arc-protocol-18).

```java
include "authentication.header";
include "authentication.arc";

$chain = ARC::chainValidate();
if ($chain["status"] == "pass" or $chain["status"] == "none")
{
	ARC::seal(
			"201805", "example.com", "pki:arc",
			$chain,
			AuthenticationResults()
				->SPF(["smtp.remote-ip" => $senderip])
				->DKIM()
				->DMARC()
				->addMethod("arc", $chain["status"], ["header.oldest-pass" => $chain["oldestpass"] ?? "0"])
				->toString()
		);
}
```
