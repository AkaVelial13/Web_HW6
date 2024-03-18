SELECT s.name AS student_name, AVG(g.grade) AS average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.subject_id = :subject_id
GROUP BY s.id
ORDER BY average_grade DESC
LIMIT 1;