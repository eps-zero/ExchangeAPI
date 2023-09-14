# ExchangeAPI

The Currency Converter API is a simple RESTful web service that allows you to convert currency from one to another. It provides real-time exchange rates and can convert a specified amount from one currency to another.

## Getting Started

These instructions will help you get the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python (3.6 or higher)
- pip (Python package manager)

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/eps-zero/ExchangeAPI.git
   cd ExchangeAPI
   ```

2. Install the required dependencies by running:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables. Create a `.env` file and set the following variables:

   - `API_URL`: The URL of the external service providing exchange rates.
   - `API_KEY`: Your API key for the external service (if required).

4. Run the application:

   ```bash
   flask app.py
   ```

   The application will start on `http://localhost:5000`.

## Usage

### Convert Currency

- **Endpoint**: `/api/rates`
- **HTTP Method**: GET

#### Request Parameters

- `from` (required): The code of the source currency (e.g., USD).
- `to` (required): The code of the target currency for conversion (e.g., RUB).
- `value` (optional): The amount of currency to convert. If not provided, it defaults to 0.

#### Example Request

```
GET /api/rates?from=USD&to=RUB&value=1
```

#### Example Response

```
{
    "result": 62.16
}
```

### Error Handling

- `400 Bad Request`: Returned if the input is invalid or required parameters are missing.
- `500 Internal Server Error`: Returned if the application fails to fetch exchange rates or encounters an internal error.

## Notes

- Make sure to provide valid currency codes (`from` and `to`) and, if necessary, an amount of currency to convert (`value`).
- If the API fails to execute a request or fetch up-to-date exchange rates, it will return an appropriate error message.
- The API runs on a local server and relies on environment variables for exchange rate data. Ensure that the `API_URL` and `API_KEY` environment variables are correctly configured before using the API.
