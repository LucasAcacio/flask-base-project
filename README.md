# Install dependencies:

    pip install -r requirements.txt

# Migrations

    flask db init
    flask db migrate -m "New migration"
    flask db upgrade

# Run

    *You may want to use a .env to load your variables*
    flask run

# Docker

    docker build -t myflask --build-arg CONFIG=config.PrdConfig .
    docker run -d -p 80:5000 myflask
