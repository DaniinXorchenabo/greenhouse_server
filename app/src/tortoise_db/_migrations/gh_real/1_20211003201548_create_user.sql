-- upgrade --
CREATE TABLE IF NOT EXISTS "user" (
    "_scopes" VARCHAR(50) NOT NULL  DEFAULT '',
    "id" UUID NOT NULL  PRIMARY KEY,
    "username" VARCHAR(50) NOT NULL UNIQUE,
    "name" VARCHAR(100),
    "surname" VARCHAR(100),
    "hashed_password" VARCHAR(4096) NOT NULL,
    "email" VARCHAR(100) NOT NULL UNIQUE
);
COMMENT ON COLUMN "user"."_scopes" IS 'Разрешения для пользователя, приписанные нотацией OAuth2';
-- downgrade --
DROP TABLE IF EXISTS "user";
