# Write your MySQL query statement below
SELECT friend_id AS id, COUNT(*) AS num
FROM
    (SELECT requester_id AS friend_id FROM RequestAccepted
     UNION ALL
     SELECT accepter_id AS friend_id FROM RequestAccepted) AS all_friends
GROUP BY friend_id
ORDER BY num DESC
LIMIT 1;
