## Privacy

### Data Collection
This plugin collects and processes the following information to provide weather query services:
- **User Input Data**: The city name provided by the user when initiating a weather query (e.g., "Beijing", "Shanghai"). This data is used solely to locate the corresponding city and retrieve weather information.
- **API Interaction Data**: When communicating with the Amap API, necessary parameters such as the city's adcode (automatically derived from the user-provided city name) and timestamps are transmitted. These parameters are required for the API to return accurate weather data.


### Data Usage
- All collected data is used exclusively for the purpose of fetching real-time weather information for the user-specified city.
- The city name and derived adcode are temporary and are not stored beyond the duration of a single query session.
- Weather data retrieved from the Amap API (such as temperature, humidity, and wind conditions) is processed and returned to the user in a structured format, with no further usage or storage.


### Data Sharing
- The plugin shares the city's adcode (a geographic code) with Amap's API to retrieve weather data. This is done in accordance with Amap's developer terms of service.
- No user input data, weather results, or personal information is shared with any third parties other than Amap for the sole purpose of providing the service.


### Data Security
- The Amap API key used for authentication is stored securely through Dify's pre-authorized credential management system, ensuring it is not exposed to unauthorized parties.
- All data transmissions between the plugin and Amap's API are encrypted via HTTPS to prevent interception or tampering.


### User Rights
- Users have the right to refrain from providing city names if they do not wish to use the weather query service.
- Since no user data is stored by the plugin, there is no need for data deletion requests. All temporary data is discarded immediately after the query is completed.


By using this plugin, you acknowledge that you have read and understood this privacy policy, and consent to the collection and use of data as described above.