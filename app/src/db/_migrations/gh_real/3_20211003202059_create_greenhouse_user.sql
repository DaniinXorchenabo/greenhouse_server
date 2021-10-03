-- upgrade --
CREATE TABLE IF NOT EXISTS "ghuser" (
    "id" UUID NOT NULL  PRIMARY KEY
);
-- downgrade --
DROP TABLE IF EXISTS "ghuser";
