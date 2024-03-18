SELECT students.id AS student_id, students.name AS student_name, subjects.name AS subject_name, ROUND(AVG(grades.grade)) AS average_grade
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
WHERE students.id = ?
GROUP BY students.id, students.name, subjects.name;