
-- INSERT VALUE
INSERT INTO candidate 
    VALUES (DEFAULT, 'Nam', 'Le', 'aaa@gmail.com', '0426649419', 'NSW', 'DENISTONE', 2000, 'resume/path', 'jessie husband', '2025-4-25 15:00:00');

INSERT INTO status 
    VALUES (1,'password', TRUE, TRUE, TRUE, TRUE, NOW());

INSERT INTO jobpost
    VALUES (DEFAULT,'Saleperson', '28 Miriam rd, Denistone NSW 2000','Sale', 'On Site', 'We''re hiring saleman, come in pls','50K','2025-4-29 11:54:00'), 
    (DEFAULT,'Junior Engineer','55 Kanimbla rd, Rouse Hill NSW 2000' ,'Engineer', 'Remote', 'We''re hiring engineer, come in pls','100K', '2025-4-29 11:55:00'),
    (DEFAULT,'Staff Engineer','1 Ultimo rd, Sydney NSW 2000 UTS' ,'Engineer', 'Remote', 'We''re hiring engineer, come in pls','200K', '2025-5-29 11:55:00'),
    (DEFAULT, 'Product Sales Coordinator', '180 George St, Sydney NSW 2000', 'Sale', 'On Site', 'As we continue to grow, we are seeking a Junior Graphic Designer to join our dynamic Design & Marketing Team. This is an exciting opportunity for a creative individual to contribute to our brand''success while developing their skills in a fast-paced, collaborative environment.\n - Create visually compelling designs for apparel embellishments, including embroidery, vinyl, and sublimation production. \n -Develop digital assets for web, email marketing, and social media campaigns. ', '80k', NOW())
