# Write your MySQL query statement below
WITH StudentSubjects AS (
    SELECT s.student_id, s.student_name, su.subject_name
    FROM Students s
    CROSS JOIN Subjects su
),
AttendanceCount AS (
    SELECT ss.student_id, ss.student_name, ss.subject_name, COUNT(e.subject_name) AS attended_exams
    FROM StudentSubjects ss
    LEFT JOIN Examinations e
    ON ss.student_id = e.student_id AND ss.subject_name = e.subject_name
    GROUP BY ss.student_id, ss.student_name, ss.subject_name
)
SELECT student_id, student_name, subject_name, attended_exams
FROM AttendanceCount
ORDER BY student_id, subject_name;
