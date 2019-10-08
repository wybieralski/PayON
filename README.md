
<details>
  <summary>POST /user_account</summary>
  
<p>
  
- user_id
- name
- surname
- date_of_birth
- balance
Response:
'200':
  decription: Account created successfully
  schema:
    type: object
    properties:
      name:
        type: string
        example: Lukasz Wybieralski
      user_id:
        type: integer
        format: uuid
        example: d290f1ee-6c54-4b01-90e6-d701748f0851
      created_at:
        type: date
        format: int64
        example: 164
      balance:
        type: float
        format: int64
        example: 1644.40
 '400':
    description: Bad request. User ID must be an integer and larger than 0.
 '401':
    description: Authorization information is missing or invalid.
  '5XX':
    description: Unexpected error.
  
</p>
  
</details>


### Description
PayON is a payment service made for academic project at the University of Aveiro

### Technologies used

### Flask
<p>Link: <a href="https://palletsprojects.com/p/flask/
" class="issue-link" title="This is a simple issue">Flask</a> </p>

### Flask-RESTPlus
<p>Link: <a href="https://flask-restplus.readthedocs.io/en/stable/
" class="issue-link" title="This is a simple issue">Flask-RESTPlus</a> </p>

### Swagger UI
<p>Link: <a href="https://swagger.io
" class="issue-link" title="This is a simple issue">Swagger</a> </p>
### API

In PayON service we have following functionalities:
- Creating an account
- Sending money to our account (top-up)
- Paying with our account
- Getting all the transactions
- Geting all users

```markdown
POST /user_account/create
- user_id
- name
- surname
- date_of_birth
- balance
Response:
'200':
  decription: Account created successfully
  schema:
    type: object
    properties:
      name:
        type: string
        example: Lukasz Wybieralski
      user_id:
        type: integer
        format: uuid
        example: d290f1ee-6c54-4b01-90e6-d701748f0851
      created_at:
        type: date
        format: int64
        example: 164
      balance:
        type: float
        format: int64
        example: 1644.40
 '400':
    description: Bad request. User ID must be an integer and larger than 0.
 '401':
    description: Authorization information is missing or invalid.
  '5XX':
    description: Unexpected error.
    

<details>
  <summary>POST /user_account</summary>
  
<p>
  
- user_id
- name
- surname
- date_of_birth
- balance
Response:
'200':
  decription: Account created successfully
  schema:
    type: object
    properties:
      name:
        type: string
        example: Lukasz Wybieralski
      user_id:
        type: integer
        format: uuid
        example: d290f1ee-6c54-4b01-90e6-d701748f0851
      created_at:
        type: date
        format: int64
        example: 164
      balance:
        type: float
        format: int64
        example: 1644.40
 '400':
    description: Bad request. User ID must be an integer and larger than 0.
 '401':
    description: Authorization information is missing or invalid.
  '5XX':
    description: Unexpected error.
  
</p>
  
</details>
    
    
# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/wybieralski/PayON/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
