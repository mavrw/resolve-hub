CREATE TABLE IF NOT EXISTS "issue_relationships" (
    "id"                SERIAL      PRIMARY KEY,
    "parent_issue_id"   INTEGER     NOT NULL    REFERENCES "issues" ("id") ON DELETE CASCADE,
    "child_issue_id"    INTEGER     NOT NULL    REFERENCES "issues" ("id") ON DELETE CASCADE,
    "created_at"        TIMESTAMP   NOT NULL    DEFAULT CURRENT_TIMESTAMP,
    "updated_at"        TIMESTAMP   NOT NULL    DEFAULT CURRENT_TIMESTAMP
);