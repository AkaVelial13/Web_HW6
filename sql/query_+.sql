SELECT students.id AS student_id, students.name AS student_name, subjects.name AS subject_name, ROUND(AVG(grades.grade)) AS average_grade, teachers.id AS teacher_id, teachers.name AS teacher_name
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE teachers.id = :teacher_id
  AND students.id = :student_id
GROUP BY students.id, students.name, subjects.name;
