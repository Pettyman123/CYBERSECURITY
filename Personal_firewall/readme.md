# Personal Firewall

A personal firewall to monitor and control incoming and outgoing network traffic based on predetermined security rules using Python, Netfilter, and iptables.

![Screenshot 2024-07-15 092832](https://github.com/user-attachments/assets/6e83cefb-3283-487f-812f-5e8afc7a132e)


## Features

- **Packet Filtering**: Filter packets based on IP addresses, port numbers, and protocols.
- **Logging**: Log all blocked traffic for monitoring and analysis.
- **Customization**: Easily modify rules to fit specific security needs.
- **Script-Based Management**: Manage firewall rules through Python scripts.
- **Integration with iptables**: Utilize iptables for managing packet filtering.

## How It Works

1. **Initialization**: Clears existing iptables rules.
2. **Defining Rules**: Adds new rules to allow or block specific traffic.
3. **Applying Rules**: Applies the defined rules to control traffic.
4. **Logging**: Logs blocked traffic for insights into potential threats.

## Installation

1. Install Python and pip:
   ```sh
   sudo apt-get install python3 python3-pip
   ```

2. Ensure iptables is installed:
  
  ```sh
   sudo apt-get install iptables
  ```
3. Install the requirements.txt file
   ```sh
   pip install requirements.txt
   ```
## Contribution
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.For more information read the detailed documenation

## License

```This project is licensed under the MIT License.```

## CREATED BY GOURAV SHARMA
