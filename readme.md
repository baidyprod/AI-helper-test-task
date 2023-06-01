# AI Assistant by baidy

## Features
* Chat understands conversation context
* Chat has information about current weekday
* Data about geolocation of shops is scraped

## Installation:
* Clone the repository
* Create and activate virtual environment
* Create an .env file and paste OpenAI API Key like this OPENAI_API_KEY="your api key"
* Open terminal and run:
1. ```bash
   pip install -r requirements.txt
   ```
2. ```bash
   python init_db
   ```
3. ```bash
   streamlit run main.py
   ```

That's it! Have fun :)

## Screenshots:
### Geolocation questions
![picture alt](https://res.cloudinary.com/dbtmzypoa/image/upload/v1685623033/AI%20helper%20screenshots/i9cahs568fh219qgv3qf.png)
### FAQ questions
![picture alt](https://res.cloudinary.com/dbtmzypoa/image/upload/v1685623033/AI%20helper%20screenshots/fqgk4weo7vpkdz9d0gwu.png)
### Complex conversation
![picture alt](https://res.cloudinary.com/dbtmzypoa/image/upload/v1685568518/AI%20helper%20screenshots/w5qwhw6xay07yw9egmol.png)

## Future possible improvements:
* FAQ scraper, like locations_scraper.py
* Playing with prompt
* Javascript front-end
