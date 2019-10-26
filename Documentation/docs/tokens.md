Page last revised on: {{ git_revision_date }}

#### Why use sotre the active Tokens?

We’ll briefly explore a predominant type of token that are used in session management. Several of the flows we discuss require an understanding of these token.

##### JSON Web Tokens (JWT)

* Each JWT contains specific information that can be interpreted by any party that has that token. For example, this information can contain the user ID of the user for whom it was issued.

* An advantage of using JWTs is scalability as the backend does not need to do a database lookup for every API call.

* The drawback is that revoking a single token on demand (before it expires) can be difficult if methods like blacklisting are not used (which impacts the scalability of the solution). However, one can revoke all tokens by changing the signing key.

##### Common attacks on sessions

Auth tokens are stored on the frontend and the backend and are frequently sent over the network (depending on the session flow). As such, they are vulnerable to several types of attacks.

* Man in the Middle attack
* OAuth token theft
* XSS
* CSRF
* Database/filesystem access
* Session fixation
* Brute force attack
* Social Engineering / physical access

##### The way used in this service to implementing session management flows

###### Short-lived access tokens

If the user voluntarily logs out, the access token is revoked and cleared from the frontend.

**Damage Analysis**
There are no critical auth tokens in this case. However, this method frequently exposes the user’s credentials during transit — making it susceptible to attack.

*Effect of stolen auth tokens*:
If the token is stolen, the attacker will only be able to do damage for a short period of time.

*Detection of theft*:
Token theft may only be detected through the use of heuristic algorithms or if the user notifies the provider/developer of the service.

*Once detected*:
Access tokens need not be revoked since they are short lived. However, if needed, Opaque access tokens can be revoked by removing them from the database.