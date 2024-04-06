CREATE "issue_hierarchies" (
    "relationship_id" SERIAL PRIMARY KEY,
    "parent_id" INTEGER NOT NULL,
    "child_id" INTEGER NOT NULL,
    "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY ("parent_id") REFERENCES "issues" ("issue_id") ON DELETE CASCADE,
    FOREIGN KEY ("child_id") REFERENCES "issues" ("issue_id") ON DELETE CASCADE
);