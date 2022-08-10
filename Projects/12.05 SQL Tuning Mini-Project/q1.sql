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

-- 1. List the name of the student with id equal to v1 (id).
SELECT name FROM Student WHERE id = @v1;

/* 
With this query, the way it is written is the fastest run time. 
The bottom most query uses the ID without it being cached which is the longest time out of all of them.
The middle query uses an index on the name column, which is even with the query as is and sometimes runs slower.
The top query, the fastest query works because the ID is cached allowing faster lookup.

# EXPLAIN ANALYZE SELECT name FROM Student WHERE id = @v1;
-> Filter: (student.id = <cache>((@v1)))  (cost=41.00 rows=40) (actual time=0.062..0.248 rows=1 loops=1)
    -> Table scan on Student  (cost=41.00 rows=400) (actual time=0.016..0.217 rows=400 loops=1)

# EXPLAIN ANALYZE SELECT name FROM Student WHERE id = @v1; (using index on name column)
-> Filter: (student.id = <cache>((@v1)))  (cost=41.00 rows=40) (actual time=0.072..0.238 rows=1 loops=1)
    -> Table scan on Student  (cost=41.00 rows=400) (actual time=0.024..0.211 rows=400 loops=1)

# EXPLAIN ANALYZE SELECT name FROM Student WHERE id = 1612521;
-> Filter: (student.id = 1612521)  (cost=41.00 rows=40) (actual time=0.818..1.348 rows=1 loops=1)
    -> Table scan on Student  (cost=41.00 rows=400) (actual time=0.714..1.323 rows=400 loops=1)
*/