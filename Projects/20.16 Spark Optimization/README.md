# 20.16 Spark Optimizations

## Improving the performance of a Spark job:

1. By picking the right operators
    The best operators for this optimization were broadcast and caching. 
    Broadcast improved the joins while caching made sure to keep the dataframes in memory.

2. Reduce the number of shuffles and the amount of data shuffled
    Shuffles were reduced and optimized by choosing the number of partitions.

3. Tuning Resource Allocation
    By using broadcasting, caching, and reducing the number of partitions helped with what resources were used.

4. Tuning the Number of Partitions
    I wanted to utilize adaptive query execution, however on my local machine, it wasn't running as expected. 
    I reduced the number of partitions manually from 200 to 4.

5. Reducing the Size of Data Structures
    Understanding the size of the data structures affects how you use the broadcast join. 
    It's usually better to broadcast the smaller data structure.

6. Choosing Data Formats
    With the files already in a parquet format they were good with using spark.