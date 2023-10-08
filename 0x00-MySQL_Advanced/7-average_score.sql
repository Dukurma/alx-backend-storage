-- A SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the
-- average score for a student. Note: An average score can be a decimal
-- Procedure ComputeAverageScoreForUser is taking 1 input:
-- user_id, a users.id value (you can assume user_id is linked to an existing users)

DELIMITER $$;

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_score DECIMAL(10,2);

    SELECT AVG(score) INTO avg_score
    FROM scores
    WHERE user_id = user_id;

    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;
END;$$

DELIMITER ;
