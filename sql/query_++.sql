SELECT students.id AS student_id, students.name AS student_name, grades.grade
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
WHERE students.group_id = :group_id
  AND subjects.id = :subject_id
  AND grades.date = (
      SELECT MAX(date)
      FROM grades
      WHERE grades.student_id = students.id
        AND grades.subject_id = subjects.id
  );