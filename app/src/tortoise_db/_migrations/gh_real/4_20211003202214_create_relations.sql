-- upgrade --
ALTER TABLE "ghuser" ADD "gh_id_id" UUID NOT NULL;
ALTER TABLE "ghuser" ADD "user_id_id" UUID NOT NULL;
ALTER TABLE "ghuser" ADD CONSTRAINT "fk_ghuser_user_2245c4c1" FOREIGN KEY ("user_id_id") REFERENCES "user" ("id") ON DELETE CASCADE;
ALTER TABLE "ghuser" ADD CONSTRAINT "fk_ghuser_greenhou_05e22f1c" FOREIGN KEY ("gh_id_id") REFERENCES "greenhouse" ("id") ON DELETE CASCADE;
-- downgrade --
ALTER TABLE "ghuser" DROP CONSTRAINT "fk_ghuser_greenhou_05e22f1c";
ALTER TABLE "ghuser" DROP CONSTRAINT "fk_ghuser_user_2245c4c1";
ALTER TABLE "ghuser" DROP COLUMN "gh_id_id";
ALTER TABLE "ghuser" DROP COLUMN "user_id_id";
