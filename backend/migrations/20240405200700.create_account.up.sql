CREATE "accounts" (
    "account_id"  SERIAL      PRIMARY KEY,
    "first_name"  TEXT        NOT NULL,
    "last_name"   TEXT        NOT NULL,
    "email"       TEXT        NOT NULL    UNIQUE,
    "password"    TEXT        NOT NULL,
    "verified"    BOOLEAN     NOT NULL    DEFAULT FALSE,
    "created_at"  TIMESTAMP   NOT NULL    DEFAULT CURRENT_TIMESTAMP
    "updated_at"  TIMESTAMP   NOT NULL    DEFAULT CURRENT_TIMESTAMP
);