# Raspberry Pi Flask GPIO API

GpioNet is a python flask application designed to remotely control GPIO pins with a API request

## Installation

Clone the repository
```bash
git clone <clone link>
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all required packages. found in 'requirements.txt'

```bash
pip3 install -r requirements.txt
```

## Usage

This application will bind to port 5002. You can change the IP/Port in the configuration file.

After configuration, run

```bash
python3 endpoint.py &
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)