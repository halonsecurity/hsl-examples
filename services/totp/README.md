This Time-based One-time Password Algorithm (TOTP) implementation [rfc6238](https://tools.ietf.org/html/rfc6238) can be used with eg. [Google Authenticator](https://en.wikipedia.org/wiki/Google_Authenticator).

Usage example
-------------

Generate a random 16 byte long base32-encoded secret (the one below should not be used in production):

```
$secret = "ABCDEFGHIJKLMNOP";
```

Go to the URL and scan the [QR code](https://github.com/google/google-authenticator/wiki/Key-Uri-Format) in Google Authenticator.

https://www.google.com/chart?chs=200x200&chld=M|0&cht=qr&chl=otpauth://totp/Halon%3Auser@example.com%3Fsecret=ABCDEFGHIJKLMNOP%26issuer=Halon

![logo](https://www.google.com/chart?chs=200x200&chld=M|0&cht=qr&chl=otpauth://totp/Halon%3Auser@example.com%3Fsecret=ABCDEFGHIJKLMNOP%26issuer=Halon)

One implementation could be to require the TOTP token to be appended after the password.

```
if ($username == "totpuser" and $password[0:-6] == "password" and totp($secret) == $password[-6:])
{
  Authenticate();
}
```
