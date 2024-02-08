create schema Hotel;

-- Table representing a hotel
-- In the following database, I operate on one hotel (with id=1)
CREATE TABLE IF NOT EXISTS Hotel.Hotel
(
    hotel_ID serial PRIMARY KEY,
    name character varying(30) NOT NULL,
    address character varying(100) NOT NULL,
    phone_number character varying(12) NOT NULL,
    e_mail character varying(50) NOT NULL,
    description text,
    star_rating int not null
);

-- Room type - name, description, price per night, whether pets are allowed, and the capacity of the roomCREATE TABLE IF NOT EXISTS Hotel.Room_type
(
    room_type_ID serial PRIMARY KEY,
    name character varying(50) NOT NULL,
    description text,
    price_per_night numeric(6, 2) NOT NULL,
    pet_friendly boolean NOT NULL DEFAULT false,
    capacity integer NOT NULL
);

-- Room - its type, door number, and the hotel it is located in
CREATE TABLE IF NOT EXISTS Hotel.Room
(
    room_ID serial PRIMARY KEY,
    room_type integer NOT NULL references Hotel.Room_type,
    door_number integer NOT NULL,
    hotel_ID integer NOT NULL references Hotel.Hotel
);

-- Guest - First name, last name, phone number, and email address
CREATE TABLE IF NOT EXISTS Hotel.Guest
(
    guest_ID serial NOT NULL PRIMARY KEY,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    phone_number character varying(12) NOT NULL,
    e_mail character varying(50) NOT NULL
);

-- Reservation for a hotel stay with check-in and check-out dates
CREATE TABLE IF NOT EXISTS Hotel.Booking
(
    booking_ID serial PRIMARY KEY,
    room_ID integer NOT NULL references Hotel.Room,
    guest_ID integer NOT NULL references Hotel.Guest,
    check_in_date date NOT NULL,
    check_out_date date NOT NULL
);

-- Services provided during a hotel stay but additionally payable
CREATE TABLE IF NOT EXISTS Hotel.Service
(
    service_ID serial PRIMARY KEY,
    name character varying(30) NOT NULL,
    description text,
    price numeric(5, 2) NOT NULL
);

-- Table of services used during a specific hotel stay
CREATE TABLE IF NOT EXISTS Hotel.Booked_service
(
    Booked_service_ID serial PRIMARY KEY,
    booking_ID integer NOT NULL references Hotel.Booking,
    service_ID integer NOT NULL references Hotel.Service
);

-- Opinion about services provided in the hotel
CREATE TABLE IF NOT EXISTS Hotel.Review
(
    review_ID serial PRIMARY KEY,
    booking_ID integer references Hotel.Booking,
    booked_service_ID integer references Hotel.Booked_service(booked_service_ID),
    rating integer NOT NULL,
    review_text text
);

