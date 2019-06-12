# portfolio
Personal Projects that I have completed of note.

serverless react app:
A basic react application running on the aws platform.  The application is not the focus in this case.  The main focus is the way the application is served to users.  The application contents are in an S3 bucket. Using route53 dns service, I connected a domain name that routes traffic to the S3 bucket the application sits. The folder containing the application is called 'game'.

The application can be viewed at www.spotaquarium.com

Here is a diagram of the serverless application:
![](images/Serverless_Site.jpg)

imgur_download_project:
I created this project to download pictures based on imgur urls located in a text file.  It works well and even has gaceful means handling 
broken links well!  If you would like to use the program, you must enter an absolute path to the txt file with imgur urls and an absolute path
to the location where you would like the pictures stored.

bitcoin_project:
I created this program to retrieve the current price of bitcoin and compare that to the value in United States Dollars.  I retrieved
the data from a website called Cryptocompare.com through their developer API.  I created this program to continuously execute while
I gave a presentation explaining bitcoin and blockchain technology in a business class a year ago.
