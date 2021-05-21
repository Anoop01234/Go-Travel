# Go-Travel Website
Our project “Advance Intelligent Tourist Guide" is an umbrella for all the globetrotters, tourists, casual weekend planners, etc. It provides all the facilities to the tourists for booking their vacations and holidays for either business or pleasure purposes. Moreover, the purpose is to accessorize the solution with more advanced technologies such as social media, different applications & features, advertisements, etc which will mitigate the problem for both customers and the company to reach out to each other and discovering a single stop for everything with a plethora of favorable deals coming their way for the buyers.

### Contents:
1. Pages
2. How to run server
3. Contribution Guidelines
4. Contributors
5. Acknowledgement
6. Licence

## Pages
### Homepage
Here you will be able to view four metropolitan cities of India i.e. Delhi, Mumbai, Chennai and Kolkata. Also here is the page from where you can register user and Sign-in to our website. (P.S.- You wont be able to book a table in a restaurant unless you are signed in to our website)

![image](https://user-images.githubusercontent.com/42812907/118974810-ded71980-b990-11eb-9d40-66eeb76400b0.png)

#### Register page
![image](https://user-images.githubusercontent.com/42812907/118987559-fe287380-b99d-11eb-8039-6fbcc4a6d647.png)

#### Login Page
![image](https://user-images.githubusercontent.com/42812907/118988236-a2121f00-b99e-11eb-9a55-9815cd79a943.png)

#### Contact Us page
![image](https://user-images.githubusercontent.com/42812907/118988484-dbe32580-b99e-11eb-8789-6f100ba3269a.png)


And based on your interest you can visit any city and see complete tour guidelines for that particular city. So lets suppose you click Delhi, so you can view different Events, Places to Visit, Shops and Market and FAQs.

![image](https://user-images.githubusercontent.com/42812907/118974931-075f1380-b991-11eb-95b3-54b580623bf2.png)

### Restaurants
Here we'll have restaurants for 4 metropolitan cities i.e. Delhi Mumbai, Chennai and Kolkata. Example if user is visitng Delhi and s/he wishes to checkout latest restaurants in Delhi, so he could find it here. Also, s/he could book a table from out site if he is register to our website. So, Delhi restaurnats would like: 

![image](https://user-images.githubusercontent.com/42812907/118975022-23fb4b80-b991-11eb-9819-af9da639cf4b.png)

### Booking Restaurants
So lets say that you are signed in to our website and you want to book a table from our site, so you can book that from our site itself. 

![image](https://user-images.githubusercontent.com/42812907/118975525-b7cd1780-b991-11eb-86b3-063924c7e0aa.png)

### Must see the place
Here we'll have must see places to visit for 4 metropolitan cities i.e. Delhi Mumbai, Chennai and Kolkata. Example if user is visitng Delhi and s/he wishes to checkout all the places that s/he can visit during his/her visit to Delhi. And the page would look like:

![image](https://user-images.githubusercontent.com/42812907/118975297-7fc5d480-b991-11eb-9241-16d643163804.png)

### Events
Here we'll have events organised in the 4 metropolitan cities i.e. Delhi Mumbai, Chennai and Kolkata. Example if user is visitng Delhi and s/he wishes to checkout latest events that are being aired in Delhi, so he could find it here. And the page would look like:

![image](https://user-images.githubusercontent.com/42812907/118975324-87857900-b991-11eb-8d95-ef1877dd813c.png)

### Shops and markets
Here we'll have shops and amarkets for 4 metropolitan cities i.e. Delhi Mumbai, Chennai and Kolkata. Example if user is visitng Delhi and s/he wishes to checkout shops and markets in Delhi, so he could find it here. And the page would look like: 

![image](https://user-images.githubusercontent.com/42812907/118975365-910ee100-b991-11eb-9755-509ce01c89f0.png)

### FAQs
Here we'll have the general questions with answers and Travel related queries.

![image](https://user-images.githubusercontent.com/42812907/118975396-9b30df80-b991-11eb-9b43-3d9b451a296d.png)

### Admin page
Here is the inbuilt interface of Django Admin page, from here you can add all the restaurants, places to visit, events, shops and markets and others.

![image](https://user-images.githubusercontent.com/42812907/118975647-db905d80-b991-11eb-94ae-4dd11dab5d87.png)


## How to run the server on your local machine:
- Clone the repository in your local machine
- Open project in a code editor (Visual studio code, atom, pycharm, etc)
- Open terminal and run command "pip install -r requirements.txt"
- Activate the virtual environment
- In settings.py enter database credentials and database name
- Navigate where "manage.py" file is located and run command "python manage.py makemigrations", then "python manage.py migrate"
- At last run command "python manage.py runserver" to run server
- To access admin panel, create django superuser and add "/admin" in the url in the browesr


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
- Anoop Gupta - [Connect on Github](https://github.com/Anoop01234)
- Muskan Goel - [Connect on Github](https://github.com/muskan-goel)
- Anushree Krishania - [Connect on Github](https://github.com/anu180)
- Tanmay Chaturvedi - [Connect on Github](https://github.com/CreamDePie)


## Acknowledgement
We will always be grateful to <b>Prof. Manish Hurkat</b> and <b>Prof. Eswaran Narasimhan</b>  for his constructive feedbacks and supportive mentoring during this project. Thanks for being a good mentor and for guiding us on the right path.

## Copyright (c) [2020] [Team - GoTravel]

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
