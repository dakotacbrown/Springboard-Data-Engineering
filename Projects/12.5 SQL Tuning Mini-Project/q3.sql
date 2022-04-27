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

-- 3. List the names of students who have taken course v4 (crsCode).
WITH transcript_cte AS (SELECT studID FROM Transcript WHERE crsCode = @v4)
SELECT stu.name FROM Student AS stu INNER JOIN transcript_cte AS cte ON stu.ID = cte.studID;

/*
With problem 3, using a CTE was faster and more cost efficent than using a subquery.

# EXPLAIN ANALYZE SELECT name FROM Student WHERE id IN (SELECT studId FROM Transcript WHERE crsCode = @v4);
-> Inner hash join (student.id = `<subquery2>`.studId)  (cost=414.91 rows=400) (actual time=0.149..0.363 rows=2 loops=1)
    -> Table scan on Student  (cost=5.04 rows=400) (actual time=0.011..0.198 rows=400 loops=1)
    -> Hash
        -> Table scan on <subquery2>  (cost=0.26..2.62 rows=10) (actual time=0.001..0.001 rows=2 loops=1)
            -> Materialize with deduplication  (cost=11.51..13.88 rows=10) (actual time=0.102..0.103 rows=2 loops=1)
                -> Filter: (transcript.studId is not null)  (cost=10.25 rows=10) (actual time=0.048..0.094 rows=2 loops=1)
                    -> Filter: (transcript.crsCode = <cache>((@v4)))  (cost=10.25 rows=10) (actual time=0.047..0.093 rows=2 loops=1)
                        -> Table scan on Transcript  (cost=10.25 rows=100) (actual time=0.023..0.072 rows=100 loops=1)

# EXPLAIN ANALYZE WITH transcript_cte AS (SELECT studID FROM Transcript WHERE crsCode = @v4)
SELECT stu.name FROM Student AS stu INNER JOIN transcript_cte AS cte ON stu.ID = cte.studID;
-> Inner hash join (stu.id = transcript.studId)  (cost=411.29 rows=400) (actual time=0.178..0.449 rows=2 loops=1)
    -> Table scan on stu  (cost=0.50 rows=400) (actual time=0.011..0.252 rows=400 loops=1)
    -> Hash
        -> Filter: (transcript.crsCode = <cache>((@v4)))  (cost=10.25 rows=10) (actual time=0.087..0.133 rows=2 loops=1)
            -> Table scan on Transcript  (cost=10.25 rows=100) (actual time=0.052..0.110 rows=100 loops=1)
*/