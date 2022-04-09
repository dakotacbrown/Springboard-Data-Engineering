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

-- 5. List the names of students who have taken a course from department v6 (deptId), but not v7.
WITH keep_cte AS (
SELECT studId FROM Transcript, Course WHERE deptId = @v6 AND Course.crsCode = Transcript.crsCode AND studID NOT IN 
(SELECT studId FROM Transcript, Course WHERE deptId = @v7 AND Course.crsCode = Transcript.crsCode)
)
SELECT name FROM Student AS s INNER JOIN keep_cte AS kc ON s.id = kc.studId;

/*
Using nested subqueries is the slowest. However using one subquery within a CTE ran faster than the two subqueries.
The second subquery used in the NOT IN statement for both tests ran similarly however, overall the CTE was able to run faster than the other subquery.

# EXPLAIN ANALYZE SELECT * FROM Student, 
	(SELECT studId FROM Transcript, Course WHERE deptId = @v6 AND Course.crsCode = Transcript.crsCode
	AND studId NOT IN
	(SELECT studId FROM Transcript, Course WHERE deptId = @v7 AND Course.crsCode = Transcript.crsCode)) as alias
WHERE Student.id = alias.studId;
-> Filter: <in_optimizer>(transcript.studId,<exists>(select #3) is false)  (cost=4112.69 rows=4000) (actual time=0.906..5.412 rows=30 loops=1)
    -> Inner hash join (student.id = transcript.studId)  (cost=4112.69 rows=4000) (actual time=0.697..0.954 rows=30 loops=1)
        -> Table scan on Student  (cost=0.06 rows=400) (actual time=0.012..0.223 rows=400 loops=1)
        -> Hash
            -> Filter: (transcript.crsCode = course.crsCode)  (cost=110.52 rows=100) (actual time=0.590..0.663 rows=30 loops=1)
                -> Inner hash join (<hash>(transcript.crsCode)=<hash>(course.crsCode))  (cost=110.52 rows=100) (actual time=0.590..0.657 rows=30 loops=1)
                    -> Table scan on Transcript  (cost=0.13 rows=100) (actual time=0.007..0.055 rows=100 loops=1)
                    -> Hash
                        -> Filter: (course.deptId = <cache>((@v6)))  (cost=10.25 rows=10) (actual time=0.497..0.560 rows=26 loops=1)
                            -> Table scan on Course  (cost=10.25 rows=100) (actual time=0.489..0.540 rows=100 loops=1)
    -> Select #3 (subquery in condition; dependent)
        -> Limit: 1 row(s)  (cost=110.52 rows=1) (actual time=0.146..0.146 rows=0 loops=30)
            -> Filter: <if>(outer_field_is_not_null, <is_not_null_test>(transcript.studId), true)  (cost=110.52 rows=100) (actual time=0.146..0.146 rows=0 loops=30)
                -> Filter: (<if>(outer_field_is_not_null, ((<cache>(transcript.studId) = transcript.studId) or (transcript.studId is null)), true) and (transcript.crsCode = course.crsCode))  (cost=110.52 rows=100) (actual time=0.146..0.146 rows=0 loops=30)
                    -> Inner hash join (<hash>(transcript.crsCode)=<hash>(course.crsCode))  (cost=110.52 rows=100) (actual time=0.076..0.142 rows=34 loops=30)
                        -> Table scan on Transcript  (cost=0.13 rows=100) (actual time=0.001..0.051 rows=100 loops=30)
                        -> Hash
                            -> Filter: (course.deptId = <cache>((@v7)))  (cost=10.25 rows=10) (actual time=0.004..0.063 rows=32 loops=30)
                                -> Table scan on Course  (cost=10.25 rows=100) (actual time=0.002..0.049 rows=100 loops=30)

# EXPLAIN ANALYZE
WITH keep_cte AS (
SELECT studId FROM Transcript, Course WHERE deptId = @v6 AND Course.crsCode = Transcript.crsCode AND studID NOT IN 
(SELECT studId FROM Transcript, Course WHERE deptId = @v7 AND Course.crsCode = Transcript.crsCode)
)
SELECT name FROM Student AS s INNER JOIN keep_cte AS kc ON s.id = kc.studId;
-> Filter: <in_optimizer>(transcript.studId,<exists>(select #3) is false)  (cost=4112.69 rows=4000) (actual time=0.438..5.164 rows=30 loops=1)
    -> Inner hash join (s.id = transcript.studId)  (cost=4112.69 rows=4000) (actual time=0.229..0.478 rows=30 loops=1)
        -> Table scan on s  (cost=0.06 rows=400) (actual time=0.007..0.208 rows=400 loops=1)
        -> Hash
            -> Filter: (transcript.crsCode = course.crsCode)  (cost=110.52 rows=100) (actual time=0.132..0.204 rows=30 loops=1)
                -> Inner hash join (<hash>(transcript.crsCode)=<hash>(course.crsCode))  (cost=110.52 rows=100) (actual time=0.131..0.198 rows=30 loops=1)
                    -> Table scan on Transcript  (cost=0.13 rows=100) (actual time=0.006..0.055 rows=100 loops=1)
                    -> Hash
                        -> Filter: (course.deptId = <cache>((@v6)))  (cost=10.25 rows=10) (actual time=0.039..0.103 rows=26 loops=1)
                            -> Table scan on Course  (cost=10.25 rows=100) (actual time=0.033..0.083 rows=100 loops=1)
    -> Select #3 (subquery in condition; dependent)
        -> Limit: 1 row(s)  (cost=110.52 rows=1) (actual time=0.154..0.154 rows=0 loops=30)
            -> Filter: <if>(outer_field_is_not_null, <is_not_null_test>(transcript.studId), true)  (cost=110.52 rows=100) (actual time=0.153..0.153 rows=0 loops=30)
                -> Filter: (<if>(outer_field_is_not_null, ((<cache>(transcript.studId) = transcript.studId) or (transcript.studId is null)), true) and (transcript.crsCode = course.crsCode))  (cost=110.52 rows=100) (actual time=0.153..0.153 rows=0 loops=30)
                    -> Inner hash join (<hash>(transcript.crsCode)=<hash>(course.crsCode))  (cost=110.52 rows=100) (actual time=0.081..0.149 rows=34 loops=30)
                        -> Table scan on Transcript  (cost=0.13 rows=100) (actual time=0.002..0.052 rows=100 loops=30)
                        -> Hash
                            -> Filter: (course.deptId = <cache>((@v7)))  (cost=10.25 rows=10) (actual time=0.005..0.066 rows=32 loops=30)
                                -> Table scan on Course  (cost=10.25 rows=100) (actual time=0.002..0.051 rows=100 loops=30)

# EXPLAIN ANALYZE
WITH keep_cte AS (
SELECT studId FROM Transcript, Course WHERE deptId = @v6 AND Course.crsCode = Transcript.crsCode
),
remove_cte AS (
SELECT studId FROM Transcript, Course WHERE deptId = @v7 AND Course.crsCode = Transcript.crsCode
)
SELECT name 
FROM Student AS s 
INNER JOIN keep_cte AS kc 
	ON s.id = kc.studId
WHERE kc.studId NOT IN (SELECT studId FROM remove_cte);
-> Filter: <in_optimizer>(transcript.studId,<exists>(select #3) is false)  (cost=4112.69 rows=4000) (actual time=0.437..5.340 rows=30 loops=1)
    -> Inner hash join (s.id = transcript.studId)  (cost=4112.69 rows=4000) (actual time=0.235..0.475 rows=30 loops=1)
        -> Table scan on s  (cost=0.06 rows=400) (actual time=0.007..0.199 rows=400 loops=1)
        -> Hash
            -> Filter: (transcript.crsCode = course.crsCode)  (cost=110.52 rows=100) (actual time=0.139..0.210 rows=30 loops=1)
                -> Inner hash join (<hash>(transcript.crsCode)=<hash>(course.crsCode))  (cost=110.52 rows=100) (actual time=0.138..0.204 rows=30 loops=1)
                    -> Table scan on Transcript  (cost=0.13 rows=100) (actual time=0.006..0.053 rows=100 loops=1)
                    -> Hash
                        -> Filter: (course.deptId = <cache>((@v6)))  (cost=10.25 rows=10) (actual time=0.039..0.103 rows=26 loops=1)
                            -> Table scan on Course  (cost=10.25 rows=100) (actual time=0.033..0.083 rows=100 loops=1)
    -> Select #3 (subquery in condition; dependent)
        -> Limit: 1 row(s)  (cost=110.52 rows=1) (actual time=0.160..0.160 rows=0 loops=30)
            -> Filter: <if>(outer_field_is_not_null, <is_not_null_test>(transcript.studId), true)  (cost=110.52 rows=100) (actual time=0.160..0.160 rows=0 loops=30)
                -> Filter: (<if>(outer_field_is_not_null, ((<cache>(transcript.studId) = transcript.studId) or (transcript.studId is null)), true) and (transcript.crsCode = course.crsCode))  (cost=110.52 rows=100) (actual time=0.160..0.160 rows=0 loops=30)
                    -> Inner hash join (<hash>(transcript.crsCode)=<hash>(course.crsCode))  (cost=110.52 rows=100) (actual time=0.085..0.156 rows=34 loops=30)
                        -> Table scan on Transcript  (cost=0.13 rows=100) (actual time=0.002..0.053 rows=100 loops=30)
                        -> Hash
                            -> Filter: (course.deptId = <cache>((@v7)))  (cost=10.25 rows=10) (actual time=0.006..0.069 rows=32 loops=30)
                                -> Table scan on Course  (cost=10.25 rows=100) (actual time=0.002..0.054 rows=100 loops=30)
*/