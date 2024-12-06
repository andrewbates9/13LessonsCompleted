CREATE TABLE Students(id INTEGER PRIMARY KEY AUTOINCREMENT,
                    firstname TEXT NOT NULL,
                    lastname TEXT NOT NULL,
                    dob TEXT NOT NULL);

CREATE TABLE Marks(id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id INTEGER,
                    subject TEXT NOT NULL,
                    mark INTEGER);


INSERT INTO Students(firstname, lastname, dob) VALUES
                    ('Jim', 'Smith', '26/09/2007'),
                    ('Mary', 'Jones', '03/04/2007'),
                    ('Bob', 'Bobby', '10/01/2007'),
                    ('Josey', 'Wales', '23/10/2007'),
                    ('Tabitha', 'Johnson', '28/02/2007'),
                    ('Jennifer', 'Rose', '14/09/2007'),
                    ('Bart', 'Michael', '11/10/2007'),
                    ('Tom', 'Penn', '19/07/2007');

INSERT INTO Marks(student_id, subject, mark) VALUES
                    (1, 'English', 50),
                    (1, 'Maths', 100),
                    (2, 'English', 67),
                    (2, 'Science', 80),
                    (3, 'English', 24),
                    (4, 'English', 97),
                    (5, 'Maths', 82),
                    (5, 'Science', 5);
