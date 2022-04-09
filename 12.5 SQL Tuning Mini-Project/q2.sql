USE springboardopt;

-- -------------------------------------
SET @v1 = 1612521;
SET @v2 = 1145072;
SET @v3 = 1828467;
SET @v4 = 'MGT382';
SET @v5 = 'Amber Hill';
SET @v6 = 'MGT';
SET @v7 = 'EE';			  
SET @v8 = 'MAT';

-- 2. List the names of students with id in the range of v2 (id) to v3 (inclusive).
EXPLAIN ANALYZE SELECT name FROM Student WHERE id BETWEEN @v2 AND @v3;

/*
With problem 2, the query is good as is. The bottom most query I completed shows that using logical operators takes longer to query.
The query above the bottom most query uses the actual numbers for ID and not the cached variables. That has the higest cost of all queries and are comparable to the worst run time.
The middle query is using an index on the name column and the run time was comparable or worse to the original query.
The top query, which is the same as the original query had the fastest or comparable run times.

EXPLAIN ANALYZE SELECT name FROM Student WHERE id BETWEEN @v2 AND @v3;
-> Filter: (student.id between <cache>((@v2)) and <cache>((@v3)))  (cost=5.44 rows=44) (actual time=0.025..0.262 rows=278 loops=1)
    -> Table scan on Student  (cost=5.44 rows=400) (actual time=0.019..0.221 rows=400 loops=1)

# EXPLAIN ANALYZE SELECT name FROM Student WHERE id BETWEEN @v2 AND @v3; (using index on name column)
-> Filter: (student.id between <cache>((@v2)) and <cache>((@v3)))  (cost=5.44 rows=44) (actual time=0.025..0.305 rows=278 loops=1)
    -> Table scan on Student  (cost=5.44 rows=400) (actual time=0.022..0.250 rows=400 loops=1)
    
# EXPLAIN ANALYZE SELECT name FROM Student WHERE id BETWEEN 1145072 AND 1828467;
-> Filter: (student.id between 1145072 and 1828467)  (cost=41.00 rows=44) (actual time=0.021..0.330 rows=278 loops=1)
    -> Table scan on Student  (cost=41.00 rows=400) (actual time=0.019..0.271 rows=400 loops=1)

EXPLAIN ANALYZE SELECT name FROM Student WHERE id >= @v2 AND id <= @v3;
-> Filter: ((student.id >= <cache>((@v2))) and (student.id <= <cache>((@v3))))  (cost=5.44 rows=44) (actual time=0.070..0.339 rows=278 loops=1)
    -> Table scan on Student  (cost=5.44 rows=400) (actual time=0.067..0.292 rows=400 loops=1)
*/


