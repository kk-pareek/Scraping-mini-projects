# webscrap

Let's learn this tiny repo:

**app.py**:
- is the main program which runs independent of any other local module 
- uses requests module for making a get request on the IMDB web-page
- uses bs4 module for extracting the data about top 100 actresses on IMDB
- uses pandas module for framing the extracted data, and storing into a .csv file
- results in creation of file 'data.csv' on a successful run

![](/images/demo.png)


**Learning steps**:
- represents the stages one should refer in order to understand app.py as a beginner
- 1.get_all_links fetches all the href links available on our source web-page
- 2.get_specific_link fetches the specific links by specifying particular class name, in this case, fetching only the links to the profiles of top 100 actresses
- 3.get_actresses_name fetches only the names of the top 100 actresses





