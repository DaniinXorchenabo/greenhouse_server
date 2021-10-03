-- upgrade --
CREATE TABLE IF NOT EXISTS "greenhouse" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "name" VARCHAR(50)
);
-- downgrade --
DROP TABLE IF EXISTS "greenhouse";
