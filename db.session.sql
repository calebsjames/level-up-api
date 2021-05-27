SELECT organizer_id as GamerID, first_name || " " || last_name as Organizer, levelupapi_event.id as EventId, date, time, title as Game
FROM levelupapi_event

    INNER JOIN auth_user
    ON auth_user.id = levelupapi_event.organizer_id

    INNER JOIN levelupapi_game
    ON levelupapi_game.id = levelupapi_event.game_id

