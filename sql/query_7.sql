SELECT students.name AS student_name, subjects.name AS subject_name, grades.grade
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
WHERE students.group_id = ? AND subjects.id = ?