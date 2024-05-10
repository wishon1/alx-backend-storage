-- Write a SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student.
-- Note: An average score can be a decimal
-- Requirements:
-- Procedure ComputeAverageScoreForUser is taking 1 input:
-- user_id, a users.id value (you can assume user_id is linked to an existing users)

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE num_corrections INT;

    -- Calculate total score for the user
    SELECT SUM(score) INTO total_score
    FROM corrections
    WHERE user_id = user_id;

    -- Count the number of corrections for the user
    SELECT COUNT(*) INTO num_corrections
    FROM corrections
    WHERE user_id = user_id;

    -- Calculate average score
    IF num_corrections > 0 THEN
        UPDATE users
        SET average_score = total_score / num_corrections
        WHERE id = user_id;
    END IF;
END $$

DELIMITER ;
