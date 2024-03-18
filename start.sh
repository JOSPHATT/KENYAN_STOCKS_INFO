#!/bin/bash

python ./all_kenya_market_pricelist.py

sleep 1
echo "PRODUCED STOCKS.JSON FILE"
sleep 1
echo "NOW PROCESSING JSON FILE TO CSV"
echo "------------------------------"
sleep 1
python ./stocks_database.py
echo "PRODUCED stocks.csv FILE"
sleep 1
echo "OPENING stocks.csv FILE"
cat ./stocks.csv


