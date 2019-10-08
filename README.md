## PayON - payment service made for academic project at the University of Aveiro



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
      id:
        type: integer
        format: int64
        readOnly: true
        example: 164
      user_id:
        type: integer
        format: int64
        readOnly: true
        example: 164
      created_at:
        type: integer
        format: int64
        readOnly: true
        example: 164
      balance:
        type: integer
        format: int64
        readOnly: true
        example: 164
'400':
  description: Invalid input
'409'
  description: User already exists

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
