const apiKey = 'de0f135e3854f55bfa0b680d5f0c6fb3'; // Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key

function getWeather() {
    const city = document.getElementById('city').value;
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

    fetch(url)
        .then(response => response.json())
        .then(data => showWeather(data))
        .catch(error => console.error('Error fetching weather data:', error));
}

function showWeather(data) {
    if (data.cod === '404') {
        document.getElementById('weather').innerHTML = 'City not found.';
        return;
    }

    const weather = `
        <h2>${data.name}, ${data.sys.country}</h2>
        <p>Temperature: ${data.main.temp} °C</p>
        <p>Weather: ${data.weather[0].description}</p>
        <p>Humidity: ${data.main.humidity}%</p>
        <p>Wind Speed: ${data.wind.speed} m/s</p>
    `;

    document.getElementById('weather').innerHTML = weather;
}