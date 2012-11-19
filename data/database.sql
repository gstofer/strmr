BEGIN;
CREATE TABLE IF NOT EXISTS "album" ("id" integer NOT NULL PRIMARY KEY, "name" varchar(30) NOT NULL);
CREATE TABLE IF NOT EXISTS "artist_albums" ("id" integer NOT NULL PRIMARY KEY, "artist_id" integer NOT NULL, "album_id" integer NOT NULL REFERENCES "album" ("id"), UNIQUE ("artist_id", "album_id"));
CREATE TABLE IF NOT EXISTS "artist" ("id" integer NOT NULL PRIMARY KEY, "name" varchar(30) NOT NULL);
CREATE TABLE IF NOT EXISTS "songs_artist" ("id" integer NOT NULL PRIMARY KEY, "songs_id" integer NOT NULL, "artist_id" integer NOT NULL REFERENCES "artist" ("id"), UNIQUE ("songs_id", "artist_id"));
CREATE TABLE IF NOT EXISTS "songs" ("id" integer NOT NULL PRIMARY KEY, "name" varchar(30),"genre" varchar(30),"album_id" integer REFERENCES "album" ("id"),"length" integer,"hash" varchar(40) NOT NULL,"track" integer,"filename" varchar(255) NOT NULL,"path" varchar(255) NOT NULL,"rating" integer);
COMMIT;