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

-- 6. List the names of students who have taken all courses offered by department v8 (deptId).
WITH v8_cte AS(
SELECT COUNT(*) AS ct, crsCode 
FROM Course
WHERE deptId = @v8
),
script_cte AS (
SELECT studId, COUNT(*) AS c, v.ct FROM Transcript AS t
	INNER JOIN v8_cte AS v
	ON t.crsCode = v.crsCode
GROUP BY studId
HAVING c = v.ct
)
SELECT name FROM Student AS s INNER JOIN script_cte AS c ON s.id = c.studId;

/*
Overall, the CTE runs faster. All of the subqueries were removed and cut the analyzation by a lot.

# EXPLAIN ANALYZE SELECT name FROM Student,
	(SELECT studId
	FROM Transcript
		WHERE crsCode IN
		(SELECT crsCode FROM Course WHERE deptId = @v8 AND crsCode IN (SELECT crsCode FROM Teaching))
		GROUP BY studId
		HAVING COUNT(*) = 
			(SELECT COUNT(*) FROM Course WHERE deptId = @v8 AND crsCode IN (SELECT crsCode FROM Teaching))) as alias
WHERE id = alias.studId;
-> Nested loop inner join  (cost=1041.00 rows=0) (actual time=5.040..5.040 rows=0 loops=1)
    -> Filter: (student.id is not null)  (cost=41.00 rows=400) (actual time=0.026..0.298 rows=400 loops=1)
        -> Table scan on Student  (cost=41.00 rows=400) (actual time=0.026..0.262 rows=400 loops=1)
    -> Covering index lookup on alias using <auto_key0> (studId=student.id)  (actual time=0.000..0.000 rows=0 loops=400)
        -> Materialize  (cost=0.00..0.00 rows=0) (actual time=4.676..4.676 rows=0 loops=1)
            -> Filter: (count(0) = (select #5))  (actual time=4.545..4.545 rows=0 loops=1)
                -> Table scan on <temporary>  (actual time=0.001..0.002 rows=19 loops=1)
                    -> Aggregate using temporary table  (actual time=4.541..4.543 rows=19 loops=1)
                        -> Nested loop inner join  (cost=1020.25 rows=10000) (actual time=0.200..0.360 rows=19 loops=1)
                            -> Filter: (transcript.crsCode is not null)  (cost=10.25 rows=100) (actual time=0.008..0.088 rows=100 loops=1)
                                -> Table scan on Transcript  (cost=10.25 rows=100) (actual time=0.007..0.075 rows=100 loops=1)
                            -> Single-row index lookup on <subquery3> using <auto_distinct_key> (crsCode=transcript.crsCode)  (actual time=0.000..0.001 rows=0 loops=100)
                                -> Materialize with deduplication  (cost=120.52..120.52 rows=100) (actual time=0.254..0.256 rows=19 loops=1)
                                    -> Filter: (course.crsCode is not null)  (cost=110.52 rows=100) (actual time=0.103..0.176 rows=19 loops=1)
                                        -> Filter: (teaching.crsCode = course.crsCode)  (cost=110.52 rows=100) (actual time=0.103..0.174 rows=19 loops=1)
                                            -> Inner hash join (<hash>(teaching.crsCode)=<hash>(course.crsCode))  (cost=110.52 rows=100) (actual time=0.102..0.170 rows=19 loops=1)
                                                -> Table scan on Teaching  (cost=0.13 rows=100) (actual time=0.004..0.053 rows=100 loops=1)
                                                -> Hash
                                                    -> Filter: (course.deptId = <cache>((@v8)))  (cost=10.25 rows=10) (actual time=0.013..0.075 rows=19 loops=1)
                                                        -> Table scan on Course  (cost=10.25 rows=100) (actual time=0.006..0.057 rows=100 loops=1)
                -> Select #5 (subquery in condition; uncacheable)
                    -> Aggregate: count(0)  (cost=211.25 rows=1000) (actual time=0.211..0.211 rows=1 loops=19)
                        -> Nested loop inner join  (cost=111.25 rows=1000) (actual time=0.117..0.208 rows=19 loops=19)
                            -> Filter: ((course.deptId = <cache>((@v8))) and (course.crsCode is not null))  (cost=10.25 rows=10) (actual time=0.005..0.079 rows=19 loops=19)
                                -> Table scan on Course  (cost=10.25 rows=100) (actual time=0.004..0.062 rows=100 loops=19)
                            -> Single-row index lookup on <subquery6> using <auto_distinct_key> (crsCode=course.crsCode)  (actual time=0.001..0.001 rows=1 loops=361)
                                -> Materialize with deduplication  (cost=20.25..20.25 rows=100) (actual time=0.122..0.125 rows=97 loops=19)
                                    -> Filter: (teaching.crsCode is not null)  (cost=10.25 rows=100) (actual time=0.002..0.074 rows=100 loops=19)
                                        -> Table scan on Teaching  (cost=10.25 rows=100) (actual time=0.002..0.064 rows=100 loops=19)
            -> Select #5 (subquery in projection; uncacheable)
                -> Aggregate: count(0)  (cost=211.25 rows=1000) (actual time=0.211..0.211 rows=1 loops=19)
                    -> Nested loop inner join  (cost=111.25 rows=1000) (actual time=0.117..0.208 rows=19 loops=19)
                        -> Filter: ((course.deptId = <cache>((@v8))) and (course.crsCode is not null))  (cost=10.25 rows=10) (actual time=0.005..0.079 rows=19 loops=19)
                            -> Table scan on Course  (cost=10.25 rows=100) (actual time=0.004..0.062 rows=100 loops=19)
                        -> Single-row index lookup on <subquery6> using <auto_distinct_key> (crsCode=course.crsCode)  (actual time=0.001..0.001 rows=1 loops=361)
                            -> Materialize with deduplication  (cost=20.25..20.25 rows=100) (actual time=0.122..0.125 rows=97 loops=19)
                                -> Filter: (teaching.crsCode is not null)  (cost=10.25 rows=100) (actual time=0.002..0.074 rows=100 loops=19)
                                    -> Table scan on Teaching  (cost=10.25 rows=100) (actual time=0.002..0.064 rows=100 loops=19)
                                    
# EXPLAIN ANALYZE
WITH v8_cte AS(
SELECT COUNT(*) AS ct, crsCode 
FROM Course
WHERE deptId = @v8
),
script_cte AS (
SELECT studId, COUNT(*) AS c, v.ct FROM Transcript AS t
	INNER JOIN v8_cte AS v
	ON t.crsCode = v.crsCode
GROUP BY studId
HAVING c = v.ct
)
SELECT name FROM Student AS s INNER JOIN script_cte AS c ON s.id = c.studId;
-> Nested loop inner join  (cost=241.00 rows=0) (actual time=0.572..0.572 rows=0 loops=1)
    -> Filter: (s.id is not null)  (cost=41.00 rows=400) (actual time=0.007..0.292 rows=400 loops=1)
        -> Table scan on s  (cost=41.00 rows=400) (actual time=0.007..0.246 rows=400 loops=1)
    -> Index lookup on c using <auto_key0> (studId=s.id)  (actual time=0.000..0.000 rows=0 loops=400)
        -> Materialize CTE script_cte  (cost=0.00..0.00 rows=0) (actual time=0.198..0.198 rows=0 loops=1)
            -> Filter: (c = '19')  (actual time=0.077..0.077 rows=0 loops=1)
                -> Table scan on <temporary>  (actual time=0.000..0.001 rows=1 loops=1)
                    -> Aggregate using temporary table  (actual time=0.075..0.075 rows=1 loops=1)
                        -> Filter: (t.crsCode = 'MAT796')  (cost=10.25 rows=10) (actual time=0.005..0.064 rows=1 loops=1)
                            -> Table scan on t  (cost=10.25 rows=100) (actual time=0.004..0.051 rows=100 loops=1)
*/