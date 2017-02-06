This Time-based One-time Password Algorithm (TOTP) implementation can be used with eg. [Google Authenticator](https://en.wikipedia.org/wiki/Google_Authenticator).

Usage example
-------------

Generate a random 16 byte long base32-encoded secret:

```
$secret = "ABCDEFGHIJKLMNOP";
```

Go to the URL and scan the QR code in Google Authenticator.

https://www.google.com/chart?chs=200x200&chld=M|0&cht=qr&chl=otpauth://totp/Halon%3Auser@example.com%3Fsecret=ABCDEFGHIJKLMNOP%26issuer=Halon

![logo](https://www.google.com/chart?chs=200x200&chld=M|0&cht=qr&chl=otpauth://totp/Halon%3Auser@example.com%3Fsecret=ABCDEFGHIJKLMNOP%26issuer=Halon)

One implementation could be to require the TOTP token to be appended before the password.

```
if (totp($secret) == $password[0:6] && $password[6:] == "password")
{
  Authenticate();
}
```
