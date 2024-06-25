# Secure Chat Application

## Overview

The Secure Chat Application is a Python-based encrypted messaging tool designed to ensure secure communication between users. This application provides end-to-end encryption, message integrity verification, and user authentication to protect sensitive conversations from unauthorized access.

## Features

- End-to-end encryption of messages using strong cryptographic algorithms.
- User authentication to ensure only authorized users can access the chat.
- Secure key exchange protocol to establish secure communication channels.
- Message integrity verification to detect tampering or unauthorized changes.
- User-friendly command-line interface for ease of use.
- Optional integration with public key infrastructure (PKI) for enhanced security.

## Requirements

- Python 3.x
- `cryptography` library for encryption and decryption
- `sqlite3` library for user management and authentication

## Installation

1. Clone the repository:
    ```bash
    https://github.com/Aravjnth/Secure-chat-application.git
    cd secure-chat-application
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Start the server to handle chat connections:
    ```bash
    python server.py
    ```

2. Start the client application to join the chat:
    ```bash
    python client.py
    ```

3. Follow the on-screen instructions to set up your username, connect to the server, and start chatting securely.

### Example

Start the server:
```bash
python server.py
```

Start the client and connect to the server:
```bash
python client.py
```

## Options

- Customize server settings and configurations in `config.py`.
- Modify encryption settings and algorithms in `crypto_utils.py`.

## Legal Disclaimer

This Secure Chat Application is intended for educational purposes and secure communication within authorized environments. It should not be used for malicious or unlawful activities. The developers assume no liability for any misuse or damage caused by this application.

## Contributing

Contributions to this project are welcome! Fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, please contact me at www.linkedin.com/in/aravinth-aj
