#!/bin/bash

echo "########### Loading data to Mongo DB ###########"
mongoimport --jsonArray --db bank --collection sample --file /tmp/data_features_rf.json