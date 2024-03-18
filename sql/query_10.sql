SELECT students.name AS student_name, teachers.name AS teacher_name, subjects.name AS subject_name
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE students.id = ? AND teachers.id = ?
GROUP BY subjects.name;