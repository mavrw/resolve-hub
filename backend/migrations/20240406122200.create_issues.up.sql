CREATE "issues" (
    "issue_id"    SERIAL      PRIMARY KEY,
    "project_id"  INTEGER     NOT NULL,
    "title"       TEXT        NOT NULL,
    "description" TEXT,
    "author_id"   INTEGER     NOT NULL,
    "assignee_id" INTEGER,
    "status"      TEXT        NOT NULL,
    "created_at"  TIMESTAMP   NOT NULL    DEFAULT CURRENT_TIMESTAMP,
    "updated_at"  TIMESTAMP   NOT NULL    DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY ("project_id") REFERENCES "projects" ("project_id") ON DELETE CASCADE,
    FOREIGN KEY ("author_id") REFERENCES "accounts" ("account_id") ON DELETE CASCADE
);