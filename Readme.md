Create an application that accesses the API for data about the International Space Station (ISS) at the following URL:
http://api.open-notify.org/

API documentation can be found here:

http://open-notify.org/Open-Notify-API/

Primary Skills:

Use the API documentation to do one or more of the following
Display the coordinates of the current location of ISS
Display the number of people currently in space
Challenge Skills:

Build a web app that shows a map of the current location of ISS.

---

In this challenge part of the task I am going to build a web application that
shows a map of the current location of the International space Station (ISS).
For doing this project I am going to use Python web framework like Flask and
javascript library like Leaflet and another python library called as folium.
Lets discuss some thing about the library I used.

FLASK and FOLIUM
Flask is a python web framework that allows developers to build web applications quickly and easily. Flask provides a wide range of features, including
URL routing, templating and support for various web technologies such as
HTTP, Websockets and more.
FOLIUM is a another amazing python library used for creating interactive
maps and visualizations. It is built on top of the widely-used mapping library
Lefleat.js and allows developers to create interactive maps with features like
markers, popups etc.

---

EXPLANATION OF THIS WEB APPLICATION PROGRAM:
The code that I have written is a python script along with HTML and CSS for
web application that displays the current location of ISS on a map using the
flask web framework and the folium python library which is used to display the
map.

The python script creates a flask application instance and defines a single
route for the root URL ‘/’ when a user visits the root URL, the index () function
is called and the following actions are performed:
• First sends a HTTP request to the open-notify.org (http://api.open-notify.org/iss-now.json) API to get the current location of the ISS in JSON
format.
• Extracts the longitude and latitude coordinates of the ISS from the json
response.
• Uses the Folium library to create a leflet map centered on the ISS coordinates and adds a marker to the map to indicate the location of the
ISS.
• Renders an HTML template index.html (which I will describe below)
and passes the map as a string(HTML) and the latitude and longitude
as variables to the template.
• Returns the rendered templates as the response to the user’s request.
Finally, if*name* == ‘_main_’ block at the end of the program runs the flask
application in debug mode.

---

Explanation of index.html:

This HTML script display a webpage that show the live location of the ISS on
a map. It also display current longitude and latitude coordinates of ISS.
Lets discuss about the elements used in the HTML program above.
The first element is the <head> section, which includes the metadata and links
to the external resources. In this program it contains a reference to the Leaflet
Javascript library which is used to display the map. I found the source, integrity codes from the website https://cdnjs.com/libraries/leaflet (cdnjs). Cdnjs is a
free and open sources software content delivery network hosted by cloudflare.
Cdnjs provides a comprehensive collection of client-side libraries and frameworks, including javascript, css and images for web developers.
The <body> section of the program includes the content that is displayed on
the page. This includes a title, some describing the ISS and its orbit and the
map itself.
The program also includes <script> section that references the lefleat library
and provides additional javascript code to control the behaviour of the map.
