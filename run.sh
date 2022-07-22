#!/bin/sh
while [ true ]
do   
    echo $FILENAME
    python data_gen.py $NUM_RECORD $FILENAME
    ls
    chmod +x ./bulk_insert_app/mockDatagen
    ./bulk_insert_app/mockDatagen $FILENAME
    rm -r $FILENAME
done