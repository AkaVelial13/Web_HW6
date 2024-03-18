SELECT g.name AS group_name, ROUND(AVG(grade)) AS average_grade
FROM students s
JOIN groups g ON s.group_id = g.id
JOIN grades gr ON s.id = gr.student_id
WHERE gr.subject_id = :subject_id
GROUP BY g.id