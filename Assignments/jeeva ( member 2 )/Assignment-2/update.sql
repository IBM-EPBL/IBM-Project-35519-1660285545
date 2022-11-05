UPDATE "TXZ44264"."User Details"
  SET
  "EMAIL" = 'dummy@mail.com'
  WHERE "USER" = 'dummy';
DELETE FROM "TXZ44264"."User Details"
  WHERE "USER" = 'dummy';