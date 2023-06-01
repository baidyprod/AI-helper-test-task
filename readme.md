# AI Assistant by baidy

## Features
* Chat understands conversation context
* Chat has information about current weekday
* Geolocation of shops is being scraped from shop website

## Installation:
* Clone the repository
* Create and activate virtual environment
* Create .env file and paste API Keys like this:
```.env
OPENAI_API_KEY="your api key"
PINECONE_API_KEY="your api key"
PINECONE_ENVIRONMENT_REGION="your api key"
```
* Open terminal in project folder and run:
1. ```bash
   pip install -r requirements.txt
   ```
2. ```bash
   python init_db.py
   ```
3. ```bash
   streamlit run main.py
   ```
4. To stop the app, press Control+C in the current terminal window
5. To restart the app, just run the last command, because the cloud db is already initialised!

That's it! Have fun :)

## Screenshots:
### Geolocation + current weekday questions
![picture alt](https://res.cloudinary.com/dbtmzypoa/image/upload/v1685623033/AI%20helper%20screenshots/i9cahs568fh219qgv3qf.png)
### FAQ questions
![picture alt](https://res.cloudinary.com/dbtmzypoa/image/upload/v1685623033/AI%20helper%20screenshots/fqgk4weo7vpkdz9d0gwu.png)
### Complex conversation
![picture alt](https://res.cloudinary.com/dbtmzypoa/image/upload/v1685568518/AI%20helper%20screenshots/w5qwhw6xay07yw9egmol.png)

## Future possible improvements:
* FAQ scraper, like locations_scraper.py
* Playing with prompt
* Javascript front-end
