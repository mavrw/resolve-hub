CREATE TABLE IF NOT EXISTS "issue_blockers" (
    "id"                SERIAL      PRIMARY KEY,
    "blocked_issue_id"  INTEGER     NOT NULL    REFERENCES "issues" ("id") ON DELETE CASCADE,
    "blocking_issue_id" INTEGER     NOT NULL    REFERENCES "issues" ("id") ON DELETE CASCADE,
    "created_at"        TIMESTAMP   NOT NULL    DEFAULT CURRENT_TIMESTAMP,
    "updated_at"        TIMESTAMP   NOT NULL    DEFAULT CURRENT_TIMESTAMP
);