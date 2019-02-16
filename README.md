# Neural Network Resources #
These resources are to aid with the replication of an experiment into predicting the Academy Awards with the use of a neural network.

## File breakdown ##
* raw_data - contains data scraped from Wikipedia
* source_code - contains the Matlab scripts for extracting and producing the results, also the specific networks trained by me.
	* all_data.m, final_predictions.m and verification.m - pull data from the film_data spreadsheet and format as required
	* networkA.mat and networkB.mat - created via use of the nntool with the following specification and given the partial_data and total_data respectively be trained on:
		* feed-forward backpropagating network
		* one hidden layer with ten neurons
	* wikipedia_scrape_formatting.py - custom Python script to turn the contents of several stacked Wikipedia tables into Excel-digestable data.
* film_data.xlsx - contains all the raw data for each award ceremony used in training the networks as well as statistics gleaned from this data e.g. the total number of Academy Awards nomination a film received
* network_performances.xlsx - benchmarks for each reasonable combination of architecture choices
* predictions.xlsx - recordings of the predictions as made by the each network and their conversion into percentages