-- Topics table
CREATE TABLE IF NOT EXISTS Topic (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic TEXT NOT NULL
);

-- Insert the topics
INSERT INTO Topic (topic) VALUES
    ('happy'),
    ('inspirational'),
    ('sad'),
    ('love'),
    ('money'),
    ('knowledge');

-- Create the quotes table
CREATE TABLE IF NOT EXISTS Quote (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL,
    author TEXT
);

-- Create the table for the relationship between quotes and topics
CREATE TABLE IF NOT EXISTS QuoteTopic (
    quote_id INTEGER,
    topic_id INTEGER,
    FOREIGN KEY (quote_id) REFERENCES Quote(id),
    FOREIGN KEY (topic_id) REFERENCES Topic(id),
    PRIMARY KEY (quote_id, topic_id)
);
