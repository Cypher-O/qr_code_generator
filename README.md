# QR Code Generator

A full-featured QR Code generator built with Django and Django REST Framework. This application provides both a web interface and API endpoints for generating QR codes from URLs or text.

## Features

- 🌐 Web interface for generating QR codes
- 🔄 RESTful API endpoints
- 📥 Downloadable QR codes
- 🎨 Clean, responsive UI
- 💾 Automatic QR code storage
- 🔗 URL validation
- 📱 Mobile-friendly design

## Tech Stack

- Python 3.11+
- Django 5.1.2
- Django REST Framework
- qrcode library
- Pillow (Python Imaging Library)

## Installation

1. Clone the repository: & navigate to the project directory

   ```sh
    git clone https://github.com/Cypher-O/qr_code_generator.git   
   ```

   ```sh
    cd qr_code_generator
   ```

2. Create and activate a virtual environment:

   ```sh
    python -m venv venv
   ```

   ```sh
    source venv/bin/activate
   ```

3. Install dependencies:

   ```sh
    pip install -r requirements.txt
   ```

4. Run migrations:

   ```sh
   python manage.py makemigrations
   ```

   ```sh
   python manage.py migrate
   ```

5. Generate Static files:

   ```sh
    python manage.py collectstatic
   ```

6. Run the server:

   ```sh
    python manage.py runserver
   ```

7. t

## Web Interface Usage

- Navigate to the homepage
- Enter a URL in the input field
- Click "Generate QR Code"
- View and download the generated QR code

## Project Structure

```
qr_code_generator/
├── apps/
│   └── generator/
│       ├── migrations/
|       ├── utils/
│           ├── __init__.py
│           └── api_response.py
|       ├── templates/
│           └── generator/
│           └── qr_code_generator.html
|       ├── static/
│           └── css/
│           └── styles.css
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── serializers.py
│       ├── urls.py
│       └── views.py
├── media/
│   └── qr_codes/
├── static/
├── manage.py
├── requirements.txt
└── README.md
```

## Development

1. Create branch for your feature

   ```sh
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit:

   ```sh
    git add .
    git commit -m "Add your feature description"
    ```

3. Push changes and create pull request:

   ```sh
   git push origin feature/your-feature-name
   ```

## Testing

Run tests with:

   ```sh
   python manage.py test
   ```

## Contributing

- Fork the repository
- Create your feature branch
- Commit your changes
- Push to the branch
- Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
Authors

Olumide Awodeji <olumide.awodeji@hotmail.com>

## Acknowledgments

- qrcode library developers
- Django and DRF teams
- Contributors and users
  