-- READ: return all rows, newest first.
SELECT id, framework_name, description, created_at
FROM framework_notes
ORDER BY created_at DESC;

-- CREATE: add another row.
INSERT INTO framework_notes (framework_name, description)
VALUES ('React', 'JavaScript library for component-based user interfaces.');

-- UPDATE: change a row selected by its framework name.
UPDATE framework_notes
SET description = 'React builds component-based browser user interfaces.'
WHERE framework_name = 'React';

-- DELETE: remove the demonstration row.
DELETE FROM framework_notes
WHERE framework_name = 'React';
