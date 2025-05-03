LA Fitness Company (Tri Duong)

Project Description

LA Fitness Company does not have a flexible application for users to browse and reserve a spot in their desired virtual workout classes when they cannot attend physical gym locations. Moreover, members of LA Fitness does not have a tool to schedule with their desired personal trainer. Therefore, I developed the protocol for LA Fitness Company so that users can book virtual classes or personal trainers through their account.

Install required libraries

$pip install pillow
$pip install pytest
To run program

Click the green triangle run icon in the top-right corner of the Pycharm window or

$python3 GUI.py
In the login prompt, use the following credentials (or create)

Username: mduong8
Password:  1111
Functionality

Create an account

Account will be saved in the user_registration.csv file after users click the Register button.

Book Classes

All booked classes will be saved in the user_bookings.csv file along with the user's information.

Schedule with Personal Trainer

A booked personal trainer will be saved in the user_bookings_trainer.csv file when the users hit Book button.

Data File

user_registration.csv

This csv file is created to store user's information when they register their accounts.This file also verify their credentials (username, password) for logging in the protocol.

Username	Password	First Name	Last Name	Phone
eden1	2222	Eden	Nguyen	1234567890
mduong8	1111	Tri	Duong	8583571805
emma2	3333	Emma	Smith	1236540987
ben4	4444	Ben	Smith	9098786552
user_bookings.csv

This csv file is created to store user's booked classes along with their information.

Username	First Name	Last Name	Phone Number	Booked Classes
eden1	Eden	Nguyen	1234567890	Yoga Class, Zumba Class
mduong8	Tri	Duong	8583571805	Yoga Class, Zumba Class
ben4	Ben	Smith	9098786552	Zumba Class, Pilates Class
user_bookings_trainer.csv

This csv file is created to store user's booked trainer along with their information.

Username	First Name	Last Name	Phone Number	Booked Trainer
eden1	Eden	Nguyen	1234567890	Khoa Pham
mduong8	Tri	Duong	8583571805	Linny Alexson
emma2	Emma	Smith	1236540987	Linny Alexson
Class

Variables

There are 5 instances variables in the User class:

username: private, string
password: private, string
firstname: private, string
lastname: private, string
phone: private, string
There are 6 instances variables in the ClassBooking class:

username: private, string
password: private, string
firstname: private, string
lastname: private, string
phone: private, string
selected_classes: public, list data type
There are 6 instances variables in the TrainerBooking class:

username: private, string
password: private, string
firstname: private, string
lastname: private, string
phone: private, string
selected_trainer_name: public, string
Methods

The User class has the following methods:

the dunder __init__method
the dunder __str__method
Each User instances has the following property:

firstname getter
firstname setter
lastname getter
lastname setter
username getter
username setter
password getter
password setter
phone getter
phone setter
The ClassBooking class has the following methods:

the dunder __init__method
the dunder __str__method
The TrainerBooking class has the following methods:

the dunder __init__method
the dunder __str__method
Auto testing

Run the following command to test the GUI.py. There are 3 test cases.

$pytest -v test.py
