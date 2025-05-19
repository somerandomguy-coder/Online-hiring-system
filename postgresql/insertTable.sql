
-- INSERT VALUE
INSERT INTO candidate 
    VALUES (DEFAULT, 'Nam', 'Le', 'aaa@gmail.com', '0426649419', 'NSW', 'DENISTONE', 2000, 'resume/path', 'jessie husband', '2025-4-25 15:00:00');

INSERT INTO status 
    VALUES (1,'password', TRUE, TRUE, TRUE, TRUE, NOW());

INSERT INTO jobpost
    VALUES (DEFAULT,'Saleperson' ,'Sale', 'On Site', 'We''re hiring saleman, come in pls','50K','2025-4-29 11:54:00'), 
    (DEFAULT,'Junior Engineer' ,'Engineer', 'Remote', 'We''re hiring engineer, come in pls','100K', '2025-4-29 11:55:00'),
    (DEFAULT,'Staff Engineer' ,'Engineer', 'Remote', 'We''re hiring engineer, come in pls','200K', '2025-5-29 11:55:00')
