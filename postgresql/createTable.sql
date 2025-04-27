DROP TABLE IF EXISTS candidate;
DROP TABLE IF EXISTS status;
DROP TABLE IF EXISTS HRMember;
DROP TABLE IF EXISTS availability;
DROP TABLE IF EXISTS interview;
DROP TABLE IF EXISTS transaction;
DROP TABLE IF EXISTS criteria;
DROP TABLE IF EXISTS report;

CREATE TABLE candidate (
    ID          VARCHAR(8)      NOT NULL PRIMARY KEY,
    firstName   VARCHAR(255)    NOT NULL,
    lastName    VARCHAR(255),
    email       VARCHAR(255),
    state       VARCHAR(255),
    suburb      VARCHAR(255),
    postcode    VARCHAR(255),
    resume      TEXT NOT NULL,
    coverLetter TEXT,
    jobPosition VARCHAR(20),
    sendAt      DATE
);

CREATE TABLE status (
    ID              VARCHAR(8) NOT NULL REFERENCES candidate(ID),
    password        VARCHAR(10),
    screeningRound  BOOLEAN,
    scheduling      BOOLEAN,
    interviewRound  BOOLEAN,
    acceptOffer     BOOLEAN,
    lastUpdated     DATE
);

CREATE TABLE HRmember (
    ID          VARCHAR(8)      NOT NULL PRIMARY KEY,
    password    VARCHAR(8),
    firstName   VARCHAR(255)    NOT NULL,
    lastName    VARCHAR(255),
    email       VARCHAR(255)
);

CREATE TABLE availability(
    availabilityID  VARCHAR(8)  NOT NULL PRIMARY KEY,
    HRID            VARCHAR(8)  NOT NULL REFERENCES HRmember(ID),
    date            DATE,
    startTime       TIME,
    endTime         TIME
);

CREATE TABLE interview(
    interviewID     VARCHAR(8) NOT NULL PRIMARY KEY,
    HRID            VARCHAR(8) NOT NULL REFERENCES HRmember(ID),
    candidateID     VARCHAR(8) NOT NULL REFERENCES candidate(ID),
    date            DATE,
    startTime       TIME,
    endTime         TIME
);

CREATE TABLE transaction(
    transID     VARCHAR(8)  NOT NULL PRIMARY KEY,
    memberID    VARCHAR(8)  NOT NULL REFERENCES HRmember(ID),
    category    VARCHAR(20),
    campaign    VARCHAR(20),
    description TEXT,
    amount      INT         NOT NULL,
    timestamp   TIMESTAMP   NOT NULL
);

CREATE TABLE criteria(
    ID          VARCHAR(8)  NOT NULL PRIMARY KEY, 
    content     TEXT        NOT NULL
); 

CREATE TABLE report( 
    repostID    VARCHAR(8)  NOT NULL PRIMARY KEY,
    memberID    VARCHAR(8)  NOT NULL REFERENCES     HRmember(ID),
    candidateID VARCHAR(8)  NOT NULL REFERENCES     candidate(ID),
    criteriaID  VARCHAR(8)  NOT NULL REFERENCES     criteria(ID),
    content     TEXT        NOT NULL
)
