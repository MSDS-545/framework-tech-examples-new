-- Create a small table solely to demonstrate PostgreSQL data types and constraints.
CREATE TABLE IF NOT EXISTS framework_notes (
    -- BIGSERIAL automatically generates increasing integer identifiers.
    id BIGSERIAL PRIMARY KEY,
    -- NOT NULL requires every row to have a framework name.
    framework_name VARCHAR(100) NOT NULL,
    -- TEXT is suitable for variable-length descriptive content.
    description TEXT NOT NULL,
    -- PostgreSQL supplies the current timestamp when a row is inserted.
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Add a few rows for SELECT demonstrations.
INSERT INTO framework_notes (framework_name, description) VALUES
('Django', 'Python web framework with an ORM and template system.'),
('FastAPI', 'Python framework focused on typed APIs.'),
('Express.js', 'Web framework that runs on Node.js.');
