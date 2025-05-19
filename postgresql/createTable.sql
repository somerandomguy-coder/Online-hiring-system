DROP TABLE IF EXISTS status;
DROP TABLE IF EXISTS availability;
DROP TABLE IF EXISTS interview;
DROP TABLE IF EXISTS transaction;
DROP TABLE IF EXISTS report;
DROP TABLE IF EXISTS criteria;
DROP TABLE IF EXISTS jobpost;
DROP TABLE IF EXISTS candidate;
DROP TABLE IF EXISTS HRMember;

CREATE TABLE candidate (
    ID          SERIAL          PRIMARY KEY,
    firstName   VARCHAR(255)    NOT NULL,
    lastName    VARCHAR(255),
    email       VARCHAR(255),
    phoneNumber TEXT,
    state       VARCHAR(255),
    suburb      VARCHAR(255),
    postcode    VARCHAR(255),
    resumePath  VARCHAR(255)    NOT NULL,
    jobPosition VARCHAR(20),
    sendAt      TIMESTAMP       NOT NULL
);

CREATE TABLE status (
    ID              INTEGER     NOT NULL REFERENCES candidate(ID),
    password        VARCHAR(10),
    screeningRound  BOOLEAN,
    scheduling      BOOLEAN,
    interviewRound  BOOLEAN,
    acceptOffer     BOOLEAN,
    lastUpdated     TIMESTAMP   NOT NULL
);

CREATE TABLE HRmember (
    ID          SERIAL          PRIMARY KEY,
    password    VARCHAR(8),
    firstName   VARCHAR(255)    NOT NULL,
    lastName    VARCHAR(255),
    email       VARCHAR(255)
);

CREATE TABLE availability(
    availabilityID  SERIAL      PRIMARY KEY,
    HRID            INTEGER     NOT NULL REFERENCES HRmember(ID),
    date            DATE,
    startTime       TIME,
    endTime         TIME
);

CREATE TABLE interview(
    interviewID     SERIAL      PRIMARY KEY,
    HRID            INTEGER     NOT NULL REFERENCES HRmember(ID),
    candidateID     INTEGER     NOT NULL REFERENCES candidate(ID),
    date            DATE,
    startTime       TIME,
    endTime         TIME
);

CREATE TABLE transaction(
    transID     SERIAL      PRIMARY KEY,
    memberID    INTEGER     NOT NULL REFERENCES HRmember(ID),
    category    VARCHAR(20),
    campaign    VARCHAR(20),
    description TEXT,
    amount      INT         NOT NULL,
    timestamp   TIMESTAMP   NOT NULL
);

CREATE TABLE criteria(
    ID          SERIAL      PRIMARY KEY, 
    content     TEXT        NOT NULL
); 

CREATE TABLE report( 
    reportID    SERIAL      PRIMARY KEY,
    memberID    INTEGER     NOT NULL REFERENCES     HRmember(ID),
    candidateID INTEGER     NOT NULL REFERENCES     candidate(ID),
    criteriaID  INTEGER     NOT NULL REFERENCES     criteria(ID),
    content     TEXT        NOT NULL
);

CREATE TABLE jobpost(
    ID          SERIAL      PRIMARY KEY,
    title       VARCHAR(20) NOT NULL,
    department  VARCHAR(8)  NOT NULL,
    worktype    VARCHAR(8)  NOT NULL,
    content     TEXT        NOT NULL,
    salary      TEXT        NOT NULL,
    timestamp   TIMESTAMP   NOT NULL
);


