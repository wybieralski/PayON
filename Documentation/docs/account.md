Page last revised on: {{ git_revision_date }}

## Account

#### Create Account

This endpoint creates one account. 

!!! note
    At the moment of creating an account, an outsourcing already offers a unique identifying ID that identifies the user. You only need to match this ID to an account.

!!! warning 
    If the external source is a social network, for example, a user can sign in with Facebook or Instagram and this generates 2 different users.

##### Request

    POST /account

**Content-Type** : application/json


| Field         | Description                                    | Format                     |
|:-------------:|:---------------------------------------------- |:--------------------------:|
| user_id       | the user ID                                    | UUID                       | 
| currency      | the account currency                           | 3-letter ISO currency code |


##### Response

**Content-Type** : application/json

| Field         | Description                                    | Format                     |
|:-------------:|:---------------------------------------------- |:--------------------------:|
| id            | the account ID                                 | UUID                       |
| user_id       | the user ID                                    | UUID                       |
| currency      | the account currency                           | 3-letter ISO currency code |  
| balance       | the available balance                          | Decimal                    |
| state         | the account state, one of _active_, _inactive_ | Boolean                    |
| created_at    | the instant when the account was created       | ISO date/time              |
| updated_at    | the instant when the account was last updated  | ISO date/time              |

--------

#### Add Amount

 *This endpoint permits add an amount to an account*

##### Request

    POST /account/<id>/amount

**Content-Type** : application/json


| Field         | Description                                    | Format                     |
|:-------------:|:---------------------------------------------- |:--------------------------:|
| amount        | amount to add to account                       | Decimal                    |

##### Response

**Content-Type** : application/json

[General Response]

--------

#### Activate Account

 *This endpoints activate an account*

##### Request

    POST /account/<id>/activate

##### Response

**Content-Type** : application/json

[General Response]

--------

#### Desactivate Account

*This endpoints desactivate an account*

##### Request

    POST /account/<id>/desactivate

##### Response

**Content-Type** : application/json

[General Response]

--------

#### Account Information

 *This endpoint gives information about an account*
##### Resquest

    GET /account/<id>

##### Response

**Content-Type** : application/json

| Field         | Description                                    | Format                     |
|:-------------:|:---------------------------------------------- |:--------------------------:|
| id            | the account ID                                 | UUID                       |
| user_id       | the user ID                                    | UUID                       |
| currency      | the account currency                           | 3-letter ISO currency code |  
| balance       | the available balance                          | Decimal                    |
| state         | the account state, one of _active_, _inactive_ | Boolean                    |
| created_at    | the instant when the account was created       | ISO date/time              |
| updated_at    | the instant when the account was last updated  | ISO date/time              |  
