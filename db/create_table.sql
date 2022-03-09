CREATE TABLE IF NOT EXISTS training (
    id INTEGER NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS exercises (
    id INTEGER NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO 'training' VALUES (1.'push', 2.'pull', 3.'legs', 4.'HIIT', 5.'Crossfit', 6.'Cardio')

INSERT INTO 'exercises' VALUES (1.'Bench Press', 2.'Dumbbell flat press', 3.'Chest Fly', 4.'Incline Bench Press', 5.'Decline Press', 6.'Press Ups', 7.'Dips', 8.'Pullover', 9.'Lat Pulldown', 10.'T-bar Row', 11.'Pull Ups', 12.'Shrugs', 13.'Squats', 14.'Romanian Deadlift', 15.'Deadlift', 16.'Hack squat', 17.'Bulgarian splits', 18.'Sumo squats', 19.'lunges', 20).'Box Jump', 21.'Ski-Erg', 22.'Vertical CLimber', 23.'dumbbell snatches', 24.'Rowing machine', 25.'Air Bike'