# SignalHound - Real-time Anomaly Detection in Time Series Data

SignalHound is a Python-based tool designed for real-time anomaly detection in time series data streams. Leveraging statistical modeling and signal processing techniques, SignalHound identifies deviations from expected behavior, enabling proactive monitoring and alerting for critical applications. This repository provides a robust and extensible framework for analyzing data from diverse sources, ranging from network traffic and server performance metrics to financial transactions and sensor readings. The primary goal is to equip developers and data scientists with a readily deployable solution capable of detecting anomalies with high accuracy and minimal latency.

SignalHound is built upon the principle of continuous learning and adaptation. It utilizes a combination of statistical models, such as Exponential Moving Average (EMA) and Seasonal Trend decomposition using Loess (STL), to establish a baseline of normal behavior. New data points are then compared against this baseline, and any significant deviations are flagged as potential anomalies. The system is designed to automatically adjust to changing data patterns, minimizing false positives and ensuring accurate anomaly detection over time. SignalHound also includes features for visualizing detected anomalies, providing users with a clear understanding of the events triggering the alerts. Furthermore, the modular design allows for easy integration with existing monitoring systems and alert pipelines.

The benefits of using SignalHound include improved system reliability, reduced downtime, and enhanced security. By detecting anomalies in real-time, organizations can proactively address potential issues before they escalate into major problems. This can lead to significant cost savings, improved operational efficiency, and enhanced customer satisfaction. The tool's flexibility and scalability make it suitable for a wide range of applications, from small-scale projects to large enterprise deployments. Additionally, the open-source nature of SignalHound encourages community contributions and ensures continuous improvement and innovation.

## Key Features

*   **Real-time Anomaly Detection:** Implements algorithms for detecting anomalies in real-time data streams with configurable thresholds.
*   **Statistical Modeling:** Employs Exponential Moving Average (EMA) with configurable smoothing factors (alpha values) for dynamic baseline calculation.
*   **Seasonal Decomposition:** Utilizes Seasonal Trend decomposition using Loess (STL) from `statsmodels` library to handle time series data with seasonality. STL parameters such as `period` and `robust` are configurable.
*   **Thresholding:** Offers adaptive thresholding based on standard deviations from the rolling mean, allowing for adjustments to sensitivity via a multiplier (e.g., 3 standard deviations).
*   **Visualization:** Provides a matplotlib-based visualization module for plotting time series data and highlighting detected anomalies. `matplotlib.pyplot` is used for generating plots with anomaly points marked in red.
*   **Data Ingestion:** Supports data ingestion from various sources, including CSV files, databases, and real-time data streams via configurable data adapters.
*   **Alerting:** Integrates with alerting systems via configurable webhooks or email notifications. The alerting module uses the `requests` library to send HTTP requests to configured endpoints.

## Technology Stack

*   **Python:** The core programming language for the entire project, providing a versatile and widely adopted platform.
*   **NumPy:** Used for efficient numerical computations and array manipulation, essential for time series analysis.
*   **Pandas:** Provides data structures and data analysis tools for easy handling of time series data.
*   **Statsmodels:** A Python library that provides classes and functions for the estimation of many different statistical models. Utilized for Seasonal Trend decomposition using Loess (STL).
*   **Matplotlib:** A plotting library used for visualizing time series data and detected anomalies.
*   **Requests:** Python library for making HTTP requests to integrate with external systems for alerting.

## Installation

1.  Clone the repository:
    git clone https://github.com/uhsr/SignalHound.git

2.  Navigate to the project directory:
    cd SignalHound

3.  Create a virtual environment:
    python3 -m venv venv

4.  Activate the virtual environment:
    source venv/bin/activate (on Linux/macOS)
    venv\Scripts\activate (on Windows)

5.  Install the required dependencies:
    pip install -r requirements.txt

## Configuration

SignalHound uses environment variables for configuration. Create a `.env` file in the project root directory and define the following variables:

*   `DATA_SOURCE`: The path to the CSV file containing the time series data. Example: `DATA_SOURCE=data/time_series.csv`
*   `ANOMALY_THRESHOLD`: The number of standard deviations from the rolling mean to consider an anomaly. Example: `ANOMALY_THRESHOLD=3`
*   `EMAIL_ALERT_ENABLED`: Enable or disable email alerts (true/false). Example: `EMAIL_ALERT_ENABLED=false`
*   `EMAIL_RECIPIENT`: The email address to send alerts to. Example: `EMAIL_RECIPIENT=alerts@example.com`
*   `WEBHOOK_URL`: The URL for sending webhook alerts. Example: `WEBHOOK_URL=https://example.com/webhook`
*   `STL_PERIOD`: The period for STL decomposition. Example: `STL_PERIOD=24`

## Usage

1.  Run the `main.py` script:
    python main.py

This will load the time series data, detect anomalies, and optionally send alerts based on the configuration.

Example code snippet:
from signalhound import SignalHound
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]
hound = SignalHound()
anomalies = hound.detect_anomalies(data)
print(anomalies)

API Documentation:

The core class `SignalHound` provides the `detect_anomalies(data, threshold=3)` method. The `data` parameter is a list of numerical values representing the time series. The `threshold` parameter specifies the number of standard deviations for anomaly detection. The method returns a list of indices corresponding to the detected anomalies.

## Contributing

We welcome contributions to SignalHound! Please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Write clear and concise code with appropriate comments.
4.  Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/uhsr/SignalHound/blob/main/LICENSE) file for details.

## Acknowledgements

We would like to thank the open-source community for providing the libraries and tools that make SignalHound possible.