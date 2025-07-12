# SignalHound: Decentralized Crypto-Alert System

SignalHound is a decentralized, serverless crypto-alert system designed to provide automated price notifications based on threshold-triggered smart contracts. Leveraging WebSockets, Chainlink oracles, and a completely serverless architecture, SignalHound ensures reliable, transparent, and tamper-proof alerts, eliminating the reliance on centralized services and their inherent vulnerabilities. Users define custom price thresholds for their desired cryptocurrencies, and when these thresholds are breached, smart contracts automatically trigger notifications delivered directly to their configured endpoints.

This project addresses the limitations of traditional crypto-alert services, which often suffer from single points of failure, data manipulation risks, and opaque alert mechanisms. SignalHound's decentralized approach leverages the immutability and transparency of the blockchain, providing a verifiable and trustworthy alert system. By using Chainlink oracles, we ensure accurate and up-to-date price feeds from reliable sources. The serverless architecture, implemented using cloud functions and decentralized storage, minimizes operational costs and maximizes uptime, making SignalHound a robust and cost-effective solution.

SignalHound empowers users to proactively manage their crypto portfolios by reacting swiftly to market movements. The system is built with extensibility in mind, allowing developers to easily integrate new cryptocurrencies, alert mechanisms, and thresholding strategies. The completely open-source nature of the project encourages community contributions and ensures ongoing development and improvement. By shifting the control and responsibility for price alerts to the user, SignalHound creates a more secure and transparent environment for cryptocurrency trading and investment.

## Key Features

*   **Decentralized Alert Logic:** Smart contracts on a supported blockchain (e.g., Ethereum, Polygon) define and enforce alert triggers, ensuring transparency and tamper-proof notifications.
*   **Chainlink Oracle Integration:** Utilizes Chainlink's decentralized price feeds to obtain accurate and reliable cryptocurrency prices, mitigating data manipulation risks. Example: The smart contract requests the current price of ETH/USD from a Chainlink oracle before evaluating the threshold.
*   **Serverless Architecture:** Employs cloud functions (e.g., AWS Lambda, Google Cloud Functions) to process WebSocket data and trigger smart contract interactions, eliminating server management overhead.
*   **WebSocket Data Streaming:** Subscribes to real-time cryptocurrency price data streams via WebSockets, providing low-latency price updates. A script receives data in JSON format, parses it, and invokes the smart contract when the price exceeds the threshold.
*   **Customizable Alert Thresholds:** Allows users to define their own price thresholds for various cryptocurrencies, tailoring alerts to their specific trading strategies. Users can set upper and lower bounds with configurable tolerances.
*   **Multi-Channel Notification Support:** Provides flexibility by allowing users to configure multiple notification channels, such as email, SMS, or push notifications via decentralized messaging apps.
*   **Threshold Trigger Management:** Stores and manages all threshold configurations and related trigger history within the smart contract. This guarantees immutability and transparency of each configured alert.

## Technology Stack

*   **Python:** The primary programming language for developing the serverless functions and WebSocket data processing logic.
*   **Web3.py:** A Python library for interacting with Ethereum-compatible blockchains, facilitating smart contract deployments and function calls.
*   **Chainlink:** Decentralized oracle network providing secure and reliable price feeds.
*   **Cloud Functions (AWS Lambda/Google Cloud Functions):** Serverless compute platform for executing event-driven code.
*   **WebSockets:** Real-time communication protocol for receiving cryptocurrency price data streams.
*   **Solidity (Smart Contracts):** Used to define the alert logic and store user configurations on the blockchain.

## Installation

1.  **Clone the Repository:**
    git clone https://github.com/uhsr/SignalHound.git
    cd SignalHound

2.  **Install Dependencies:**
    pip install -r requirements.txt

3.  **Install Hardhat**
    npm install --save-dev hardhat
    npx hardhat

4.  **Deploy Smart Contracts:**
    Deploy the smart contracts to a compatible blockchain network (e.g., Ethereum, Polygon testnet) using a tool like Hardhat or Truffle. Make sure to update the contract addresses in the configuration file after deployment. Remember to fund the contract with enough gas for the oracle calls.

5.  **Configure Cloud Functions:**
    Deploy the Python scripts as cloud functions (AWS Lambda or Google Cloud Functions). Configure the functions to trigger on WebSocket events and interact with the deployed smart contracts.

## Configuration

*   **Environment Variables:**
    *   `WEB3_PROVIDER_URI`: The URI of the Ethereum provider (e.g., Infura, Alchemy).
    *   `CONTRACT_ADDRESS`: The address of the deployed smart contract.
    *   `CHAINLINK_ORACLE_ADDRESS`: The address of the Chainlink oracle.
    *   `PRIVATE_KEY`: The private key of the account used to interact with the smart contract.
    *   `NOTIFICATION_ENDPOINT`: The URL of the notification service (e.g., email, SMS).

*   **Configuration File (config.json):**
    This file stores user-defined alert thresholds and notification preferences. For example:
    {
        "ETH/USD": {
            "upper_threshold": 3500,
            "lower_threshold": 2500,
            "notification_channel": "email",
            "email_address": "user@example.com"
        }
    }

## Usage

1.  **Smart Contract Interaction:**
    Use Web3.py to interact with the deployed smart contracts. For example, to set a new price threshold:

    from web3 import Web3

    w3 = Web3(Web3.HTTPProvider(os.environ.get("WEB3_PROVIDER_URI")))
    contract_address = os.environ.get("CONTRACT_ADDRESS")
    contract_abi = [...] # ABI of your smart contract
    contract = w3.eth.contract(address=contract_address, abi=contract_abi)
    account = w3.eth.account.from_key(os.environ.get("PRIVATE_KEY"))

    txn = contract.functions.setThreshold("ETH/USD", 3500).buildTransaction({
        'nonce': w3.eth.getTransactionCount(account.address),
        'gas': 200000,
        'gasPrice': w3.eth.gasPrice
    })

    signed_txn = account.sign_transaction(txn)
    txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    print(f"Transaction Hash: {txn_hash.hex()}")

2.  **WebSocket Data Processing:**
    The Python script subscribes to a WebSocket stream, parses the incoming data, and invokes the smart contract when a threshold is breached.

## Contributing

We welcome contributions to SignalHound! Please follow these guidelines:

*   Fork the repository.
*   Create a new branch for your feature or bug fix.
*   Write clear and concise commit messages.
*   Submit a pull request with a detailed description of your changes.
*   Adhere to the project's coding style and conventions.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/uhsr/SignalHound/blob/main/LICENSE) file for details.

## Acknowledgements

We would like to thank the Chainlink team for providing valuable resources and support. We also appreciate the contributions of the open-source community.