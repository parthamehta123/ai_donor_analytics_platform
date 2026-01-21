DROP TABLE IF EXISTS campaign_metrics;
CREATE TABLE campaign_metrics (
    client_id TEXT PRIMARY KEY,
    impressions INT,
    clicks INT,
    donations INT,
    revenue FLOAT
);

INSERT INTO campaign_metrics VALUES
('abc', 10000, 850, 120, 1500),
('demo', 5000, 200, 50, 400),
('xyz', 8000, 600, 90, 1100);

DROP TABLE IF EXISTS donor_retention;
CREATE TABLE donor_retention (
    client_id TEXT PRIMARY KEY,
    retention_rate FLOAT
);

INSERT INTO donor_retention VALUES
('abc', 0.42),
('demo', 0.33),
('xyz', 0.51);
