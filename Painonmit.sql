CREATE VIEW henkilo_mittaus_ika AS
SELECT henkilo.henkilo_id, henkilo.sukunimi, henkilo.etunimi, mittaus.mittaus_id, mittaus.pituus, mittaus.paino, henkilo.spaiva, date('now') AS tanaan. (julianday('now') -
FROM henkilo LEFT OUTER JOIN mittaus ON henkilo.henkilo_id = mittaus.henkilo_id