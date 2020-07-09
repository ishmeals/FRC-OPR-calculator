# FRC OPR Calculator

Offensive power rating calculator for FRC. The math is based on [this great Blue Alliance post](https://blog.thebluealliance.com/2017/10/05/the-math-behind-opr-an-introduction/).

For google sheets. Use [this](https://docs.google.com/spreadsheets/d/1tBf0YKXdqrcKlKkN4dv1hALj7ZQSP9wOv6X00jebCD8/edit?usp=sharing) as a template. Copy the id of the spreadsheet (in the link of the copy) and paste it into the code.

Create an oAuth 2.0 Client ID [here](https://console.developers.google.com/). Download the client_secret.json, rename it as 'creds.json', and place it in the code folder.



## Imports

* Numpy for calculations
* os for session things
* Pickle for session things that I don't understand
* google-api-python-client, google-auth, google-auth-oauthlib for googly things 