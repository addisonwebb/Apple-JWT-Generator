# Apple JWT Generator

In order to use MapKit JS or MusicKit JS you need to generate a JWT to authenticate your requests. Unfortuneatly this isn't straight forward and Apple's documentation isn't super helpful with showing you how to generate a JWT.

> MapKit JS requires authorization via JSON Web Tokens (JWT) for initialization and some API calls. You obtain a key used to create the token when you complete the setup in your Apple Developer account.

This simple Python program should help you generate a JWT you can use for development.

### What is a JWT?
JSON Web Tokens are a method for representing claims securely between two parties. For more information check out [jwt.io](https://jwt.io/introduction/)

## What do you need from Apple?

### 1. [Create a Map/Music ID](https://developer.apple.com/videos/play/wwdc2018/508/?time=155)
You can create the Map ID in the developer portal ([developer.apple.com](https://developer.apple.com)) in the `Certificates, Identifiers & Profiles` tab.

### 2. [Your Key ID](https://developer.apple.com/videos/play/wwdc2018/508/?time=220)
Next you will generate a new key. You will need the ID of this key to generate the JWT.

### 3. [Your Map/Music Private Key](https://developer.apple.com/videos/play/wwdc2018/508/?time=280)
Download the private key. You will only be able to download this once. Save it in a private, safe place. You can open this key file with a text editor and copy the entire contents of the file for inserting into `main.py`.
![Key ID](/images/KeyID.jpg)

### 4. Your Team ID.
You will need this ID to generate your JWT. You can get this under the `Membership` tab on the home page of the developer portal.
![Team ID](/images/TeamID.jpg)


## The Good Stuff
You probably just want an easy way to generate your JWT so you can move on with development. 😉 Fine, here is how you can use this program.

*Note: These directions are for macOS*

### Setup Python Environment
1. Clone this repository - `$ git clone git@github.com:addisonwebb/Apple-JWT-Generator.git`
2. Verify you have Python installed - `$ python --version` *Output will likely be `Python 2.7.10`*
3. Install pip - `$ sudo easy_install pip`
4. Install virtualenv - `$ sudo -H pip install virtualenv`
5. Change to the root directory of the project
6. Setup a virtual environment - `$ virtualenv env`
7. Begin using virtual environment - `$ source env/bin/activate`
8. Install [pyjwt](https://github.com/jpadilla/pyjwt/) - `$ pip install pyjwt`
9. Install [cryptography](https://github.com/pyca/cryptography) - `$ pip install cryptography`

### Using the program
1. Update `main.py` with the values for your Team ID, Key ID, and private key. Save the file.
2. Back in terminal run the program - `$ python main.py`

You should see output that looks like the following:
```
fyFhbEciOiJFUzI1NiIsInR5cC16IkpXVCIsImtpZCI6IkNTTFo2QjdNOFoifQ.eyJpc3MiOiJGSjRVQk02Uko3IiwiaWF0IjoxNTMwMDcwMtkyLjMyNQA4OSwiZXhwIjoxNTMwMDcxOTkyLjMyNDA4OX0.uveH2BifavlkJp8KLUPCHC0Eh9C6igaUdA6jIawW0r1wsOo44mNSq53e_bH8ZoB2JcNSqXqYvKVYEREi6S02gq
```

🎉 This is the JWT you use to authenticate requests via the MapKit JS and MusicKit JS. 


## Sources:
- [Getting and Using a MapKit JS Key (video)](https://developer.apple.com/videos/play/wwdc2018/508)
- [Getting Keys and Creating Tokens](https://developer.apple.com/documentation/applemusicapi/getting_keys_and_creating_tokens)
- [jwt.io](https://jwt.io)
- [pyjwt](https://github.com/jpadilla/pyjwt/)


