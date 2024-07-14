# Overview

The Menu Item Inquiry project is a web application designed to help users search and find detailed information about various restaurant menu items. Users can search for dishes, view their details, and learn more about the restaurants offering these dishes.

# Table of Contents 
 - Installation
 - Usage
 - Features
 - Technologies Used
 - Contributing
 - License
 - Installation

Follow these steps to install and set up the project locally.

# Prerequisites 
 - Python 3.x
 - Django 5.0
   
# Steps

## Clone the repository:

'''
git clone https://github.com/Niki-098/Menu_Item_Inquiry.git
cd Menu_Item_Inquiry
'''

## Install dependencies:

'''
pip install -r requirements.txt
'''

## Configure the environment variables:

Create a .env file in the project root and add necessary environment variables.

## Apply migrations:

'''
python manage.py migrate
'''

## Start the development server:

'''
python manage.py runserver
'''

## Access the application:

Open your web browser and go to http://127.0.0.1:8000/search.

# Usage

To use the application, follow these steps:

- Open the application in your web browser.
- Use the search bar to type in the name of a dish you are interested in.
- View the search results, which will display the details of the dish and the restaurant offering it.
  
## Example

- Go to http://127.0.0.1:8000/search.
- Enter "Aloo Paratha" in the search bar and press Enter.
- The results will display detailed information about "Aloo Paratha," including the restaurant name, address, cuisines, average cost for two, user rating, and online delivery availability.
  
# Features

- Search for menu items: Easily search for dishes by name.
- Detailed information: View comprehensive details about dishes and restaurants.
- User ratings: See user ratings for each dish.
- Online delivery: Check if the restaurant offers online delivery.
  
# Technologies Used

- Django: Backend framework
- HTML/CSS/JavaScript: Frontend technologies
- SQLite: Database 

# Contributing

We welcome contributions! Follow these steps to contribute:

## Fork the repository:

- Click the "Fork" button at the top right of the repository page.

## Create a new branch:

'''git checkout -b feature/your-feature'''
  
## Commit your changes:

''' git commit -am 'Add new feature'''
  
## Push to the branch:

'''git push origin feature/your-feature'''
  
## Submit a pull request:

- Open a pull request on the original repository and provide a detailed description of your changes.

# Requirements

Here's the requirements.txt file for your project:

- Django==5.0
- Python==3.12.0







