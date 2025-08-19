## amapweather

**Author:** aiguantoux
**Version:** 0.0.1
**Type:** tool

## Description  
A tool plugin for retrieving real-time weather information of Chinese cities using the Amap (Gaode Map) API. It supports fuzzy search for city names (e.g., inputting "Suining" matches "遂宁市") and returns structured weather data including temperature, humidity, wind direction, and more.  


## Prerequisites  
Before using this plugin, you need to:  
1. Obtain a valid Amap API key:  
   - Register a developer account at [Amap Open Platform](https://lbs.amap.com/).  
   - Create a new application and generate an API key with access to the "Weather Service" API.  


## Installation  
1. Package the plugin using the Dify CLI:  
   ```bash
   dify plugin package
   ```  
2. Upload the generated `.zip` file to your Dify platform via the "Plugins" management page.  


## Configuration  
1. Navigate to the plugin's settings page after installation.  
2. Under "Pre-authorized Credentials", enter your Amap API key in the `api_key` field.  
3. Save the configuration to activate the plugin.  


## Usage  

### In Workflows/Conversation Flows  
1. Add the `amapweather` tool to your workflow or conversation flow.  
2. Configure the input parameter:  
   - **Required Input:** `city` (city name, e.g., "北京市" or "Shanghai").  
     - Fuzzy search is supported (e.g., "遂宁" automatically matches "遂宁市").  

3. Execute the workflow or send a message containing the city name (e.g., "What's the weather in 广州?").  


## Response Format  
The plugin returns a JSON object with the following structure:  
```json
{
  "result": {
    "城市": "晋宁区",
    "天气": "阴",
    "更新时间": "2025-08-19 23:03:25",
    "温度": "19℃",
    "湿度": "85%",
    "省份": "云南",
    "风力": "≤3",
    "风向": "南"
  }
}
```  


## Troubleshooting  
- **"API Key not configured"**: Ensure a valid Amap API key is entered in the plugin settings.  
- **"City not found"**: Use a more specific name (e.g., "北京市" instead of "北京") or check if the city is supported.  
- **API timeout**: Verify network connectivity or retry later.  


## Notes  
- Supports most cities and districts in China.  
- Weather data is provided by Amap and updated in real-time.  
- Ensure your Amap API plan covers the required request volume for your use case.