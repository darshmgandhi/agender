# Agender
Our project "Agender" is a website where users can build forms and incorporate the functionality of predicting Age and Gender of the person filling the form using the verification process. We have used Convolutional Neural Network, to predict Age and Gender of the person.

### Contents:
1. Pages
2. How to run server
3. Contribution Guidelines
4. Contributors
5. Licence

## Pages
 - Login/SignUp
 - Form Builder
 - Form to enter user data
 - Verification Page

## How to run the server on your local machine:
1. Download the docker-compose.yml file that has been uploaded.
2. Make sure you have Docker and docker-compose installed on your machine.
3. Navigate to the directory where you have downloaded the docker-compose.yml file and run the command
   "docker-compose up -d".
4. The project will take 3-4 minutes to start.
5. Use any modern browser (Firefox, Chrome, etc) of your choice and navigate to "localhost:8000\signup".
6. Create an account by entering a username, email, password (minimum 8 characters with at least 1 Uppercase character, 1 lower case character and 1 special character).
7. Now click on login and enter you username and password.
8. After logging, in you are presented with a dashboard (\new_page route) where you the following options: <br>

   a. Form builder - Here you can build your custom forms and save them. We have a dedicated button to add camera verification field for gender and age detection.

   b. Form Page - Here you can see the created forms and fill them. After clicking on submit, you will be taken to the gender and age verification (webcam) page. In this page you can click your photo, agree to the terms and conditions after which the gender and age verification will be done.

   c. Logout - You can use this button to log out. 

<b> *** Notes ***</b> <br>

a. The container can take some time to boot up because of the Machine Learning models that have been used for gender and age verification. <br>

b. You can only navigate to the dashboard (\new_page) if you are logged in. <br>

c. There is a not homepage (\ route) so please use (\signup) or (\login) instead. <br>

## Contribution Guidelines:-
Contributions are always welcome! Please ensure your pull request adheres to the following guidelines:
   1. Alphabetize your entry.
   2. Search previous suggestions before making a new one, as yours may be a duplicate.
   3. Suggested READMEs should be beautiful or stand out in some way.
   4. Make an individual pull request for each suggestion.
   5. New categories or improvements to the existing categorization are welcome.
   6. Keep descriptions short and simple, but descriptive.
   7. Start the description with a capital and end with a full stop/period.
   8. Check your spelling and grammar.
   9. Make sure your text editor is set to remove trailing whitespace.

## Contributors
- Darsh Gandhi - [Connect on Github](https://github.com/darshmgandhi) 
- Anoop Gupta - [Connect on Github](https://github.com/Anoop01234)
- Muskan Goel - [Connect on Github](https://github.com/muskan-goel)
- Kailash Karthik - [Connect on Github](https://github.com/KailashKS)


## Copyright (c) [2020] [Team - Agender]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
