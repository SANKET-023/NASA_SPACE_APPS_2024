

# Farm-Buddy

**Farm-Buddy** is a web application designed to empower farmers with data-driven insights for enhanced agricultural productivity. The platform provides **geospatial data visualization** for factors like precipitation, wind speed, temperature, and other meteorological conditions to assist in crop planning. It offers **natural calamity alerts** and **crop recommendations**, including resilient crop suggestions, using NASA data sources.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [System Requirements](#system-requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Security and Privacy Implications](#security-and-privacy-implications)
7. [Environmental Implications](#environmental-implications)
8. [Ethical Implications](#ethical-implications)

---

### Project Overview

**Farm-Buddy** is tailored for farmers seeking guidance on crop management and resilience against environmental challenges. By offering real-time geospatial insights and customized recommendations, the platform aids in making informed decisions to boost productivity and protect crops from natural hazards.

### Features

1. **Geospatial Data Visualization**:
   - Displays key meteorological parameters like precipitation, temperature, and wind speed.
   - Provides visual overlays based on farm location to help farmers understand climate impact.

2. **Crop Recommendations**:
   - Offers crop recommendations based on local soil and climate data, enabling farmers to select optimal crops.
   - Suggests drought-resilient crops if a region is prone to low rainfall or droughts.

3. **Natural Calamity Alerts**:
   - Provides notifications of potential natural calamities, giving farmers time to safeguard crops.
   - Alerts include flood, drought, and storm warnings, using NASA weather and climate data.

4. **Location-based Analytics**:
   - Automatically detects farm location and farm size (user-provided) for tailored recommendations.

5. **MQTT and Pub/Sub Architecture**:
   - Implements a message-passing system to deliver real-time updates on weather and alerts efficiently.

### System Requirements

- **Python 3.8+**
- **Flask**
- **MongoDB**
- **NASA Earthdata API** (for meteorological data)
- **MQTT** broker (e.g., Mosquitto)

#### Hardware Requirements
- Stable internet connection for real-time data updates and alert notifications.
- Any modern laptop or desktop for running the application server.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/farm-buddy.git
   cd farm-buddy
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up MongoDB**:
   - Install and start MongoDB, then create a database named `farm_buddy` with a collection named `users`.

4. **NASA API Key**:
   - Register for a NASA Earthdata account and obtain an API key.
   - Add the API key to the `.env` file.

5. **MQTT Broker**:
   - Set up an MQTT broker like Mosquitto to handle Pub/Sub messages for real-time data updates.

6. **Run the Application**:
   ```bash
   flask run
   ```

7. **Access the Application**:
   - Open a web browser and navigate to `http://127.0.0.1:5000`.

### Usage

1. **Register an Account**:
   - Visit the registration page and provide basic information like farm location, size, and crop preferences.

2. **View Geospatial Data**:
   - After logging in, navigate to the dashboard to view real-time geospatial data visualizations based on your farm’s location.
   - Use filters to adjust the display for specific parameters, such as temperature, rainfall, or wind speed.

3. **Crop Recommendations**:
   - Based on your farm data, the application provides crop recommendations tailored to soil type, climate, and regional trends.
   - In case of anticipated droughts, it suggests drought-resilient crop alternatives.

4. **Receive Alerts**:
   - If there’s a risk of natural calamity, a notification will appear in the dashboard, along with recommended actions.

5. **Customize Preferences**:
   - In the settings, you can adjust preferences like notification frequency, preferred crop types, and data update frequency.

### Security and Privacy Implications

Farm-Buddy collects and processes sensitive data, making security and privacy a priority:

1. **Data Privacy**:
   - Farm data, including location and preferences, is securely stored in MongoDB.
   - Ensure compliance with data privacy standards (e.g., GDPR) to protect farmers’ personal information.

2. **Network Security**:
   - MQTT messaging is secured with SSL/TLS to protect against data breaches.
   - API keys and other credentials are securely managed using environment variables.

3. **User Authentication**:
   - Basic authentication is used to control access to user data and dashboards.

### Environmental Implications

Farm-Buddy has the potential to contribute positively to sustainable agriculture:

1. **Efficient Resource Use**:
   - By recommending appropriate crop types and practices based on local climate, the platform promotes efficient use of resources such as water and fertilizers, potentially reducing agricultural waste.

2. **Climate Adaptation**:
   - With features like drought-resistant crop recommendations, Farm-Buddy helps farmers adapt to changing climate conditions, mitigating potential losses due to extreme weather.

3. **Sustainable Practices**:
   - Encouraging data-driven decisions can lead to more sustainable agricultural practices, benefiting the environment and reducing the ecological footprint of farming.

### Ethical Implications

Farm-Buddy’s recommendations can impact farmers’ livelihoods, so it’s essential to consider ethical aspects:

1. **Fair Access to Information**:
   - Ensure that the platform remains accessible to farmers of all economic backgrounds, particularly those with limited technical literacy or internet access.

2. **Algorithmic Fairness**:
   - Crop recommendations should be unbiased and consider various factors that might impact different regions differently, ensuring fair support for all users.

3. **Transparency in Data Use**:
   - Inform users about how their farm data is collected, stored, and used. Consent should be clearly obtained during registration, and farmers should have the option to delete their data if they wish.

---

**Farm-Buddy** provides actionable insights for farmers, helping them to adapt to environmental changes and optimize crop selection, thereby fostering a more resilient and sustainable agricultural ecosystem.
