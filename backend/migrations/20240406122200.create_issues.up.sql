CREATE TABLE IF NOT EXISTS "issues" (
    "id"            SERIAL      PRIMARY KEY,
    "project_id"    INTEGER     NOT NULL      REFERENCES "projects" ("id") ON DELETE CASCADE,
    "title"         TEXT        NOT NULL,
    "description"   TEXT,
    "author_id"     INTEGER     NOT NULL      REFERENCES "accounts" ("id") ON DELETE CASCADE,
    "assignee_id"   INTEGER,
    "status"        TEXT        NOT NULL,
    "created_at"    TIMESTAMP   NOT NULL      DEFAULT CURRENT_TIMESTAMP,
    "updated_at"    TIMESTAMP   NOT NULL      DEFAULT CURRENT_TIMESTAMP
);