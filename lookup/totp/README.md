# Class TOTP
A Class implementing Time-based One-time Password Algorithm (TOTP) [rfc6238](https://tools.ietf.org/html/rfc6238) can be used with eg. [Google Authenticator](https://en.wikipedia.org/wiki/Google_Authenticator).

You need to run Halon 5.5 or newer, as the functions *base32_decode()* and *base32_endode()* are used.

# Description
Based on a secret known to you (the Halon system) and the user, you can verify a token
supplied by the user at a given time. The token is string af 6 integers.

To verify, create an instance of the class *TOTP* with the secret. Use the
function *verify_token(user_token)* of the object to verify the token supplied
by the user. Time is in slices of 30 seconds. A token is valid for the
previous, current and next slice of time. This is to allow for the user reaction
time as well as time difference between Halon and the users's system.

# Usage examples

Validate a token with a base32 encoded secret:
```
$base32_encoded_user_secret = base32_encode("the-secret-to-use");

$TOTP = TOTP(["secret" => $base32_encoded_user_secret]);

if ($TOTP->verify_token($user_token)) {
  echo "User authenticated";
}
```

Validate a token with a non-encoded secret:
```
$raw_user_secret = "the-secret-to-use";

$TOTP = TOTP(["secret" => $raw_user_secret, "is_base32" = false]);

if ($TOTP->verify_token($user_token)) {
  echo "User authenticated";
}
```

Get the current token for a secret:
```
$base32_encoded_user_secret = base32_encode("the-secret-to-use");

$TOTP = TOTP(["secret" => $base32_encoded_user_secret]);

$token = $TOTP->get_token();
```

Require the valid TOTP token (length 6) to be appended after the password for user *totpuser*.
```
if ($username == "totpuser" and
    $password[0:-6] == "password" and TOTP(["secret" => $base32_encoded_secret])->get_token() == $password[-6:])
{
  Authenticate();
}
```

# Constructor
The TOTP constructor has these optional arguments:
* *secret*: The secret to calculate tokens for. (Default: Random 64 character string).
* *is_base32*: Is the secret encoded as base32?. (Default: *true*).
* *time*: The time (As seconds since epoch) to validate tokens for. (Default: The time of TOTP object instantiation).
* *window_width*: The width of a slice of time in seconds. (Default: *30*).
* *window_back*: How many slices of time, before the current, to verify a token for with *verify_token()*. (Default: *1*).
* *window_forward*: How many slices of time, after the current, to verify a token for with *verify_token()*. (Default: *1*)

An example of instantiating a *TOTP* object with secret *"my_secret"*, and all
other arguments explicitly set to their defaults:
```
$TOTP = TOTP([
  "secret" => "my_secret",
  "is_base32" => true,
  "time" => time(),
  "window_width" => 30,
  "window_back" => 1,
  "window_forward" => 1 
  ]);
```

# Methods
The *TOTP* class, has the following methods:
* verify_token(*token*): Verifies a token for the secret. Returns *true* or *false*.
* get_token(): Get token for the secret. Defaults to current slice of time. Accepts a *counter* (A slice of time, positive integer) as optional argument.
