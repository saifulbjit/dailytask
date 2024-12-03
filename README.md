[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](https://choosealicense.com/licenses/mit/)

# SnapReq: A CLI-Based API Client for Simplified API Testing

**SnapReq** is a command-line tool designed to simplify API testing and interactions, similar to Postman but entirely in the terminal. With SnapReq, you can easily perform **GET**, **POST**, **PUT**, **PATCH**, and **DELETE** requests on any provided URL. It supports adding headers, query parameters, or payloads and allows saving responses to files.

---

## Key Features

- **Support for All HTTP Methods**: Perform `GET`, `POST`, `PUT`, `PATCH`, and `DELETE` requests.
- **Custom Headers**: Add request headers using the `--headers` option.
- **Query Parameters and Data Payloads**:
  - Use `--params` for query parameters in `GET` requests.
  - Use `--data` for payloads in other methods.
- **Response Management**:
  - Save responses to a file with the `--output` option.
  - View response headers using `--show-headers`.
- **User-Friendly Help**:
  - `snapr --help` provides an overview of available commands.
  - `snapr <method> --help` shows specific options for each HTTP method.

---

## Installation

SnapReq is available on PyPI. Install it using `pip`:

```bash
pip install snapreq
```

---

## Usage

### Command Overview

To see all available commands, use:

```bash
snapr --help
```

**Output:**

```
usage: snapr [-h] {get,post,put,patch,delete} ...

SnapReq: A simple API Client

options:
  -h, --help            show this help message and exit

commands:
  {get,post,put,patch,delete}
    get                 Make a GET request
    post                Make a POST request
    put                 Make a PUT request
    patch               Make a PATCH request
    delete              Make a DELETE request
```

### Performing Requests

SnapReq provides detailed help for each HTTP method. Below are examples for each method:

---

#### **GET Request**

Make a `GET` request with query parameters, headers, and optional response output.

```bash
snapr get --params "key1=value1&key2=value2" --headers "Authorization=Bearer token" --output response.json https://api.example.com/data
```

**Get Method Help**:
```bash
snapr get --help
```

**Output**:
```
usage: snapr get [-h] [--headers HEADERS] [--show-headers] [--output OUTPUT] [--params PARAMS] url

positional arguments:
  url                   API endpoint URL

options:
  -h, --help            show this help message and exit
  --headers HEADERS     Headers as a string of key-value pairs (e.g. header1=value1&header2=value2)
  --show-headers, -sh   Show response headers
  --output OUTPUT, -o OUTPUT
                        Output file path
  --params PARAMS, -p PARAMS
                        Query parameters as a string of key-value pairs (e.g. key1=value1&key2=value2)
```

---

#### **POST Request**

Make a `POST` request with data, headers, and optional response output.

```bash
snapr post --data "key1=value1&key2=value2" --headers "Content-Type=application/json" --output response.json https://api.example.com/data
```

**Post Method Help**:
```bash
snapr post --help
```

**Output**:
```
usage: snapr post [-h] [--headers HEADERS] [--show-headers] [--output OUTPUT] [--data DATA] url

positional arguments:
  url                   API endpoint URL

options:
  -h, --help            show this help message and exit
  --headers HEADERS     Headers as a string of key-value pairs (e.g. header1=value1&header2=value2)
  --show-headers, -sh   Show response headers
  --output OUTPUT, -o OUTPUT
                        Output file path
  --data DATA, -d DATA  Payload as a string of key-value pairs (e.g. key1=value1&key2=value2)
```

---

#### **PUT Request**

Make a `PUT` request similar to `POST`, using the `--data` option for payload.

```bash
snapr put --data "key1=value1" --headers "Authorization=Bearer token" https://api.example.com/data
```

---

#### **PATCH Request**

Make a `PATCH` request to partially update resources.

```bash
snapr patch --data "field=value" --headers "Authorization=Bearer token" https://api.example.com/data
```

---

#### **DELETE Request**

Perform a `DELETE` request to remove resources.

```bash
snapr delete --headers "Authorization=Bearer token" https://api.example.com/resource
```

---

## Advanced Options

- **Show Response Headers**:
  Use `--show-headers` (or `-sh`) to print response headers to the console.
  ```bash
  snapr get --headers "Authorization=Bearer token" --show-headers https://api.example.com/data
  ```

- **Save Response**:
  Use `--output` (or `-o`) to save the response body to a file.
  ```bash
  snapr get --output response.json https://api.example.com/data
  ```

---

## Examples

### Example 1: GET Request with Parameters and Headers

```bash
snapr get --params "search=python&limit=10" --headers "User-Agent=SnapReq" https://api.example.com/search
```

---

### Example 2: POST Request with Data and Response File

```bash
snapr post --data "key1=value1&key2=value2" --headers "Content-Type=application/json" --output post_response.json https://api.example.com/resource
```

---

## Contributing

Contributions are welcome! If you encounter any bugs or have feature suggestions, feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.