INSERT INTO Hotel.Hotel (name, address, phone_number, e_mail, description, star_rating) 
VALUES 
('Chata', 'ul. Zimowa 18, 30-101, Zimów, Polska', '101202303', 'chata@kontakt.com', 'Chata is a charming hotel located in a picturesque mountain 
setting.\nOur hotel offers unforgettable experiences in a winter scenery, surrounded by white snow and breathtaking views.\nWe are far away from 
the city hustle, in the heart of mountain nature, providing our guests with peace and relaxation.\nThe interiors of Chata exude the warmth of a 
fireplace and rustic charm, creating the perfect atmosphere for relaxation after a day on the slopes or mountain hikes.\nWelcome to Chata - 
where nature and comfort come together to create unforgettable memories of a mountain stay.', 4);

INSERT INTO Hotel.Room_type (name, description, price_per_night, pet_friendly, capacity) VALUES 
('Standard Room', 'Cozy room with a mountain view for two people, with twin beds and a bathroom', 150.00, true, 2),
('Premium Suite', 'Spacious suite with a living room and a bedroom with a double bed, and a large balcony', 300.00, false, 2),
('Family Suite 2+2', 'Room with a double bed for parents, connected to a room with two separate beds for children, with a shared bathroom', 270.00, true, 4),
('Standard Room 3-person', 'Room with three single beds and a bathroom', 225.00, false, 3),
('Standard Room 4-person', 'Room with four single beds, balcony with mountain view, and a bathroom', 290.00, false, 4);

INSERT INTO Hotel.Room (room_type, door_number, hotel_ID) VALUES 
(1, 101, 1),
(1, 102, 1),
(1, 103, 1),
(2, 201, 1),
(2, 202, 1),
(2, 203, 1),
(3, 301, 1),
(3, 302, 1),
(3, 303, 1),
(4, 401, 1),
(4, 402, 1),
(4, 403, 1),
(5, 501, 1),
(5, 502, 1),
(5, 503, 1);

INSERT INTO Hotel.Guest (first_name, last_name, phone_number, e_mail) VALUES 
('Jan', 'Kowalski', '123456789', 'jan.kowalski@gmail.com'),
('Anna', 'Nowak', '987654321', 'anna.nowak@gmail.com'),
('Piotr', 'Wiśniewski', '555444333', 'piotr.wisniewski@gmail.com'),
('Maria', 'Dąbrowska', '111222333', 'maria.dabrowska@gmail.com'),
('Aleksandra', 'Kowalczyk', '999888777', 'aleksandra.kowalczyk@gmail.com'),
('Tomasz', 'Lewandowski', '333222111', 'tomasz.lewandowski@gmail.com'),
('Magdalena', 'Zając', '444555666', 'magdalena.zajac@gmail.com'),
('Wojciech', 'Szymański', '777888999', 'wojciech.szymanski@gmail.com'),
('Alicja', 'Woźniak', '666777888', 'alicja.wozniak@gmail.com'),
('Kamil', 'Jankowski', '111333555', 'kamil.jankowski@gmail.com'),
('Martyna', 'Kaczmarek', '999111222', 'martyna.kaczmarek@gmail.com'),
('Paweł', 'Mazur', '444666888', 'pawel.mazur@gmail.com');

INSERT INTO Hotel.Booking (room_ID, guest_ID, check_in_date, check_out_date) VALUES 
(1, 1, '2023-01-10', '2023-01-17'), --1
(3, 5, '2023-03-02', '2023-03-10'), --2
(2, 8, '2023-04-20', '2023-04-25'), --3
(5, 11, '2023-05-15', '2023-05-20'), --4
(4, 6, '2023-06-10', '2023-06-15'), --5
(6, 9, '2023-07-05', '2023-07-10'), --6
(10, 12, '2023-08-30', '2023-09-04'), --7
(3, 7, '2023-09-25', '2023-09-30'), --8
(1, 1, '2023-02-22', '2023-02-25'), --9
(2, 2, '2023-03-15', '2023-03-27'), --10
(3, 3, '2023-04-30', '2023-05-02'), --11
(4, 4, '2023-05-24', '2023-05-30'), --12
(5, 5, '2023-06-23', '2023-06-25'), --13
(6, 6, '2023-07-18', '2023-07-20'), --14
(7, 7, '2023-08-30', '2023-09-04'), --15
(8, 8, '2023-09-16', '2023-09-30'), --16
(9, 9, '2023-10-20', '2023-10-27'), --17
(10, 10, '2023-11-15', '2023-11-20'), --18
(11, 11, '2023-12-30', '2024-01-04'), --19
(12, 12, '2024-01-25', '2024-01-30'), --20
(13, 1, '2024-02-16', '2024-02-25'), --21
(14, 2, '2024-03-15', '2024-03-23'), --22
(15, 3, '2024-04-25', '2024-05-05'); --23


INSERT INTO Hotel.Service (name, description, price) VALUES 
('Highland Breakfast', 'Buffet with traditional dishes made from local products', 20.00),
('Relaxation Massage', 'Professional massage for relaxation - 1 hour', 50.00),
('Swimming Pool', 'Access to the pool with two 25-meter lanes, recreational pool, and jacuzzi', 60.00),
('Sauna', 'Access to two saunas - dry and wet', 60.00),
('Sauna + Pool', 'Sauna and pool package', 100.00);

INSERT INTO Hotel.Booked_service (booking_ID, service_ID) VALUES 
(1, 1),
(1, 2),
(2, 3),
(3, 5),
(4, 1),
(4, 2),
(5, 3),
(6, 5),
(7, 1),
(7, 2),
(7, 4),
(8, 1),
(9, 4),
(10, 3);


INSERT INTO Hotel.Review (booking_ID, booked_service_ID, rating, review_text)
VALUES 
(1, 1, 5, 'Great breakfast! Very tasty and varied meals.'),
(2, 3, 4, 'The pool is well-maintained, spacious, and enjoyable.'),
(3, 4, 4, 'Very relaxing pool and sauna, a great place to unwind.'),
(4, 6, 5, 'The massage was fantastic, I completely relaxed.'),
(5, 7, 4, 'Great pool, suitable for both small and larger children.'),
(6, 8, 3, 'The pool was okay, but the sauna could be better maintained.'),
(7, 10, 5, 'The massage was excellent, I recommend it to everyone!'),
(8, 12, 4, 'Tasty breakfast, great selection of dishes.'),
(9, 13, 5, 'Super saunas and tubs with icy water.'),
(10, 14, 3, 'The pool was okay, but I expected something more.');



-- VIEWS

-- Overview of guests who used any service and provided feedback about it
CREATE VIEW Guest_Service_Reservations_With_Reviews AS
SELECT
	g.first_name AS first_name,
    g.last_name AS last_name,
    s.name AS used_service,
    rv.rating AS rating,
    rv.review_text as opinion
FROM
    Hotel.Guest g
JOIN
    Hotel.Booking b ON g.guest_ID = b.guest_ID
LEFT JOIN
    Hotel.Booked_service bs ON b.booking_ID = bs.booking_ID
LEFT JOIN
    Hotel.Service s ON bs.service_ID = s.service_ID
LEFT JOIN
    Hotel.Review rv ON b.booking_ID = rv.booking_ID AND bs.booked_service_ID = rv.booked_service_ID
where bs.service_ID is not null and rv.review_ID is not null;



-- Overview of revenues for the Chata hotel in the year 2023. Payments for the stay are made before the start of the hotel stay.
CREATE VIEW Monthly_revenue AS
SELECT
    EXTRACT(MONTH FROM b.check_in_date) AS month_nr,
    SUM(rt.price_per_night * (b.check_out_date - b.check_in_date)) AS Room_revenue,
    COALESCE(SUM(s.price),0) AS Services_revenue,
	SUM(rt.price_per_night * (b.check_out_date - b.check_in_date) + COALESCE(s.price, 0)) as Total_revenue
FROM
    Hotel.Booking b
JOIN
    Hotel.Room r ON b.room_ID = r.room_ID
JOIN
    Hotel.Room_type rt ON r.room_type = rt.room_type_ID
JOIN
    Hotel.Hotel h ON r.hotel_ID = h.hotel_ID
LEFT JOIN
    Hotel.Booked_service bs ON b.booking_ID = bs.booking_ID
LEFT JOIN
    Hotel.Service s ON bs.service_ID = s.service_ID
WHERE
    h.hotel_ID = 1 and EXTRACT(YEAR FROM b.check_in_date) = 2023
GROUP BY
    EXTRACT(MONTH FROM b.check_in_date)
ORDER BY
    EXTRACT(MONTH FROM b.check_in_date);


-- Overview of average duration of stay of guests, who stayed at the hotel at least two times
CREATE VIEW Average_duration_of_stay AS
SELECT
    g.first_name as first_name,
    g.last_name as last_name,
	COUNT(DISTINCT b.booking_ID) as number_of_stays,
    round(cast(AVG(b.check_out_date - b.check_in_date) as numeric), 2) AS Average_duration_of_stay
FROM
    Hotel.Guest g
JOIN
    Hotel.Booking b ON g.guest_ID = b.guest_ID
GROUP BY
    g.first_name, g.last_name
HAVING
     COUNT(DISTINCT b.booking_ID) >= 2
ORDER BY
    g.last_name;
