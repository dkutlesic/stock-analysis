# Stocks - real time analysis

In this project, we analyze and compare the stock values.

## Web page
The web page can be found on the : [Link](https://646e2be8d9b4d204938d1af6--friendly-praline-8c0e3e.netlify.app/). It is deployed manually via `Netlify`.

## Assignment description

Design and implement a single page web application displaying a graph and a table containing
the performance and some statistics of 3 stocks of your choice (e.g., AAPL, MSFT, TSLA).

### Backend: 

* The path to backend scripts: `./stocks-backend`
* Locally, the backend is run on `Python 3.8.2`. (This version is not supported on Heroku, so the automatic `Python` version inference is done (`Python 3.11.3`))
* To run the backend, install packages from `requirements.txt`.
* The desired stocks' codes to be analyzed are in the file `stocks_of_interestest.py`
* The Flask app route methods that provide the data necessary for the graph and the table is in `process_data.py`. The fresh data is deployed with Heroku and the fronted targets the endpoints: [Graph data endpoint](https://stocks-dkutlesi.herokuapp.com/graph) and [Table data endpoint](https://stocks-dkutlesi.herokuapp.com/statistics)
* The script that obtains fresh data (last 2 weeks) using `yfinance` is in `get_data.py`. This script also contains getting mock data, which was used during the frontend and real-time updates testing.
* The subfolder `tests/` was used during the development to ensure that data is updated in real-time (`random_data_generator.py` generates random values, writes them to a file, from where the values are processed with `process_data.py` and presented at the frontend)

### Frontend:

* The path to the `Vue 3` project: `./stocks-frontend`
* The frontend consists of The plot and the Table components. These components poll new stocks data every 30 minutes (since the actual stocks' values are updated daily).