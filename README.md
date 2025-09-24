# Reddit Image Scraper

A simple Python project that scrapes image posts from a subreddit

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need Python 3.x installed on your system. Install required libraries with:

```pip install -r requirements.txt```

This will install:  
- `requests` → to fetch data from Reddit  
- `flask` → to run the optional web page

### Installing

1. Clone the repository:

```git clone https://github.com/YOUR_USERNAME/reddit-image-scraper.git```

```cd reddit-image-scraper```

2. Run the scraper to fetch posts:

```python scrapper.py```

- This will scrape ~10 pages from the subreddit and save posts with images into `output.json`.

3. (Optional) View posts in a simple web page:

```python app.py```


- Open your browser at `http://127.0.0.1:5000/` to see titles and images.

4. Repeat scraping as needed or change the subreddit in `scrapper.py`.

### End with demo

- Open `output.json` to see sample scraped data:

```json
[
  {
    "title": "Beautiful sunset in KL",
    "image_url": "https://i.redd.it/example.jpg"
  },
]
```

### Coding style

Code is formatted for readability; follow Python PEP8 style.

### Deployment

To deploy the Flask web page on a server, run app.py with Python and configure a web server (like Nginx) to forward requests to Flask.

## Built With

* [Python](https://www.python.org/) - Programming language
* [Requests](https://docs.python-requests.org/) - To fetch Reddit data
* [Flask](https://flask.palletsprojects.com/) - For optional web page

## Contributing

Please fork the repository and submit pull requests. Make sure to follow Python best practices.

## Versioning

We use [SemVer](http://semver.org/) for versioning. 

## License

This project is licensed under the MIT License - see the ```LICENSE.md``` file for details

## Acknowledgments

* Reddit API for providing JSON access
