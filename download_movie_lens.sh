curl -k https://files.grouplens.org/datasets/movielens/ml-25m.zip -o data_process/data/ml-25m.zip
yes | unzip -j data_process/data/ml-25m.zip ml-25m/tags.csv ml-25m/movies.csv ml-25m/ratings.csv -d data_process/data
rm -r -f data_process/data/ml-25m.zip
