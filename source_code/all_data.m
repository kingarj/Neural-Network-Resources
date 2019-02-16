% this data is taken from the film_data spreadsheet where
% filmdataS1 is from D2:P359 of the partial_films sheet
% filmdataS2 is from D2:V129 of the all_films sheet

partial_data = table2array(filmdataS1).';
partial_in = partial_data(2:13,:);
partial_t = partial_data(1,:);
total_data = table2array(filmdataS2).';
total_in = total_data(2:19,:);
total_t = total_data(1,:);