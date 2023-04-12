from flask import Flask, render_template #importing flask module of python and importing render_template function from flask!!!
#render_template is a function that allows developers to render HTML templates with dynamic data.
import requests
import folium  #python library for creating maps and visualizatioins on the web
app = Flask(__name__)

@app.route('/')
def index():
    # Send HTTP request to get ISS coordinates
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()
    latitude = float(data['iss_position']['latitude'])
    longitude = float(data['iss_position']['longitude'])
    
    
    # Creating a Leaflet map centered on the ISS coordinates
    m = folium.Map(location=[latitude, longitude], zoom_start=3)
    # This like Add a marker for the ISS
    folium.Marker(location=[latitude, longitude], icon=folium.Icon(icon='rocket')).add_to(m)
    # Render the map using a template and display latitude and longitude in webpage...
    #return render_template('index.html', map=m._repr_html_())
    return render_template('index.html', map=m._repr_html_(), latitude=latitude, longitude=longitude)

if __name__ == '__main__':
    app.run(debug=True)
