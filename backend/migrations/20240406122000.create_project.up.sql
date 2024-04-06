CREATE TABLE IF NOT EXISTS "projects" (
    "id"            SERIAL      PRIMARY KEY,
    "name"          TEXT        NOT NULL,
    "key"           TEXT        NOT NULL      UNIQUE,
    "description"   TEXT,
    "author_id"     INTEGER     NOT NULL      REFERENCES "accounts" ("id") ON DELETE CASCADE,
    "created_at"    TIMESTAMP   NOT NULL      DEFAULT CURRENT_TIMESTAMP,
    "updated_at"    TIMESTAMP   NOT NULL      DEFAULT CURRENT_TIMESTAMP
);