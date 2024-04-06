CREATE "projects" (
    "project_id"  SERIAL      PRIMARY KEY,
    "name"        TEXT        NOT NULL,
    "key"         TEXT        NOT NULL    UNIQUE,
    "description" TEXT,
    "author_id"   INTEGER     NOT NULL,
    "created_at"  TIMESTAMP   NOT NULL    DEFAULT CURRENT_TIMESTAMP,
    "updated_at"  TIMESTAMP   NOT NULL    DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY ("author_id") REFERENCES "accounts" ("account_id") ON DELETE CASCADE
);