CREATE "issue_blockers" (
    "blocker_id" SERIAL PRIMARY KEY,
    "blocked_issue_id" INTEGER NOT NULL,
    "blocking_issue_id" INTEGER NOT NULL,
    "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY ("blocked_issue_id") REFERENCES "issues" ("issue_id") ON DELETE CASCADE,
    FOREIGN KEY ("blocking_issue_id") REFERENCES "issues" ("issue_id") ON DELETE CASCADE
);