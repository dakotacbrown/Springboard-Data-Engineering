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

-- 4. List the names of students who have taken a course taught by professor v5 (name).
WITH pt_cte AS (
SELECT crsCode, semester FROM Professor AS prof INNER JOIN Teaching AS tch
WHERE prof.name = @v5 AND prof.ID = tch.profID
),
transcript_cte AS (
SELECT studID, pcte.crsCode, pcte.semester FROM Transcript AS trn INNER JOIN pt_cte AS pcte
WHERE trn.crsCode = pcte.crsCode AND trn.semester = pcte.semester 
)
SELECT stu.name, tcte.studId, tcte.crsCode, tcte.semester FROM Student AS stu INNER JOIN transcript_cte AS tcte WHERE stu.id = tcte.studId;

/*
The fast querying method was creating a temp table, however without being able to analyze the the costs of creating the temp table, the CTE was the fastest method.
The original method was very slow due to the nested subqueries. Being able to put each subquery in its own CTE made things faster.

# EXPLAIN ANALYZE SELECT name FROM Student,
	(SELECT studId FROM Transcript,
		(SELECT crsCode, semester FROM Professor
			JOIN Teaching
			WHERE Professor.name = @v5 AND Professor.id = Teaching.profId) as alias1
	WHERE Transcript.crsCode = alias1.crsCode AND Transcript.semester = alias1.semester) as alias2
WHERE Student.id = alias2.studId;

-> Inner hash join (student.id = transcript.studId)  (cost=1313.72 rows=160) (actual time=37.646..37.646 rows=0 loops=1)
    -> Table scan on Student  (cost=0.03 rows=400) (never executed)
    -> Hash
        -> Inner hash join (professor.id = teaching.profId)  (cost=1144.90 rows=4) (actual time=37.624..37.624 rows=0 loops=1)
            -> Filter: (professor.`name` = <cache>((@v5)))  (cost=0.95 rows=4) (never executed)
                -> Table scan on Professor  (cost=0.95 rows=400) (never executed)
            -> Hash
                -> Filter: ((teaching.semester = transcript.semester) and (teaching.crsCode = transcript.crsCode))  (cost=1010.70 rows=100) (actual time=37.613..37.613 rows=0 loops=1)
                    -> Inner hash join (<hash>(teaching.semester)=<hash>(transcript.semester)), (<hash>(teaching.crsCode)=<hash>(transcript.crsCode))  (cost=1010.70 rows=100) (actual time=37.612..37.612 rows=0 loops=1)
                        -> Table scan on Teaching  (cost=0.01 rows=100) (actual time=37.376..37.444 rows=100 loops=1)
                        -> Hash
                            -> Table scan on Transcript  (cost=10.25 rows=100) (actual time=0.035..0.086 rows=100 loops=1)

# EXPLAIN ANALYZE
WITH pt_cte AS (
SELECT crsCode, semester FROM Professor AS prof INNER JOIN Teaching AS tch
WHERE prof.name = @v5 AND prof.ID = tch.profID
),
transcript_cte AS (
SELECT studID, pcte.crsCode, pcte.semester FROM Transcript AS trn INNER JOIN pt_cte AS pcte
WHERE trn.crsCode = pcte.crsCode AND trn.semester = pcte.semester 
)
SELECT stu.name, tcte.studId, tcte.crsCode, tcte.semester FROM Student AS stu INNER JOIN transcript_cte AS tcte WHERE stu.id = tcte.studId;
-> Inner hash join (stu.id = trn.studId)  (cost=1313.72 rows=160) (actual time=0.334..0.334 rows=0 loops=1)
    -> Table scan on stu  (cost=0.03 rows=400) (never executed)
    -> Hash
        -> Inner hash join (prof.id = tch.profId)  (cost=1144.90 rows=4) (actual time=0.318..0.318 rows=0 loops=1)
            -> Filter: (prof.`name` = <cache>((@v5)))  (cost=0.95 rows=4) (never executed)
                -> Table scan on prof  (cost=0.95 rows=400) (never executed)
            -> Hash
                -> Filter: ((tch.semester = trn.semester) and (tch.crsCode = trn.crsCode))  (cost=1010.70 rows=100) (actual time=0.306..0.306 rows=0 loops=1)
                    -> Inner hash join (<hash>(tch.semester)=<hash>(trn.semester)), (<hash>(tch.crsCode)=<hash>(trn.crsCode))  (cost=1010.70 rows=100) (actual time=0.305..0.305 rows=0 loops=1)
                        -> Table scan on tch  (cost=0.01 rows=100) (actual time=0.005..0.069 rows=100 loops=1)
                        -> Hash
                            -> Table scan on trn  (cost=10.25 rows=100) (actual time=0.106..0.161 rows=100 loops=1)
                            
CREATE TEMPORARY TABLE prof_script AS
SELECT studId FROM Transcript AS ts,
(SELECT crsCode, semester FROM Professor AS p INNER JOIN Teaching AS t WHERE p.name = @v5 AND p.id = t.profID) as Alias
WHERE ts.crsCode = Alias.crsCode AND ts.semester = Alias.semester;
EXPLAIN ANALYZE SELECT name FROM Student AS s INNER JOIN prof_script AS p WHERE s.id = p.studId;

# EXPLAIN
-> Inner hash join (s.id = p.studId)  (cost=41.35 rows=40) (actual time=0.026..0.026 rows=0 loops=1)
    -> Table scan on s  (cost=5.00 rows=400) (never executed)
    -> Hash
        -> Table scan on p  (cost=0.35 rows=1) (actual time=0.018..0.018 rows=0 loops=1)
*/